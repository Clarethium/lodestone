# Glossary

Vocabulary used throughout this work. Each entry is a load-bearing term that recurs across sections. Definitions are tight; sections that treat each term in depth populate as the manuscript develops.

## The Loop and its steps

**The Loop.** The five-step cycle that governs disciplined work: understand the system and the task, build the part, verify it works, record what was learned, declare done. Each step has a stop condition; skipping a step loads risk into a later one.

**Understand.** First loop step. Read the actual code, trace the user journey, find similar features, map integration points. Stops when the system is grasped, not when the task feels familiar.

**Build.** Second loop step. Implement the work, matching established patterns and naming.

**Verify.** Third loop step. Confirm the work behaves correctly across the dimensions that matter, not only the happy path. Verification at one level is not coverage of all levels.

**Record.** Fourth loop step. Capture decisions, failures, and rejected alternatives so future work compounds on this one. Without recording, learning leaks.

**Done.** Fifth loop step. Declared only when the work would survive a fresh-eyes test and the verification gaps are explicit.

## Frame and stance

**Frame.** The shape of the problem as currently seen: which questions are being asked, which are not, what counts as evidence. Frames are often invisible to the operator inside them.

**Frame-awareness.** The discipline of noticing the frame in operation, including the basin it pulls toward. The foundational entry to disciplined operator-AI work.

**Operator.** The person whose judgment shapes work continuously through a loop with an AI system. The locus of practice; the methodology serves operator skill, not AI capability.

## Calibration

**Calibration.** Matching stance to actual conditions. Wrong stance applied to right conditions, or right stance to wrong conditions, both fail. The prerequisite for everything else.

**Search uncertainty.** A class of uncertainty where the answer exists and must be found. Calls for directed exploration and systematic verification.

**Generate uncertainty.** A class of uncertainty where the answer is being constructed. Calls for open exploration, multiple drafts, permission to be wrong.

## Altitude

**Altitude.** The level at which reasoning currently operates. Long reasoning drifts toward detail; periodic altitude checks restore breadth. Four levels: meta, system, component, detail.

**Meta altitude.** Reasoning about why the work matters and what the real problem is.

**System altitude.** Reasoning about how the components connect and what is affected.

**Component altitude.** Reasoning about how a single piece works.

**Detail altitude.** Reasoning about exact implementation.

## Quality levels

**Functional.** Code runs, handles the happy path, is basically correct. The minimum bar.

**Complete.** All user flows work, error states handled, integration points connected. Passes the fresh-eyes test.

**Polished.** Performance acceptable, accessibility checked, edge cases covered. Passes the self-review checklist.

**Exceptional.** Reaches territory the default implementation cannot. Reserved for critical or visible features where the specific context opens something the generic version cannot reach.

## Failure shapes

See [Section V](05-failure-shapes.md) for the canonical concept and detection signature for each shape.

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

**Fresh eyes test.** Approaching the work as if encountering it for the first time: find the feature via UI only, complete the workflow end-to-end, check for errors. The test that says ready or not.

**Specificity test.** A test for whether output reaches past the default. If the work could exist identically in a generic context, it has not yet reached the territory the specific context opens.

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
