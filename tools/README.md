# Lodestone tools

Lodestone-aware integrations that deliver pieces of the methodology into an operator's workflow.

These are reference implementations, not the methodology itself. The methodology lives in the canonical sections; the tools here either surface protocols at the moment of action or document how Lodestone concepts map to existing measurement substrates.

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

### `lodestone-via-touchstone.md`

A cross-reference document mapping Lodestone methodology concepts to [Touchstone](https://github.com/Clarethium/touchstone) measurement layers. Where a Lodestone concept can be operationalized via Touchstone (Verified/Not verified, Quality theater, Assumption over verification, Default implementation), the mapping is named with a runnable example using `clarethium_touchstone`'s Python API.

Concepts that describe operator behavior rather than output structure (the stance directives, altitude, calibration, most failure shapes) are not directly measurable through Touchstone; the document names the limit honestly.

### `lodestone-score.py`

A runnable CLI that takes a work file and a source file, calls `clarethium_touchstone.measure()`, and formats the result as a Lodestone score report covering the four operationalized concepts from `lodestone-via-touchstone.md`. Each concept gets its measurement, a threshold check, and a status (within threshold or concern).

```bash
python3 tools/lodestone-score.py --work path/to/work.txt --source path/to/source.txt
```

Exit codes: `0` if all measurable concepts are within thresholds; `1` if at least one concern threshold tripped (useful in CI); `2` on error (file not found, Touchstone not installed, measurement raised).

Thresholds are tunable per invocation (`--projected-threshold`, `--gap-threshold`, `--unsourced-threshold`). Defaults are heuristic; refine to context.

Requires `clarethium_touchstone`. The script prints install instructions if the import fails.

## Status

v1 reference implementations. Five detection rules in the hook; four operationalized concept mappings in the Touchstone cross-reference; one runnable scoring CLI on top of the mapping. The tools deliver methodology into workflows or measurement substrates, not methodology content; the underlying protocols cited are Lodestone canonical sections.

Additional integrations (shell wrappers, IDE plugins, MCP servers, CI hooks, JSON output mode for `lodestone-score`) are out of scope for v1. The composition pattern with cma's reference integrations and the Touchstone API surface provide the templates for future ones.
