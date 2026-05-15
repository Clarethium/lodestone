# Lodestone specimens

A specimen is the abstracted form of a captured failure. It carries the failure's shape with operator-specific detail removed.

## What a specimen contains

Per Lodestone's [forward-looking annex on collective practice](../forward-looking/01-collective-practice.md), a specimen preserves:

- The failure mode it instantiates (which Lodestone failure shape).
- The surface where it occurred.
- The structural pattern of how the failure formed.
- The prevention that would have caught it earlier.

A specimen removes:

- Operator filesystem paths.
- Operator project names and identifiers.
- Operator identity.

## What this directory is

Lodestone-published specimens, structured for recognition-library use. Each specimen instantiates one failure shape in a form that lets an external reader recognize the pattern in their own work.

The directory seeds the recognition library that Lodestone's lineage calls for: Klein's recognition-primed decision pattern (Section V) requires a library of recognized shapes to function. The catalog of failure shapes names the cues; specimens give them concrete form.

Future specimens may be contributed by operators running compound practice; the format below is the contribution shape.

## Specimen format

Each specimen lives in its own file: `specimens/<id>.md`. The filename ID is short, kebab-case, stable for citation.

```
---
id: <kebab-case-id>
failure_shape: <name (Section reference)>
surface: <surface tag>
model_context: <model-era description>
status: illustrative | abstracted-from-capture | curated | canonical
---

# <Short title>

## Cue

The recognizable signal at the moment of action.

## Situation (abstracted)

The structural pattern of how the failure formed. Removes operator-specific detail.

## What was about to happen

The action that recognition would interrupt.

## Recovery

What is done instead, once the shape is recognized.

## Prevention

What would have caught the failure earlier, before it formed.

## What this specimen does not preserve

The operator-specific detail removed in abstraction.
```

See [TEMPLATE.md](TEMPLATE.md) for the empty scaffold.

## Status tiers

Drawn from the curation framework in the forward-looking annex:

- **illustrative**: written for teaching, not derived from a captured incident. Marked clearly so readers can calibrate. The v1 corpus starts here.
- **abstracted-from-capture**: derived from an actual `cma` capture, redacted to specimen form.
- **curated**: reviewed and confirmed well-written, sufficiently sanitized, useful as reference.
- **canonical**: promoted through sustained curation; serves as a definitional teaching case.

## Contribution

Specimens contributed by operators running cma capture-and-redact:

1. Take a cma miss with texture (intended, corrected, excerpt fields populated; see [cma DATA.md](https://github.com/Clarethium/cma/blob/main/DATA.md)).
2. Abstract: remove paths, project names, identities. Keep the structural shape.
3. Cast in the specimen format above. Use [TEMPLATE.md](TEMPLATE.md) as a starting point.
4. Status: `abstracted-from-capture`.

Curated and canonical promotion is editorial review, not part of the contribution flow.

## Status of the v1 corpus

One illustrative specimen ships as format reference. Real abstracted-from-capture specimens are expected to follow as the corpus grows. The illustrative tier exists so the format is anchored before captured material is published.
