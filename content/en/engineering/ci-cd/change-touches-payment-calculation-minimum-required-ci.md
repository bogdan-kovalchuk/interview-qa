---
id: eng-cicd-0001
title: "A change touches payment calculation: what is the minimum required CI gate of unit, integration, and static checks you should choose given the failure risks?"
description: "A change touches payment calculation: what is the minimum required CI gate of unit, integration, and static checks you should choose given the failure risks?"
track: engineering
section: ci-cd
level: middle
type: practical
tags: []
status: published
updated: 2026-09-08
content_revision: 3
reconciled_with:
  uk: 3
anki:
  export: true
sources:
  - source_id: github-continuous-integration
    title: "GitHub Docs: Continuous Integration"
    url: https://docs.github.com/en/actions/get-started/continuous-integration
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Explains CI checks and automated pull-request feedback; it does not prescribe one universal set of checks."
  - source_id: py314-decimal
    title: "Python 3.14 documentation: decimal"
    url: https://docs.python.org/3.14/library/decimal.html
    accessed: 2026-09-08
    kind: official
    version: "3.14"
    applicability: "Defines exact decimal arithmetic, explicit rounding modes, and quantize for monetary calculations in the Python example."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/development/ci_cd.md#L3-L60
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**There is no architecture-independent minimum checklist: make the checks that cover this change's
actual failure boundaries required before merge.** Always test money rules, boundary values and the
named rounding mode deterministically. Add database or provider integration tests only when the
change crosses those boundaries, and run the project's relevant type, lint and security checks.
CI makes those selected checks visible and enforceable on the pull request.[^github-continuous-integration]

## Detailed explanation

A CI gate is a set of automated checks that must pass before a change is allowed to merge into the
main branch.[^github-continuous-integration]

The required set follows the failure model, not the label "payment". Start with the changed path:
the arithmetic and rounding rule, storage representation, serialization, database transaction, or
provider contract. A pure calculation change may need exhaustive unit and property tests but no
live service. A schema or repository change needs a representative database test. A gateway-client
change needs a contract or sandbox test at that boundary. Static analysis is included when the
project has configured it to catch a relevant class of defect; it supplements executable tests but
does not replace them.

Money tests should use exact decimal values and name the rounding rule. Python's `decimal` module
represents decimal inputs exactly and exposes explicit rounding modes.[^py314-decimal] Cover zero,
negative values if the domain permits them, maximum supported values, currency precision, and ties
on both sides of an even digit. Keep storage and provider tests focused on the assumptions the
change actually touches.

An example of a unit test for a boundary value in payment calculation:

```python
def test_rounds_half_cent_with_half_even():
    assert calculate_total_cents(
        subtotal_cents=90,
        tax_rate="0.05",
        rounding="ROUND_HALF_EVEN",
    ) == 94
```

Here the tax is exactly 4.5 cents and `ROUND_HALF_EVEN` rounds it to 4, so the total is 94 cents.
The interface is illustrative; the production test should call the actual domain API.

**Common mistakes with the CI gate for payment code:**
- treating a generic linter, type checker, database, or sandbox test as mandatory without connecting
  it to a failure the change can cause;
- covering only the happy path and omitting exact half-unit, limit, sign, and currency-precision
  boundaries;
- testing only the formula when the changed behavior also depends on storage or provider semantics;
- calling every available check "required", which lengthens feedback without increasing confidence.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
