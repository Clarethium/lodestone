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

Reference integrations that deliver pieces of the methodology into an operator's workflow are in [tools/](tools/):

- A Claude Code `PreToolUse` hook that surfaces Lodestone protocols at the moment of action (authentication surface, database surface, git write operations, deletion, Pattern Study triggers). Composes with [cma](https://github.com/Clarethium/cma)'s reference hook.
- A cross-reference document mapping Lodestone concepts (Verified/Not verified, Quality theater, Assumption over verification, Default implementation) to [Touchstone](https://github.com/Clarethium/touchstone) measurement layers, with runnable examples.

See [tools/README.md](tools/README.md) for installation and details.

## Specimens

[specimens/](specimens/) seeds the recognition library that Klein's RPD lineage (Section V) calls for. Each specimen instantiates one failure shape in a form that lets an external reader recognize the pattern in their own work. The v1 corpus starts with one illustrative specimen as format anchor; abstracted-from-capture specimens contributed by operators running cma are the intended growth path. See [specimens/README.md](specimens/README.md) for format and contribution shape.

## Companions

Lodestone composes with the other open Clarethium artifacts:

- **[Touchstone](https://github.com/Clarethium/touchstone)**: third-person measurement of AI outputs. The substrate that pairs with Lodestone's first-person operator discipline.
- **[cma](https://github.com/Clarethium/cma)**: executable compound-practice loop. The terminal-side instantiation of Lodestone's Section VIII.

The methodology lives in Lodestone. cma is what running that methodology looks like in a terminal.

## License

CC-BY 4.0. See [LICENSE](LICENSE).

## Author

L. Lucic. Published under Clarethium.
