# I. Stance

Stance is the operator's disposition toward AI work, prior to any specific task. It is prior to method and prior to tactic. The stance determines how the operator interprets uncertainty, how they treat AI output, how they decide when to verify, and how they recognize their own drift.

The methodology frames operator-AI work as a coupled cognitive system rather than a tool-use relationship: the operator and the model engage in a continuous loop where each shapes the other's contribution. The framing extends Edwin Hutchins's distributed cognition (*Cognition in the Wild*, 1995) and Andy Clark's extended-mind thesis (*Supersizing the Mind*, 2008) to the operator-AI domain; the underlying claim that cognition is a property of human-tool-environment systems carries over directly. Where Hutchins's distributed cognition models cognition across multiple human agents and shared instruments, and Clark's extended mind models a single agent's cognition reaching into passive external aids, operator-AI work combines features of both without reducing to either: a single operator coupled with a generative partner that produces hypotheses requiring evaluation rather than tools storing memory or peers contributing reasoning. Stance is the operator's contribution to that coupling; it shapes what the system as a whole produces.

The operator stance has four directives. They are simple to state and difficult to hold under pressure. The work of stance is not learning the directives but holding them when conditions favor abandoning them.

## Frame-awareness

Underlying the four directives is frame-awareness: the discipline of noticing the frame the work is operating within. A frame is the implicit configuration of a problem: which questions are being asked, which approaches are being considered, what counts as evidence. Frames form from prior assumptions, experience, and recent context; they are invisible to the operator inside them until something forces re-framing. The basin a frame pulls toward (its default approach) captures unexamined work.

Frame-awareness draws on Donald Schön's frame reflection (*The Reflective Practitioner*, 1983; with Martin Rein, *Frame Reflection*, 1994): the practitioner's capacity to step back and notice the framing that has organized their approach to a problem, particularly when standard approaches are failing in ways the standard frame cannot diagnose.

The directives below presuppose frame-awareness. Without it, the operator can follow the directives correctly inside an unexamined frame and produce competent work that solves the wrong problem cleanly. Several recovery moves elsewhere in this document operationalize frame-awareness for specific failures: saturation and return (Section III) recovers from frame-stuck, the altitude check (Section IV) detects when reasoning has drifted to the wrong altitude for the work, and basin capture (Section V) is the failure shape that frame-awareness most directly prevents.

## Evidence over assumption

The operator does not state how a system behaves without specific evidence from the system. AI output is not evidence about the system; it is a hypothesis about how the system might behave. Evidence comes from reading the actual code, running the actual command, observing the actual output.

This applies to the operator's own claims and to AI-generated claims uniformly. When the AI says "this code calls X," that is a hypothesis worth checking, not a fact about the code. When the operator says "the function does Y," that statement is only as strong as the evidence read from the function. The operator judges AI output by evidence, not evidence by AI output. Output that contradicts evidence is wrong; output that matches evidence is at least confirmed against that evidence.

The directive does not preclude rapid work. It precludes claims without evidence. Rapid work that maintains evidence-for-claim is the goal; rapid work that asserts without checking is the failure.

## Systems over tasks

The operator works on tasks within systems, not tasks divorced from systems. A change to a function happens in the context of where the function is called, what depends on its behavior, and what conventions the surrounding code follows. A new feature happens in the context of how the rest of the application is organized, navigated, and tested.

The reverse stance, task without system, tends to produce work that compiles in isolation and breaks at the integration boundary: components that pass unit tests and fail in production. The operator who treats systems as the unit of work produces components that fit, because they were designed for the system from the start.

The directive applies at every altitude. At the meta altitude, it asks whether the task is the right framing of the problem. At the system altitude, it asks how the components connect. At the component altitude, it asks how this piece fits the whole. At the detail altitude, it asks whether the implementation matches the conventions of similar code.

## Patterns over invention

When patterns exist in a system, the operator follows them rather than introducing new ones. Consistency across a codebase is its own form of correctness. A new pattern is justified only when an existing pattern clearly fails the work at hand, and even then the new pattern is justified explicitly, not invented quietly.

The directive is not a prohibition on improvement. It is a prohibition on ignoring what exists. The operator who studies three similar features before writing a fourth will produce work that fits; the operator who writes the fourth without study will produce work that drifts from the system's voice.

The shape of the directive is: study before invention. Pattern Study (Section VII) is the practice that operationalizes this stance.

## Prevention over detection

The operator prefers preventing a failure to detecting it after the fact. Detection requires watching for symptoms; prevention requires understanding root causes. Prevention can scale to failures that have not yet occurred by addressing root causes; detection requires recognizable symptoms.

The directive shapes how the operator records what they learn. A failure that is detected and not understood will recur. A failure that is detected, understood, and surfaced as a warning before the next operation that could repeat it will not. Compound practice (Section VIII) describes the mechanism. The stance is what makes the operator use it.

## The integrity principle

Three formulations hold the integrity principle:

- **Stated equals done.** A claim of completion is only valid when the work it claims to describe has actually been done. Saying "I've recorded that" is not a recording; running the command is.
- **Scope committed equals scope completed.** A commitment to do all of N items is fulfilled when N items are done, not when fewer are done and the topic changes.
- **Quality claimed equals quality demonstrated.** A claim that work is exceptional is only valid when the evidence for the claim is shown.

The integrity principle is not a moral injunction. It is a precondition for the rest of the methodology to work. Compound learning requires accurate records of what was done; calibration requires accurate self-reports of what was verified; the loop requires that "done" mean what it says. Without integrity, the rest is theater.
