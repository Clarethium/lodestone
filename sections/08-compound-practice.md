# VIII. Compound Practice

The Record step of the Loop (Section II) captures what the operator has learned. Compound practice is what those captures do next: surface relevant learning at the moment of future action, catch repeating failures before they happen, and accumulate evidence that the loop is closing. Without surfacing, recording produces an archive that tends to remain unread. With surfacing, the archive becomes a living instrument that catches repeats before they happen.

Compound practice draws on K. Anders Ericsson's deliberate-practice framework, shaped to the operator-AI loop. Like deliberate practice in other crafts, it is structured around feedback, oriented toward identified weaknesses (the captured misses), and instrumented for whether the practice produces improvement (recurrence detection and prevention captures, described below). Ericsson's deliberate practice is canonically coach-mediated: a teacher observes the practitioner, identifies the next weakness to address, and designs the corrective exercise. Compound practice automates one specific coaching function: the timely return of relevant past observations at the moment of action. Observation, weakness identification, and how to act on a surfaced warning remain the operator's responsibility. What distinguishes compound practice from simple journaling is this surfacing layer: captures return at the moment future actions match their context, turning the archive into an active instrument rather than a passive record.

The mechanism is described in this section. The implementation is cma (the executable companion to Lodestone), specified in its own repository. This section addresses what compound practice is and what it requires; the running implementation addresses how it is captured, indexed, and surfaced on the operator's machine.

## What gets captured

Compound practice records four kinds of material:

**Misses.** Failures that occurred. A miss is a specific case where the work fell short of what it intended. Recording a miss preserves the texture of the failure: what the operator was about to do, what they did instead after correction, the conditions that produced the drift. Misses are particularly valuable because they reveal where the operator's discipline is currently weakest.

**Decisions.** Architectural and strategic choices made during the work. A decision is recorded with its rationale and the alternatives considered. Decisions are easily lost to time: without them, the operator returns to a system months later and cannot reconstruct why it is shaped the way it is.

**Rejections.** Options considered and ruled out. A rejection is recorded with the reason for elimination and the conditions that would warrant revisiting. Rejections survive context compaction in long sessions and prevent the operator from silently rebuilding what was deliberately not built.

**Preventions.** Catches where a surfaced warning prevented a recurrence. A prevention is the evidence that compound learning is more than a claim. Without prevention captures, the loop is open: warnings surface but their effect on operator behavior is unverified.

The four together compose compound practice's captures. Misses are what failed. Decisions are what was chosen. Rejections are what was eliminated. Preventions are what was caught.

## Surfacing at the moment of action

A capture is only useful if it returns to influence future work. Surfacing is the mechanism that makes captures relevant when relevant.

The principle: a capture surfaces when its context matches the current operator action. A miss recorded last week surfaces when an action today touches the same surface, the same files, or the same kind of work. A decision surfaces when a current action falls within its applicability. A rejection surfaces when the rejected option becomes tempting again.

The timing is load-bearing. Surfacing at session start dumps all warnings into early context, where they are visible but easy to forget by the time they would matter. Surfacing at the moment of relevant action delivers the warning where it can change behavior. The latter is harder to implement and more useful when implemented; surfacing infrastructure should aim for moment-of-action delivery.

The signals that a capture is relevant: surface match, file match, keyword overlap with the current work, and (when texture has been preserved) the situational similarity between the prior context and the current one.

## The compound loop

The compound loop is the cycle that turns recorded captures into prevented failures and accumulated learning:

1. **Capture.** A failure, decision, rejection, or prevention is recorded at the moment it occurs. The discipline of capturing is the Record step of the Loop.
2. **Surface.** When a future action's context matches a prior capture, the capture surfaces in view. Surfacing is automatic; the operator does not need to remember to look.
3. **Catch.** The surfaced capture changes the operator's action: a planned step is reconsidered, a different approach is taken, a verification is added. The catch is where the loop closes.
4. **Record prevention.** The catch is itself recorded as a prevention, linked to the original capture. The prevention is evidence that the warning was effective.
5. **Strengthen.** The prevention reinforces the warning's weight. Captures with proven prevention effect rise in surfacing priority. Captures that surface but never produce preventions decline; either the capture is no longer relevant, or the warning text is not landing.

Each iteration strengthens the next. After enough iterations, a class of failure that once recurred regularly can stop recurring. The operator notices this not by reading captures but by the absence of the failure in current work.

## Recurrence and decision lifecycle

Two derived signals from the compound loop matter for operator practice. The first, recurrence detection, pairs with prevention captures as the loop's dual evidence channels: prevention captures show what was caught, recurrence shows what was missed. Together they close the question of whether captured learning is reaching the operator's behavior.

**Recurrence detection.** When a failure pattern repeats across captures, the system flags the recurrence. The flag is not a punishment; it is information. Recurrence indicates that the prevention currently in place is not working. The recovery is to sharpen the prevention: rewrite the warning text, change when it surfaces, change which actions trigger it, or retire it as ineffective and record a different prevention attempt.

**Decision lifecycle.** Decisions captured early in a project are referenced or contradicted by later decisions. A decision that goes unreferenced for an extended period is a candidate for archival. A decision that is contradicted by later work without explicit acknowledgment is a candidate for review. Tracking decisions through their lifecycle keeps the project's reasoning record current and prevents silent drift.

Both signals require the captures to be properly indexed and the surfacing layer to be operating. Both are absent from a system that records but does not surface.

## Where cma fits

Compound practice is a discipline. cma is the implementation of that discipline as an executable on the operator's machine.

The split is intentional. The discipline is canonical: the four capture types, the surfacing principle, the compound loop, the recurrence and decision-lifecycle signals. These are described in this section as the methodology that any compound-practice tool should implement.

cma's seven primitives map to the discipline. Four are capture verbs (`cma miss`, `cma decision`, `cma reject`, `cma prevented`). The remaining three handle operations: `cma surface` brings prior captures into view; `cma distill` promotes accumulated patterns to permanent surfacing; `cma stats` provides the evidence dashboard, including recurrence and prevention rates.

The full design is specified in the [cma repository](https://github.com/Clarethium/cma). Operators who run cma have a personal compound-practice instance on their machine. The captured data is private; the discipline is shared.

The methodology in this document does not require cma. An operator can practice compound capture without any specific tool, by writing captures into a structured journal and rereading them when context matches. cma exists because the surfacing-at-moment-of-action discipline is hard to maintain manually; the executable removes that overhead. But the discipline is what matters; the tool serves the discipline.
