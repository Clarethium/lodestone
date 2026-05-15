# Preface

Working with AI systems is a practice. Lodestone specifies the practice.

This document is a reference, not a tutorial. It defines the components of disciplined work with AI systems: the stance, the loop, the calibration, the altitude, the failure shapes, the quality levels, the surface protocols, and the compound practice. It does not teach how to use specific AI tools, nor does it predict which models will be capable next quarter. It addresses operator discipline: the meta-skills that hold across model generations more than they depend on any specific model's capability. Some specific failure shapes in Section V are more time-bound, but the underlying disciplines are not.

A forward-looking annex on collective practice extends the discipline across operators. The annex is provisional: its claims are reasoned designs awaiting validation by multi-operator pilot, not validated practice. It is held separately so the canonical sections preserve their authority.

## Who this is for

The audience is senior operators: people whose work with AI systems is shaped through repeated exchange with the model, and whose output quality depends on the discipline they bring to that exchange. Engineers, researchers, designers, writers, analysts. The work is recognizable. Each unit of output develops over many turns with the model; the model is capable and the work is non-trivial; output quality emerges from both the model's capability and the discipline the operator brings to the loop.

This document does not address operator skill at the level of "how to write a prompt." It addresses operator skill at the level of how to remain coherent across long sessions, how to detect when work is drifting before it fails, and how to make each piece of work compound on prior learning.

If you are new to working with AI, this is not the place to start. If you have worked with AI long enough to recognize the failure shapes named in Section V, much of what this document names will already be familiar; the document gives the practice an explicit vocabulary.

## How to read this

The document can be read in order or used as a reference. Read in order, it builds: stance precedes the loop; the loop precedes calibration; calibration precedes altitude; altitude precedes the catalog of failure shapes; the catalog precedes the quality levels; the quality levels precede the surface protocols; the surface protocols precede the compound practice that turns each session's work into next session's signal.

Used as a reference, each section is independent. The Glossary lists every load-bearing term in one place; cross-references throughout the document point to the section that treats each term in depth.

This is a working reference. Where the document specifies, the wording is intentional and rewards careful reading. Where it leaves room for adaptation to specific contexts, tools, or projects, it does so explicitly.

Specific numbers in the methodology (three similar features for Pattern Study, five files for the five-file rule, three to five turns for the altitude-check cadence, ten failure shapes) are heuristic anchors based on practice rather than optimized parameters; reasonable variation does not break the rule.

## The body it sits in

Lodestone is one of two open reference artifacts published by Clarethium:

- **[Touchstone](https://github.com/Clarethium/touchstone)** validates work against quality standards.
- **Lodestone** orients practice.

[cma](https://github.com/Clarethium/cma) is the executable companion. cma runs the compound practice loop on the operator's local machine, capturing failures and surfacing relevant context as the operator works. The methodology lives in Lodestone; the running implementation lives in cma.

These artifacts are designed to compose. They can also be used independently. An operator can read Lodestone without running cma, or run cma without reading Lodestone in detail. They reinforce each other when used together.

## What this is not

Lodestone is not a curriculum. It does not progress the operator from beginner to advanced; it specifies a practice that a skilled operator can adopt and refine.

Lodestone is not a manifesto. It does not claim that AI changes everything, or that the practices specified here are universal. It specifies a practice that, in the author's work, has produced better work; whether that practice generalizes more broadly is an empirical question.

The document's specificity and abstraction are both intentional: specific where the rules hold across operators, abstract where adaptation is the right move.

Lodestone is not a comprehensive treatment of the methodological tradition it draws on. The Influences section names the works that informed this document's structure and vocabulary; engagement with each is provisional and will deepen in subsequent versions.
