#!/usr/bin/env bash
# lodestone-pretool-hook.sh
#
# Lodestone-aware PreToolUse hook for Claude Code. Detects action
# patterns that map to Lodestone methodology concepts and surfaces the
# relevant protocol guidance to the assistant's context at the moment of
# action.
#
# Composes with cma's PreToolUse hook (see https://github.com/Clarethium/cma):
# cma surfaces past captures matching the action's surface; this surfaces
# methodology protocols. Past captures are operator-specific and grow over
# time; protocols are universal and stable. Together they cover both ends
# of the action-time injection layer.
#
# Install: add to ~/.claude/settings.json alongside cma's hook if present.
#
#   "hooks": {
#     "PreToolUse": [
#       {
#         "hooks": [
#           {
#             "type": "command",
#             "command": "bash /path/to/lodestone/tools/lodestone-pretool-hook.sh"
#           }
#         ]
#       }
#     ]
#   }
#
# Failure-isolated: any internal error exits silently with code 0; the
# wrapped tool call always proceeds. Requires python3 on PATH.

set -uo pipefail

# Drain stdin JSON from Claude Code's hook payload.
stdin_payload=""
if [[ ! -t 0 ]]; then
    stdin_payload=$(cat)
fi

# No stdin and no useful env var fallback: nothing to do.
if [[ -z "$stdin_payload" ]]; then
    exit 0
fi

python3 - "$stdin_payload" <<'PYEOF'
import json
import re
import sys

stdin_json = sys.argv[1]

try:
    data = json.loads(stdin_json)
except json.JSONDecodeError:
    sys.exit(0)

tool_name = data.get("tool_name", "")
tool_input = data.get("tool_input", {})
if not isinstance(tool_input, dict):
    sys.exit(0)

# Only surface for tools that touch files or run commands.
relevant_tools = {"Edit", "Write", "MultiEdit", "NotebookEdit", "Bash"}
if tool_name not in relevant_tools:
    sys.exit(0)

# Extract context.
file_path = ""
command = ""
if tool_name in ("Edit", "Write", "MultiEdit", "NotebookEdit"):
    file_path = tool_input.get("file_path") or tool_input.get("notebook_path") or ""
elif tool_name == "Bash":
    command = tool_input.get("command", "")

text_to_match = (file_path + " " + command).lower()

# Detection rules. Each returns a (concept_label, cue_text) tuple when
# the rule matches the current action. Rules are designed to be specific
# enough to avoid false positives on common operations; refine in place
# as false positives are observed in actual use.
cues = []

# Authentication surface. Edit/Write or shell commands touching paths or
# keywords that indicate authentication, sessions, credentials, or
# payments. The protocol below is the Section VII auth discipline pared
# to its methodology-level rule; OWASP carries the tactical canon.
if re.search(r"\b(auth|login|session|jwt|oauth|password|credential|payment|stripe|billing|checkout)\b", text_to_match):
    cues.append((
        "Authentication, authorization, and payments (Section VII)",
        "Validate inputs at the boundary, by allow-list rather than deny-list. "
        "Require both authentication and resource-specific authorization on protected routes. "
        "Rate-limit sensitive endpoints. Treat secrets as configuration, not code. "
        "Audit-log sensitive operations. Never trust client-side state for security decisions. "
        "Never store credentials in reversible form. "
        "Tactical canon: OWASP."
    ))

# Database surface. Edit/Write to schema, migration, or database-shaped
# paths. Section VII database protocol.
if re.search(r"\b(schema|migration|/model|database|db/)\b", text_to_match) or re.search(r"\.sql\b", text_to_match):
    cues.append((
        "Database surface (Section VII)",
        "Read the exact schema before any change. Identify required vs optional vs auto-generated fields. "
        "Plan rollback before changes. Check existing migration patterns."
    ))

# Git write operations. Bash commands that modify version control state.
# Section VII git protocol.
if tool_name == "Bash" and re.search(r"\bgit\s+(commit|push|merge|reset|rebase|cherry-pick|branch\s+-D|checkout\s+--|restore\s+--|clean\s+-f)", command):
    cues.append((
        "Git write operation (Section VII)",
        "Check status before any write. Stage explicit files only, never `git add .` or `git reset HEAD`. "
        "Ask before touching files you did not modify. When stuck, stop and state what is seen rather than guessing."
    ))

# Deletion without understanding. Bash commands that remove code, files,
# or data at scale. Section V failure-shape Deletion without understanding.
if tool_name == "Bash" and re.search(r"(\brm\s+-[rf]|\brm\s+--recursive|\bdrop\s+table|\btruncate\s+table|\bdelete\s+from)", command, re.IGNORECASE):
    cues.append((
        "Deletion without understanding (Section V)",
        "Before removing code or data: git blame to learn why it was added; grep for what depends on it; "
        "run tests after removal to confirm nothing broke. When the answer is unclear, ask."
    ))

# Pattern Study trigger. Creating a new file in a critical surface.
# Encourages the three-similar-features study before writing.
if tool_name == "Write" and re.search(r"\b(auth|login|payment|stripe|schema|migration|/api/|route|endpoint|controller|handler)\b", text_to_match):
    cues.append((
        "Pattern Study (Section VII)",
        "Before writing new code in this surface, find three similar features already implemented and read "
        "their complete implementations. Where the three are uniform, follow the uniform pattern; where they "
        "vary, follow the strongest. Convention emerges from three, not one."
    ))

# Output cues. Silent on no match.
if cues:
    print("Lodestone protocols relevant to this action:")
    print()
    for concept, cue in cues:
        print(f"**{concept}**")
        print(cue)
        print()
PYEOF
