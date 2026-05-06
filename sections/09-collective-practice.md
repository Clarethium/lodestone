# IX. Collective Practice

Compound practice (Section VIII) keeps the operator's captures private and surfaces them against the operator's own future actions. Collective practice extends the discipline across operators: failures observed by one operator can prevent failures in operators who never observed them. The mechanism is a shared corpus of abstracted failure specimens, contributed deliberately by participating operators and consumed alongside their own captures.

This section addresses what collective practice is and what it requires. The implementation is specified separately as the cma corpus protocol, which defines the wire format, the redaction pipeline, and the governance rules. The methodology does not require any specific corpus to exist; it specifies the discipline that any cross-operator compound-practice corpus should embody.

## What gets contributed

Collective practice records two kinds of material derived from individual captures:

**Specimens.** A specimen is the abstracted form of a miss. The operator's local miss carries paths, code, and project-identifying detail; a specimen carries the failure's shape with that detail removed. The shape preserves: the failure mode it instantiates, the surface where it occurred, the structural pattern of how the failure formed, and the prevention that would have caught it. The shape removes: the operator's filesystem, the operator's project, the operator's identity.

A specimen is useful to other operators because failure shapes generalize. The operator who wrote into the wrong tree because a familiar path felt safe is the same shape as the operator who reused a stale config because a familiar value felt safe. The specific paths and configs are local; the shape is shared.

**Narratives.** A narrative is a longer, sanitized account of a specimen's circumstances, written deliberately by the operator and reviewed for identifying detail. Narratives are the textbook material of collective practice: cited in operator manuals, discussed in operator training, used to construct evaluation cases. Specimens carry pattern; narratives carry texture.

Narratives are optional. A specimen without a narrative is still useful for matching and cross-operator surfacing; it cannot be quoted in canonical reference work.

## What gets consumed

A participating operator pulls specimens from the corpus into their local surfacing layer. A pulled specimen is treated by the surfacing mechanism (Section VIII) the same way as a local miss, with one addition: the source is marked. The operator sees that the warning derives from another operator's specimen, and how many corroborating signatures exist. Both signals modulate trust: a specimen with many corroborating signatures describes a near-universal failure shape; a specimen with one describes a pattern that may be local.

Consumption is filtered. An operator pulls specimens by surface and failure mode relevant to their work, not the entire corpus. The local mirror is incremental and small.

## The collective loop

The collective loop extends the compound loop (Section VIII) with cross-operator steps:

1. **Capture and contribute.** The operator captures a miss locally as in Section VIII. When the operator chooses to share, the miss is abstracted into a specimen, reviewed by the operator, and submitted to the corpus.
2. **Aggregate.** The corpus collects signatures from many operators. Identical or near-identical patterns reinforce each other; rare patterns remain visible but flagged as singular.
3. **Distribute.** Operators pull relevant specimens into their local surfacing layer.
4. **Surface and catch.** A pulled specimen surfaces when its context matches a current action, the same way local misses surface. The catch is the operator's behavior changing due to a warning derived from another operator's failure.
5. **Record the crossing.** The catch is recorded as a crossing: a prevention attributed to a non-self specimen. Crossings are the evidence that collective practice is more than a claim.

A crossing is to collective practice what a prevention is to individual compound practice. Without crossings, the corpus is a published archive that no one acts on. With crossings, the archive prevents work the operator never observed in their own practice.

## Privacy as discipline

Contribution raises a discipline question: what protects the operator's privacy, and what protects the corpus's integrity? The discipline answers in three commitments:

**Layer separation.** The operator's local captures are private and remain private. Specimens are derived artifacts, structurally separate from the records they were derived from. No tool transmits a local capture without the operator approving the abstracted form.

**Operator review at the boundary.** Submission is never automatic. The operator sees the original record and the proposed specimen side by side and decides whether the abstraction is sufficient. Submission timing is the operator's choice; capture and submission are decoupled.

**Non-destructive retraction.** An operator who later regrets a submission can mark the specimen retracted. The retraction is signed and visible; the specimen remains citable with the retraction notice attached. Citations always resolve; the corpus does not silently lose specimens.

These commitments hold whether or not any particular implementation enforces them. An implementation that bypasses operator review or transmits raw captures violates the discipline regardless of whether the data flow is technically permitted.

## Forks and the absence of a single canonical corpus

The discipline does not depend on a single canonical corpus existing. Multiple corpora can run the same protocol; specimens from one corpus can be cited and consumed independently of any other. The operator chooses which corpora to participate in based on their fit for the operator's domain, governance preferences, and trust assumptions.

A reference corpus is useful for citation and curriculum because it is shared. It is not useful as a single point of authority. The discipline treats canonical status as earned through curation quality and contribution depth, not as a structural privilege of any one operator group.

## Aging

Failure shapes are time-bound to the systems they were observed against. A specimen captured against one generation of model may be irrelevant against a later generation whose failure surface has shifted. The discipline includes aging as a normal part of the corpus's life: specimens are timestamped against their model context, deprecated when their underlying behavior no longer recurs, and recurrent specimens are re-confirmed against current model generations periodically.

An aged-out specimen is not deleted; it is marked as historical. Citations resolve; surfacing weight drops. The corpus retains its archival function without polluting current surfacing.

## Where the corpus protocol fits

Collective practice is a discipline. The cma corpus protocol is the implementation of that discipline as a wire format, a redaction pipeline, and a set of governance rules.

The split is intentional. The discipline is canonical: the two contribution kinds, the operator-review boundary, the cross-operator surfacing principle, the crossing as evidence, the retraction and aging mechanisms. These are described in this section as the methodology that any cross-operator compound-practice corpus should implement.

The cma corpus protocol specifies the concrete realization: cryptographic identity, namespaced specimen IDs, the editorial board's role in curating canonical specimens, schema versioning rules. Operators who participate in a cma-protocol corpus run the discipline in a specific instantiation. The methodology in this document does not require the cma protocol; an operator group can run collective practice with any implementation that holds the commitments named above.

The discipline is what matters; the protocol serves the discipline.
