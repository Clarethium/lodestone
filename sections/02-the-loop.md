# II. The Loop

The Loop is the cycle that governs disciplined work: understand the system and the task, build the part, verify it works, record what was learned, declare done. Each step has a stop condition. Each step has typical ways to fail. Skipping a step does not save time; it loads risk into a later step that has to absorb the gap.

The Loop is not unique to AI work. It is the discipline of any craft where the work develops through cycles. What changes in AI work is how often the cycle runs (many times per session, sometimes per minute) and how easy it becomes to skip steps when model output arrives quickly. The Loop is the structural defense against the failure shapes *Speed over understanding* and *Happy path only* (Section V).

## Understand

The first step is to grasp the system and the task. Read the actual code in the area being changed. Trace the user journey when the work is user-facing. Find similar features that already exist. Map the integration points the work will touch.

The step is complete when the operator can describe, without consulting the AI: what the system does in the relevant area, what calls and depends on the area being changed, where the code that implements similar features lives, and what the task adds to or modifies in that picture.

The typical failure of this step is to declare it complete when the task feels familiar, rather than when the system is grasped. Familiarity is not understanding. The cost of advancing without understanding is paid in the Build and Verify steps as rework, and again in production as integration failures.

## Build

The second step is to implement the work, matching the established patterns and naming. Build is often started prematurely, because it is the step that produces visible output.

The step is complete when the implementation is in place, the work compiles or runs in the local context, and the implementation matches the style and conventions of the surrounding code.

The typical failure of this step is to advance to Verify before the implementation matches the surrounding patterns. The result is code that works locally, drifts from the system's voice, and creates inconsistency that compounds across future changes.

## Verify

The third step is to confirm the work behaves correctly across the dimensions that matter. Verification is plural, not singular: a piece of work has multiple kinds of correctness (functional, integration, performance, accessibility), and verification at one level does not establish coverage of the others.

The step is complete when the operator can name what was verified and what was not. "Verified: X. Not verified: Y." The not-verified statement is mandatory; an empty not-verified is itself a claim that requires justification.

The typical failure of this step is to verify the happy path and treat that as proof. Functional correctness is a kind of verification, not all of verification. The catalog of failure shapes (Section V) names this as *Happy path only*.

## Record

The fourth step is to capture what was learned. Capture decisions made during the work. Capture the alternatives that were considered and ruled out. Capture failures encountered. Capture the surprising patterns or constraints that shaped the work.

This is the step most often skipped. Recording does not produce visible output for the current task; the operator's attention is already moving to the next task. Without recording, learning leaks.

Record is the link to compound practice. Every recorded miss is a candidate for surfacing the next time conditions match. Every recorded decision is a candidate for re-application or reconsideration. Every recorded rejection is a barrier against silently rebuilding what was deliberately not built. The Compound Practice section (Section VIII) describes the mechanism; the discipline of using it begins here, at the Record step of every Loop.

The typical failure of this step is to skip it because the work feels complete after Verify. The cost of skipping is paid not in this Loop but in the next one, when the same failure recurs because nothing was captured to prevent it.

## Done

The fifth step is to declare completion. Done is not a state the work enters automatically when Verify passes; it is a deliberate claim the operator makes. Stated equals done.

Done is valid when the work would survive a fresh-eyes test (Section VII), when the verification gaps are explicit, and when the recording step has been completed. Without those three conditions, "done" is a claim that has not been earned.

The typical failure of this step is to declare done after Verify and before Record, leaving the compound practice loop incomplete. The work appears finished. The operator moves to the next task. The lesson the work could have produced is lost.
