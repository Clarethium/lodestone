# VII. Surface Discipline

A surface is a domain area within the work: database, authentication, payments, git operations, UI components, system internals, infrastructure, documentation, general code. Different surfaces carry different risks. The same operator stance applied uniformly across surfaces fails on the surfaces where the consequences of error are highest.

Surface discipline is the practice of applying additional rigor proportionate to the risk on a given surface. The methodology described in earlier sections (stance, the Loop, calibration, altitude) is uniform across all surfaces. Surface discipline adds surface-specific protocols on top of the uniform foundation.

This section names the surfaces that most often warrant heightened discipline, sketches the protocol for each, and specifies three universal practices (Pattern Study, the five-file rule, the fresh-eyes test) that compose with any surface.

## High-risk surfaces

A high-risk surface is one where errors are difficult to detect, hard to recover from, or have consequences that extend beyond the immediate work. The four canonical high-risk surfaces:

**System internals.** Core logic, infrastructure, and shared utilities. Errors propagate to everything that depends on them. Recovery is expensive because dependents may have already shipped against the broken behavior. The discipline: understand the full call chain before modifying, map dependents, identify implicit contracts that depend on current behavior, plan rollback for infrastructure changes.

**System analysis.** Recommendations to consolidate, refactor, or restructure. The risk is asymmetric: a wrong recommendation that gets adopted is expensive to undo. The discipline: distinguish hypothesis from verified claim. State the hypothesis explicitly, state evidence for and against, state what was actively done to disconfirm. Empty disconfirming evidence is incomplete analysis. Actionable recommendations require a verified status; observations that lack verification stay observations.

**Authentication, authorization, and payments.** Errors here have user-facing consequences ranging from privacy breach to financial loss. The methodology-level discipline:

- Validate inputs at the boundary, by allow-list rather than deny-list
- Require both authentication and resource-specific authorization on protected routes
- Rate-limit sensitive endpoints
- Treat secrets as configuration, not code
- Audit-log sensitive operations
- Never trust client-side state for security decisions
- Never store credentials in reversible form

Tactical specifics (parameterized queries, CSRF tokens, JWT expiration, route patterns, the full catalog of anti-patterns) are canonicalized in OWASP and similar references; the discipline above is the methodology-level rule, not a substitute for the tactical canon.

**Git write operations.** Operations that modify version control state can lose work or rewrite published history. The discipline: check status before any write; stage explicit files only, never `git add .` or `git reset HEAD`; ask before touching files the operator did not modify; when stuck, stop and state what is seen rather than guessing.

## Other discipline surfaces

Some surfaces are not high-risk but warrant surface-specific protocols.

**Database.** Errors are usually recoverable by migration, but the cost of recovery is real. The protocol: read the exact schema before any change, identify required versus optional versus auto-generated fields, plan rollback before changes, check existing migration patterns.

**UI components.** User-facing components require attention to integration (does the user discover the feature?) and to accessibility (semantic HTML, keyboard navigation, focus indicators, form labels, color contrast). Integration is operationalized by route types, route mappings, and navigation UI; the five-file rule (below) checks the file-count signal; design quality is addressed in Section VI.

Other surfaces (documentation, general code, infrastructure) carry lower risk and rely on the universal practices below without surface-specific protocols.

## Three universal practices

Three practices apply across all surfaces. Each operationalizes a directive from Section I (Stance) and feeds the Loop's Understand and Verify steps.

### Pattern Study

Pattern Study is the practice that operationalizes *Patterns over invention* (Section I). Before writing new code, the operator finds three similar features already implemented in the codebase and reads their complete implementations.

The practice has a specific shape:

1. Find three (not one or two) similar features. One example may be unrepresentative; three reveal the convention.
2. Read each complete implementation, not just the parts visible in the area being changed.
3. Map the structural patterns: file organization, naming, the order of operations, the conventions for error handling.
4. Where the three are uniform, follow the uniform pattern. Where they vary, follow the strongest implementation.

The practice fails when the operator skims one example and starts writing. Pattern Study takes longer to begin than improvising; the time spent compounds across the work, because every subsequent decision falls within the established pattern rather than diverging from it.

### The five-file rule

The five-file rule operationalizes *Component over journey* (Section V). A user-facing feature modifies at least five files: data layer, API or business logic, page or component, navigation type definitions, navigation UI. Touching only one or two files for a user-facing feature signals missing integration.

The rule is an indicator, not a quota. Some features legitimately touch fewer files; others touch many more. The signal is that one or two files for a user-facing feature usually means the feature is invisible to users, undiscoverable from the navigation, or lacks the integration that makes it actually a feature rather than a hidden URL.

When the operator notices the file count is low, the response is not to invent files for the count's sake. The response is to ask: how does the user discover this feature, and what makes that discovery work? The answer often reveals the integration files that were not touched.

### The fresh-eyes test

The fresh-eyes test operationalizes the Done step of the Loop (Section II). Before declaring done, the operator approaches the work as if encountering it for the first time:

1. Clear context. Open the application or codebase from a fresh state.
2. Find the feature via the UI only, without typing the URL or using a bookmark. If the feature cannot be found and is meant to be reachable from the UI, the integration is incomplete.
3. Complete the workflow end-to-end. Follow the user's path from start to finish.
4. Check the console, network, and logs for errors. Silent failures are still failures.
5. Ask: would I ship this now?

The fresh-eyes test catches what the operator's familiarity hides. After hours of work on a feature, the operator's eyes have adapted to the work's incompleteness. The test resets that adaptation.

## Surfaces and practices together

Surface discipline and universal practices compose. The surface tells the operator what protocols apply; the universal practices apply on top. A change to authentication code that touches the database benefits from both the auth checklist and the database protocol, plus Pattern Study for finding how the codebase already implements similar auth-database operations, plus the fresh-eyes test before declaring done.

The discipline is not to memorize every protocol. The discipline is to recognize which surface the current work is on, retrieve the relevant protocol, and apply the universal practices alongside. The protocols themselves are a reference, not a curriculum: the operator returns to them when the work touches the relevant surface.
