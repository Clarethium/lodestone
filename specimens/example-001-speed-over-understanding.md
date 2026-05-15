---
id: example-001
failure_shape: Speed over understanding (Section V)
surface: general
model_context: 2026-era LLM coding assistance
status: illustrative
---

# Speed over understanding: error-message removal at the symptom

## Cue

The assistant proposes a fix that suppresses an error message without first explaining what produced the undefined value. The fix would make the failing test pass without locating the defect.

## Situation (abstracted)

A test in a downstream module fails with a "cannot read property X of undefined" error. The proposed fix adds a null check at the failure site. The undefined value originates from a fixture renamed in a recent commit; the middleware that constructs the request still reads the stale config key. Adding the null check at the failure site hides the actual defect: every other caller of the same middleware is silently passing the wrong value.

## What was about to happen

Apply the null check at the failure site, watch the test pass, declare done. The reported bug would be "fixed" until another caller hits the same stale key, at which point the same shape recurs in a different file.

## Recovery

Trace the call chain upstream from the failure site. The undefined value originates two files up, in the middleware reading from the stale config key. Fix at the source. The original test passes for the right reason; other callers stop being latent breakages of the same defect.

## Prevention

Before applying any fix that suppresses an error message, run the Section V recurrence test for *Speed over understanding*: would this defect recur in another file? If the answer is yes, the fix at the failure site is wrong target. The upstream is the right target.

## What this specimen does not preserve

Operator project, specific file paths, language and framework, the exact stale config key, the exact rename that introduced the divergence, model identity. The shape preserved here is the failure pattern: a fix that suppresses a symptom while the upstream defect continues to recur through other call sites.
