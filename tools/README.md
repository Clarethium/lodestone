# Lodestone tools

Lodestone-aware integrations that surface methodology protocols at the moment of action.

These are reference implementations, not the methodology itself. The methodology lives in the canonical sections; these tools deliver pieces of it into an operator's workflow.

## What's here

### `lodestone-pretool-hook.sh`

A Claude Code `PreToolUse` hook that detects action patterns relevant to Lodestone concepts and surfaces the relevant protocol guidance to the assistant's context.

What it does on each tool call:

1. Reads the Claude Code hook JSON payload from stdin.
2. Inspects the tool name, file path, and command for Lodestone-relevant signals.
3. Emits matching methodology cues to stdout, where Claude Code injects them as additional context for the assistant.

Silent on no match. Failure-isolated: any internal error exits 0 so the wrapped tool call always proceeds.

Detection rules in v1:

| Rule | Trigger | Surfaces |
|------|---------|----------|
| Authentication surface | Edit/Write/Bash touching auth, sessions, credentials, or payments | Section VII auth discipline |
| Database surface | Edit/Write to schema, migration, or `.sql` paths | Section VII database protocol |
| Git write operations | Bash commands that modify version control state | Section VII git protocol |
| Deletion without understanding | Bash commands that remove code, files, or data at scale | Section V failure-shape |
| Pattern Study trigger | Creating a new file in a critical surface | Section VII Pattern Study |

The rules are deliberately conservative: each trigger pattern is specific enough to avoid surfacing on routine operations. Refine in place as false positives or false negatives are observed.

### Composition with `cma`

This hook composes with [cma](https://github.com/Clarethium/cma)'s `PreToolUse` hook rather than replacing it. cma surfaces past captures matching the action's surface; this hook surfaces methodology protocols. Past captures are operator-specific and accumulate over time; protocols are universal and stable. Both run together; either runs alone.

A new Lodestone reader who has not yet captured any failures still receives methodology guidance from this hook. An operator running cma alone receives capture surfacing without methodology cues. Running both gives both.

### Install

Requires `python3` on PATH. No other dependencies.

Add to `~/.claude/settings.json` alongside cma's hook if present:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash /path/to/lodestone/tools/lodestone-pretool-hook.sh"
          }
        ]
      }
    ]
  }
}
```

If you already have cma's `PreToolUse` hook installed, add this as an additional entry in the `PreToolUse` array; both hooks will run on each tool call.

### Tuning

The detection rules are intentionally simple to keep the surface conservative. As the operator encounters false positives (cues that surface where the methodology does not apply) or false negatives (situations where the cue should have fired but did not), adjust the regex patterns in `lodestone-pretool-hook.sh` directly. The script is single-file and readable; tuning is local.

## Status

v1, reference implementation. Five detection rules. The hook is not under the public-canon discipline (it is tooling that delivers methodology into a workflow, not methodology content); the underlying protocols cited are Lodestone canonical sections.

Additional integrations (shell wrappers, IDE plugins, MCP servers, CI hooks) are out of scope for v1. The composition pattern with cma's reference integrations provides the template for any future ones.
