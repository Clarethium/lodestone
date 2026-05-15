# V. Failure Shapes

Failure shapes are recurring patterns by which disciplined work breaks down. Each shape names a specific way the work pulls into something that looks complete but is not. Naming the shapes makes them visible; visible shapes are easier to detect early and recover from cleanly.

The structure follows the recognition-primed decision pattern Gary Klein names in naturalistic decision research (*Sources of Power*, 1998): experts recognize a situation through its cues, and the typical action follows from recognition rather than from option comparison. The detection signature in each entry below is the cue that surfaces the shape; the prevention and recovery patterns are the typical actions recognition makes available. The catalog extends RPD to failure-shape recognition: where Klein's classic RPD examples engage situation cues that prompt execution, the failure shapes here engage cues that prompt protective action. Klein's own later work on pre-mortems ("Performing a Project Premortem," *Harvard Business Review*, 2007) operates in the same failure-recognition territory; the catalog is the operator's recognition library for shapes that signal trouble.

Ten shapes follow. Each entry has the concept, the detection signature, the prevention pattern, and the recovery move.

---

**Speed over understanding.** Starting work before grasping the system or the defect. Signature: code begins within minutes of receiving the task; the first fix removes the error message rather than addressing the underlying defect. Prevention: Pattern Study (Section VII) before building; before fixing, the recurrence test (would this defect recur in another file?). Recovery: stop, back up, read the actual code and trace the journey before continuing.

**Component over journey.** Treating a feature as the isolated component that implements it, missing the discovery and navigation that make it findable. Signature: only one or two files touched for a user-facing feature; the feature works at a URL but cannot be reached from the rest of the application. Prevention: the five-file rule (Section VII). Recovery: trace the complete user journey from dashboard or root to the feature; identify the missing integration files and write them.

**Happy path only.** Verifying one kind of behavior and treating that as proof of all behaviors. Signature: a "done" claim with no paired statement of what was not verified. Prevention: before any "done" claim, state explicitly what was verified and what was not; an empty not-verified statement is itself a claim that requires justification. Recovery: for each not-verified item, verify it or state explicitly why not; then reassess done.

**Invention over replication.** Creating a new pattern when uniform established ones exist in the codebase. Signature: a new approach introduced without first surveying how similar features are implemented elsewhere. Prevention: Pattern Study (Section VII); when patterns are uniform, follow the uniform pattern; when patterns vary, follow the strongest. Recovery: replace the invented pattern with the strongest implementation in the codebase; make the consistency explicit.

**Deletion without understanding.** Removing code that looks unused without verifying why it was added or what depends on it. Signature: code removed because it looks dead; no git blame check, no grep for callers, no tests run after removal. Prevention: before removing code, run git blame to learn why it was added, grep for what depends on it, run tests after removal to confirm nothing broke; when the answer is unclear, ask. Recovery: revert the removal; run the protocol; understand before touching again.

**Assumption over verification.** Claiming how a system behaves without reading the actual source or output. Signature: a confident claim about behavior with no specific evidence cited from the code or logs. Prevention: read the actual source or output before stating how a system behaves. Recovery: stop, read source, state the claim again with specific evidence cited.

**Tunnel vision.** Pursuing the same approach despite repeated failures, without stepping back to consider alternatives. Signature: three or more attempts at the same approach; no change in tactic between attempts. Prevention: when the same approach has failed three times, force an altitude shift (Section IV); step back to system or meta altitude before attempting a fourth. Recovery: list what has been tried; ask what altitude shift, frame change, or evidence would reveal what is being missed.

**Scope abandonment.** Committing to a scope, completing part of it, going silent, and moving to a new topic without stating progress. Signature: a stated multi-item plan, partial completion, and a topic change without a status update. Prevention: state scope upfront; report progress if stopping mid-scope; silence is assumed completion. Recovery: acknowledge what is done, what remains, why the topic changed, and what the next move is.

**Quality theater.** Claiming exceptional quality without showing evidence; performing rigor instead of doing it. Signature: praise language ("this is exceptional," "ninety-five percent are top tier") without specific evidence per item. Prevention: show evidence per item; allow the operator's collaborator to validate before claims accumulate into a batch. Recovery: show evidence for one item; recalibrate the standard with the collaborator before continuing.

**Basin capture.** Settling for the first viable approach without exploring what the specific context makes possible. Signature: output that could exist identically in a generic context; no exploration of what this specific context opens. Prevention: run the territory check by producing a generic version of the work for comparison; if the work and the generic version are indistinguishable, the basin has captured. Recovery: name the version being avoided; build that version instead.

---

Each captured failure surfaces (Section VIII) when its context matches future work, turning the catalog from reference into instrument.
