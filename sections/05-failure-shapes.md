# V. Failure Shapes

Failure shapes are recurring patterns by which disciplined work breaks down. Each shape names a specific way the work pulls into something that looks complete but is not. Naming the shapes makes them visible; visible shapes are easier to detect early and recover from cleanly.

Ten shapes follow, each with the concept it names and a short detection signature. Detailed prevention patterns and recovery moves come in later passes; this skeleton fixes the names.

---

**Speed over understanding.** Starting work before grasping the system or the defect. Signature: code begins within minutes of receiving the task; the first fix removes the error message rather than addressing the underlying defect.

**Component over journey.** Treating a feature as the isolated component that implements it, missing the discovery and navigation that make it findable. Signature: only one or two files touched for a user-facing feature; the feature works at a URL but cannot be reached from the rest of the application.

**Happy path only.** Verifying one kind of behavior and treating that as proof of all behaviors. Signature: a "done" claim with no paired statement of what was not verified; verification at one level treated as coverage of all levels.

**Invention over replication.** Creating a new pattern when uniform established ones exist in the codebase. Signature: a new approach introduced without first surveying how similar features are implemented elsewhere.

**Deletion without understanding.** Removing code that looks unused without verifying why it was added or what depends on it. Signature: code removed because it looks dead; no git blame check, no grep for callers, no test run after removal.

**Assumption over verification.** Claiming how a system behaves without reading the actual source or output. Signature: a confident claim about behavior with no specific evidence cited from the code or logs.

**Tunnel vision.** Pursuing the same approach despite repeated failures, without stepping back to consider alternatives. Signature: three or more attempts at the same fix; mounting frustration without altitude shift.

**Scope abandonment.** Committing to a scope, completing part of it, going silent, and moving to a new topic without stating progress. Signature: a stated multi-item plan, partial completion, and a topic change without a status update.

**Quality theater.** Claiming exceptional quality without showing evidence; performing rigor instead of doing it. Signature: praise language ("this is exceptional," "ninety-five percent are top tier") without specific evidence per item.

**Basin capture.** Settling for the first viable approach without exploring what the specific context makes possible. Signature: output that could exist identically in a generic context; no exploration of what this specific context opens.
