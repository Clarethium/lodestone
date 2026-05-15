# Lodestone

Operator methodology for working with AI systems.

## What this is

Lodestone names the practice that keeps work true to its frame. It is one of two open reference artifacts published by Clarethium:

- **Touchstone** validates work against quality standards.
- **Lodestone** orients practice.

Lodestone defines the components of disciplined work with AI systems: the stance, the loop, the calibration, the altitude, the failure shapes, the quality levels, the surface protocols, and the compound practice.

This is a reference, not a tutorial. Read it as you would read a field manual or a published standard. The audience is operators ready to adopt the practice.

## Who this is for

Senior operators whose work develops continuously through a loop with AI. The quality of that loop determines the quality of the output. Engineers, researchers, designers, writers, analysts.

## Structure

See [OUTLINE.md](OUTLINE.md) for the manuscript table of contents.

A forward-looking annex on [collective practice](forward-looking/01-collective-practice.md) extends Lodestone's discipline into territory not yet validated by multi-operator pilot. The annex is provisional, held separately from the canonical sections, and evolves at its own pace as pilot evidence accumulates.

## Tools

A reference Claude Code `PreToolUse` hook that surfaces Lodestone protocols at the moment of action is in [tools/](tools/). It detects action patterns matching Lodestone concepts (authentication surface, database surface, git write operations, deletion, Pattern Study triggers) and surfaces the relevant protocol guidance to the assistant's context. Composes with [cma](https://github.com/Clarethium/cma)'s reference hook: cma surfaces past captures, the Lodestone hook surfaces methodology protocols. See [tools/README.md](tools/README.md) for installation and detection rules.

## Companions

Lodestone composes with the other open Clarethium artifacts:

- **[Touchstone](https://github.com/Clarethium/touchstone)**: third-person measurement of AI outputs. The substrate that pairs with Lodestone's first-person operator discipline.
- **[cma](https://github.com/Clarethium/cma)**: executable compound-practice loop. The terminal-side instantiation of Lodestone's Section VIII.

The methodology lives in Lodestone. cma is what running that methodology looks like in a terminal.

## License

CC-BY 4.0. See [LICENSE](LICENSE).

## Author

L. Lucic. Published under Clarethium.
