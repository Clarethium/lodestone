# Lodestone via Touchstone

Cross-reference between Lodestone methodology concepts and [Touchstone](https://github.com/Clarethium/touchstone) measurement layers. Where a Lodestone concept can be operationalized via Touchstone, this document names the mapping with a runnable example.

Touchstone is the measurement substrate. The Touchstone Standard specifies eleven measurement layers for output profiling; ten are deterministic (regex, structural analysis, string search, arithmetic) and one (Layer 1a, optional) generates baseline documents via an LLM for comparison.

The mappings below work against the Python reference implementation (`clarethium-touchstone`). API examples use the v0.1 surface.

## Concept mappings

### Verified / Not verified — Section II, Verify step

The Verify step requires an explicit "Verified: X. Not verified: Y." statement. Touchstone's grounding-decomposition layer (Layer 11) provides the third-person measurement: each sentence is labeled Grounded (supported by the source), Framed (interpretive but not contradicted), or Projected (beyond what the source supports).

```python
from clarethium_touchstone import measure

result = measure(work_text, source=source_text)
gfp = result["grounding_decomposition"]["proportions"]
print(f"Grounded: {gfp['G']:.0%}, Framed: {gfp['F']:.0%}, Projected: {gfp['P']:.0%}")
print(f"Has projection: {result['grounding_decomposition']['has_projection']}")
```

A high Projected proportion is the measurement complement of an unfilled "Not verified" gap. A claim of Done with high Projected rate is "done" claimed without verification.

### Quality theater — Section V, failure shape

Quality theater claims exceptional quality without evidence. Touchstone's quality profile (Layer 10) measures the substance-versus-presentation gap.

```python
result = measure(work_text, source=source_text)
print(f"Substance index: {result['quality_profile']['substance_index']:.2f}")
print(f"Gap: {result['quality_profile']['gap']:.2f}")
```

A negative gap (substance exceeds presentation) is the desired signal. A positive gap is the measurement symptom of Quality theater: presentation runs ahead of substance.

The composite quality profile requires at least ten numbers in the text for the source-fidelity component to qualify; see the Touchstone README for the threshold conditions.

### Assumption over verification — Section V, failure shape

Assumption over verification makes claims about a system without specific evidence from the system. Touchstone's source matching (Layer 4) measures the unsourced-claim rate.

```python
result = measure(work_text, source=source_text)
print(f"Unsourced rate: {result['source_matching']['unsourced_rate']:.0%}")
```

The unsourced rate is the third-person complement of claims the operator made without citing evidence.

### Default implementation — Section VI, specificity tests

The default implementation is the output a competent operator would produce given the same brief without exploiting what the specific context makes possible. Touchstone's baseline-document generation (Layer 1a, optional) provides the comparator: an LLM generates baseline documents on the same topic for comparison against the actual work.

Layer 1a is the only Touchstone layer that calls an LLM, and it generates baselines, not scoring. The comparison itself is deterministic. See the Touchstone Standard for the Layer 1a API.

## What is not yet mapped

Several Lodestone concepts are not currently operationalizable via Touchstone:

- The four stance directives (Evidence over assumption, Systems over tasks, Patterns over invention, Prevention over detection) describe operator disposition rather than output properties.
- Altitude and the altitude check describe operator-process states rather than output properties.
- Calibration describes an operator meta-skill rather than an output property.
- Most failure shapes other than the three above (Tunnel vision, Speed over understanding, Component over journey, Invention over replication, Deletion without understanding, Scope abandonment, Basin capture) describe action patterns rather than output structure.

Touchstone measures AI outputs against sources. Concepts that describe operator behavior rather than output structure are not directly measurable through this substrate. The [cma](https://github.com/Clarethium/cma) capture-and-surface layer is the operationalization route for those concepts.

## Limits

Touchstone's measurement is third-person and source-grounded. It is most useful when the work has a clear source to compare against: a document being summarized, a codebase being analyzed, a brief being implemented. For freeform generative work without a source, several layers degrade in usefulness or do not apply.

The Lodestone-to-Touchstone mapping above is a v1 reading. As both projects evolve, the mappings will sharpen; specific Layer numbers and API surfaces may shift across Touchstone Standard versions. Refer to the Touchstone Standard text for the authoritative layer definitions.
