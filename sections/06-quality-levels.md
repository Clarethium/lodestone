# VI. Quality Levels

The methodology distinguishes four quality levels. Each is a different bar for what "done" means. Most work targets a level that fits the stakes; not all work warrants the highest level. Recognizing which level the current work needs is part of calibration (Section III).

## The four levels

**Functional.** The code runs. It handles the happy path. It is basically correct. Functional is the minimum bar; below it, the work is not done.

**Complete.** All user flows work. Error states are handled. Integration points are connected. The work passes the fresh-eyes test (Section VII). Complete is the bar for any feature that ships.

**Polished.** Performance is acceptable. Accessibility is checked. Edge cases are covered. The work passes a self-review checklist for the surface it touches. Polished is the bar for work that the operator wants to be confident in for the long run.

**Exceptional.** The work reaches territory that the default implementation cannot. The specific context (user data, problem, constraints) has been used to produce something a generic implementation could not produce. Exceptional is reserved for work where stopping at Polished would be a missed opportunity that the context made available.

## Where each level applies

Most work targets Complete or Polished. Functional is for prototypes and exploration; below Complete, the work is not ready to ship. Exceptional is reserved for critical or visible features where the specific context offers something that a generic implementation would miss.

The mistake is targeting Exceptional uniformly. Exceptional takes longer than Polished, is harder to verify, and produces marginal or zero gains on work where the default already serves. Exceptional applied to internal tooling or generic CRUD is over-investment. Polished applied to a flagship user-facing feature is under-investment.

Calibration is what tells the operator which level fits the current work. Stakes, visibility, audience, and the specific opportunities the context opens together set the right level. The methodology does not prescribe a single answer; it requires the operator to choose deliberately rather than default to one level uniformly.

## The specificity tests

Distinguishing Exceptional from Polished requires specific tests. Polished work passes the self-review checklist. Exceptional work passes specificity tests, which check whether the work has actually reached past the default.

The core specificity test:

**Is user data the structure of the work, or is it filling a template?**

If the user data shapes the structure of what is produced, the work is specific to the context. If the user data fills slots in a template that would be filled with anyone's data the same way, the work is generic. Polished, perhaps, but not Exceptional.

Additional specificity tests:

**Could this exist in a generic SaaS or generic codebase?** If yes, the work has not yet reached the territory the specific context opens. The default has been served, not exceeded.

**Is the information density per surface intentional?** Default implementations distribute information uniformly. Specific implementations recognize where the operator's attention will land and put information density there.

**What longer flows pass through this work?** Specific work participates in the flows the system supports (a user's progression, a data lifecycle, a development cycle). Generic work stands alone.

**Does the work adapt to context or state?** A specific implementation reads the current state and shapes itself accordingly. A generic implementation produces the same output regardless of state.

The tests are not pass/fail individually. They are diagnostic: each test surfaces a different angle from which to ask whether the work has reached past the default. Work that passes most or all of them has reached the territory the context opened. Work that passes none of them has stayed in the default zone where any operator with the brief would have produced the same output.

## The structure test in practice

Of the specificity tests, the structure test is the most diagnostic and the most often missed.

The default failure mode: the operator builds a template that accepts user data, displays it competently, and ships. The user data is the content; the template is the structure. The work is Polished. The template displays the data correctly, handles edge cases, looks clean. But the structure is not specific. The same template would accept any user's data and produce the same shape.

The Exceptional version: the operator notices that the user's data has a structure of its own. The relationships between the data, the patterns within it, and the timing and sequence are the structure. The template is shaped by what the data is, not the other way around. Two different users produce two different shapes because their data has two different structures.

The structure test asks the operator to look at the work and answer: if I replaced this user's data with another user's data, would the work look different in shape, or only in content? Different in shape means the structure is specific. Different only in content means the structure is generic.

The test is asymmetric. Generic work rarely becomes specific through more polish; it usually requires going back to the structure question and answering it differently. Specific work, structured around real user data, has a path to Exceptional that template-based work does not, because the structure does work the template alone cannot.
