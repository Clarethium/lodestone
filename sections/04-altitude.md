# IV. Altitude

Altitude is the level at which reasoning currently operates. Where calibration in Section III matches stance to conditions, altitude matches scope to the question being asked. Without explicit attention to altitude, long reasoning drifts toward detail and loses contact with why the work matters. The altitude check is the periodic re-anchor that restores breadth.

## Why long reasoning drifts

Long reasoning drifts toward detail. Each turn engages a smaller problem than the turn before. The operator solves what is directly in front of them. The model output reinforces concrete engagement with code and specifics. Without explicit re-anchoring, attention narrows naturally. The original goal can fade across many turns. By turn fifty, the operator is solving micro-issues with no fresh contact with the question that opened the work.

The drift is not a failure of intelligence or attention. It is a structural property of long-context work, intensified by the AI environment where each model response is concrete and arrives quickly. Drift requires intervention; it does not stop on its own.

## The four altitudes

Reasoning operates at one of four altitudes at any moment:

**Meta.** Why the work matters and what the real problem is. Questions at meta altitude: Is this the right problem to be solving? Is the scope right? What is the actual outcome that matters? Meta altitude is the work of framing.

**System.** How the components connect and what is affected. Questions at system altitude: How does this piece fit the rest of the system? What depends on what is being changed? What integration points are involved? System altitude is the work of integration.

**Component.** How a single piece works. Questions at component altitude: How does this function operate? What does this method do? What contract does this code follow? Component altitude is the work of behavior.

**Detail.** Exact implementation. Questions at detail altitude: What is the syntax? What is the variable name? What is the specific logic line by line? Detail altitude is the work of execution.

All four altitudes are valid for the work they fit. Detail altitude is required when implementing. Meta altitude is required when scoping. The methodology does not prescribe a single correct altitude. It prescribes that the operator know which altitude they are currently at, and whether that altitude fits the question currently in front of them.

The failure is not being at detail altitude. The failure is staying at detail altitude when the conditions have changed and a higher altitude is required.

## The altitude check

The altitude check is the periodic action of asking: at what altitude am I currently operating? Is that the altitude this work needs?

The check is reflection-in-action in Donald Schön's sense: questioning, mid-stream, the level at which the work is currently being framed. Where Schön frames reflection-in-action as the practitioner's response to surprise, the altitude check institutionalizes the same move on a regular cadence rather than waiting for surprise to trigger it.

The check has two triggers:

**Cadence.** Every three to five substantive responses, the operator runs the check unprompted. The cadence is short enough to catch drift early, long enough not to interrupt productive work.

**Entropy signals.** Conditions that flag drift before the cadence trigger fires. The operator runs the check immediately when an entropy signal occurs.

The entropy signals are observable conditions that drift has occurred:

- A long response that does not reference the goal of the work
- Three or more iterations on the same narrow problem
- A fix that removes the error message but does not address the underlying defect
- A context switch (new file, new subtask, new direction)
- An "almost done" feeling without a fresh-eyes pass

The first four are checkable in the actual transcript or the actual state of the work. The "almost done" feeling is first-person: the operator's own signal that a fresh-eyes pass is needed before declaring done.

## When to shift altitude

The altitude check produces one of two outcomes. Either the operator is at the altitude the work needs, in which case the check is a no-op and work continues. Or the operator is at the wrong altitude, in which case a shift is required.

The shift direction is determined by the current work, not by preference:

- Stuck at detail with three failed attempts: shift to system or meta. The detail-level work is symptomatic of a problem at a higher level.
- At meta when the work is implementation: shift down to component or detail. The framing work is done; the implementation is now blocking.
- At system when a component bug is blocking: shift to component. The integration question is downstream of resolving the local behavior.

A shift is not a failure. It is the recovery that altitude awareness makes possible.

## Altitude and the rest of the methodology

Altitude composes with the rest of the methodology in specific ways.

Each step of the Loop (Section II) has a typical altitude. Understand often runs at system and meta altitudes. Build runs at component and detail. Verify runs across altitudes depending on what is being verified. Record runs at meta altitude (what was learned at the level of the practice). Done is declared from meta altitude (does this work answer the question that opened it).

Calibration (Section III) and Altitude are the two meta-skills. Calibration asks what stance fits the conditions. Altitude asks what level of reasoning fits the question. The two operate together: an operator can be wrongly calibrated at the right altitude, or rightly calibrated at the wrong altitude. Both fail. Both must be right for the rest of the methodology to work.

Several failure shapes (Section V) are specifically detected by altitude awareness. *Tunnel vision* is a detail-altitude trap: the operator is locked at detail, repeating the same approach. *Speed over understanding* starts at too-low an altitude: the operator engages at component or detail altitude when meta or system altitude is required first. The altitude check is the operator's instrument for detecting these shapes early.
