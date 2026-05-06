# Glossary

Vocabulary used throughout this work. Each entry is a load-bearing term that recurs across sections. Definitions are tight; cross-references throughout the document point to the section that treats each term in depth.

## The Loop and its steps

**The Loop.** The five-step cycle that governs disciplined work: understand the system and the task, build the part, verify it works, record what was learned, declare done. Each step has a stop condition; skipping a step loads risk into a later one.

**Understand.** First loop step. Read the actual code, trace the user journey, find similar features, map integration points. Stops when the system is grasped, not when the task feels familiar.

**Build.** Second loop step. Implement the work, matching established patterns and naming.

**Verify.** Third loop step. Confirm the work behaves correctly across the dimensions that matter, not only the happy path. Verification at one level is not coverage of all levels.

**Record.** Fourth loop step. Capture decisions, failures, and rejected alternatives so future work compounds on this one. Without recording, learning leaks.

**Done.** Fifth loop step. Declared only when the work would survive a fresh-eyes test and the verification gaps are explicit.

## Frame and stance

**Frame.** The shape of the problem as currently seen: which questions are being asked, which are not, what counts as evidence. Frames are often invisible to the operator inside them.

**Operator.** The person whose judgment shapes work continuously through a loop with an AI system. The locus of practice; the methodology serves operator skill, not AI capability.

**Stance.** The operator's disposition toward AI work, prior to any specific task. Composed of four directives (see Directives below). Stance is prior to method and prior to tactic.

**Integrity principle.** The principle that claims and reality must match. Three formulations: stated equals done, scope committed equals scope completed, quality claimed equals quality demonstrated. A precondition for the rest of the methodology to work.

## Directives

The four directives that compose the operator stance. See [Section I](01-stance.md) for the full treatment of each.

**Evidence over assumption.** Claims about a system require evidence from the system; AI output is hypothesis, not evidence.

**Systems over tasks.** Tasks happen within systems; treating tasks as isolated produces components that fail in integration.

**Patterns over invention.** When uniform patterns exist, follow them; new patterns are justified explicitly, not invented quietly.

**Prevention over detection.** Prevent failures by understanding root causes; prevention scales, detection only catches what has happened before.

## Calibration

**Calibration.** Matching stance to actual conditions. Wrong stance applied to right conditions, or right stance to wrong conditions, both fail. The prerequisite for the rest of the methodology to do useful work.

**Search uncertainty.** A class of uncertainty where the answer exists and must be found. Calls for directed exploration and systematic verification.

**Generate uncertainty.** A class of uncertainty where the answer is being constructed. Calls for open exploration, multiple drafts, permission to be wrong.

**Frame-stuck.** The state in which multiple approaches keep failing the same way because the framing of the problem is itself wrong, not because of wrong stance. Recovered by saturation and return.

## Altitude

**Altitude.** The level at which reasoning currently operates. Long reasoning drifts toward detail; periodic altitude checks restore breadth. Four levels: meta, system, component, detail.

**Meta altitude.** Reasoning about why the work matters and what the real problem is.

**System altitude.** Reasoning about how the components connect and what is affected.

**Component altitude.** Reasoning about how a single piece works.

**Detail altitude.** Reasoning about exact implementation.

**Altitude check.** Periodic action of asking: at what altitude am I currently operating? Is that the altitude this work needs? Triggered on cadence (every three to five substantive responses) or on entropy signals.

**Entropy signals.** Observable conditions that reasoning has drifted: long response without goal reference, three or more iterations on the same narrow problem, a fix that removes the error without addressing the defect, a context switch, an "almost done" feeling without a fresh-eyes pass. Trigger an altitude check immediately.

## Quality levels

**Functional.** Code runs, handles the happy path, is basically correct. The minimum bar.

**Complete.** All user flows work, error states handled, integration points connected. Passes the fresh-eyes test.

**Polished.** Performance acceptable, accessibility checked, edge cases covered. Passes the self-review checklist.

**Exceptional.** Reaches territory the default implementation cannot. Reserved for critical or visible features where the specific context opens something the generic version cannot reach.

## Failure shapes

See [Section V](05-failure-shapes.md) for the canonical concept, detection signature, prevention pattern, and recovery move for each shape.

**Speed over understanding.** Starting work before grasping the system or the defect.

**Component over journey.** Treating a feature as the isolated component that implements it, missing the discovery and navigation that make it findable.

**Happy path only.** Verifying one kind of behavior and treating it as coverage of all behaviors.

**Invention over replication.** Creating a new pattern when uniform established ones exist.

**Deletion without understanding.** Removing code that looks unused without verifying why it exists.

**Assumption over verification.** Claiming how a system behaves without reading the actual source or output.

**Tunnel vision.** Pursuing the same approach despite repeated failures.

**Scope abandonment.** Committing to a scope, completing part, going silent, moving to a new topic.

**Quality theater.** Claiming exceptional quality without showing evidence.

**Basin capture.** Settling for the first viable approach without exploring what the specific context makes possible.

## Practices and gates

**Pattern Study.** The practice of finding three similar features in a codebase and reading their complete implementations before writing new code. Defense against invention over replication.

**Five-file rule.** User-facing features modify at least five files (data, API, page, navigation types, navigation UI). Touching only one or two files signals missing integration.

**Fresh-eyes test.** Approaching the work as if encountering it for the first time: find the feature via UI only, complete the workflow end-to-end, check for errors. The test that says ready or not.

**Specificity test.** A test for whether output reaches past the default. Multiple specificity tests apply (see Section VI); the most diagnostic asks whether user data shapes the work or merely fills a template.

**Saturation and return.** A move when frame-stuck. Leave the failing frame entirely, saturate in an unrelated domain, return with fresh framing.

## Compound practice

**Compound practice.** The discipline of capturing failures, surfacing relevant context at the moment of action, and tracking patterns across sessions so each piece of work builds on prior learning.

**The compound loop.** The cycle: capture failures, surface relevant context at the moment of action, catch the repeat, record the prevention. Each iteration strengthens the next.

**Surfacing.** Bringing a prior capture into view when its context matches the current work. A miss recorded last week surfaces when an action today matches the conditions under which it was recorded.

**Recurrence.** When a failure pattern repeats across captures. Recurrence indicates the prevention is not working and the relevant rule or warning needs sharpening.

## Captures

**Miss.** A captured failure: a specific case where the work fell short of what it intended. Recorded with the texture of the failure preserved (the conversation excerpt, the intended action, the corrected action).

**Decision.** A captured architectural or strategic choice. Recorded with the rationale and the alternatives considered.

**Rejection.** A captured elimination: an option considered and ruled out, with the reason. Survives session compaction so the elimination is not silently rebuilt.

**Prevention.** A captured catch: a moment where a surfaced warning actually prevented a recurrence. Without prevention captures, compound learning is a claim; with them, it is evidence.
