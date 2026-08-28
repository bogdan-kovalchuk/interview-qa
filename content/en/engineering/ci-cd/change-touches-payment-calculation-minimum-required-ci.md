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
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: git-git-merge
    title: "Git docs: Git Merge"
    url: https://git-scm.com/docs/git-merge
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official Git documentation."
  - source_id: git-git-rebase
    title: "Git docs: Git Rebase"
    url: https://git-scm.com/docs/git-rebase
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official Git documentation."
  - source_id: git-git-revert
    title: "Git docs: Git Revert"
    url: https://git-scm.com/docs/git-revert
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official Git documentation."
  - source_id: git-git-reset
    title: "Git docs: Git Reset"
    url: https://git-scm.com/docs/git-reset
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official Git documentation."
  - source_id: git-git-reflog
    title: "Git docs: Git Reflog"
    url: https://git-scm.com/docs/git-reflog
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official Git documentation."
  - source_id: github-continuous-integration
    title: "GitHub Docs: Continuous Integration"
    url: https://docs.github.com/en/actions/get-started/continuous-integration
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official GitHub documentation."
  - source_id: gcloud-deployment-strategies
    title: "Google Cloud docs: Deployment Strategies"
    url: https://docs.cloud.google.com/deploy/docs/deployment-strategies
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official Google Cloud documentation."
  - source_id: google-standard
    title: "Google Engineering Practices: Standard"
    url: https://google.github.io/eng-practices/review/reviewer/standard.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official Google Engineering Practices material."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/development/ci_cd.md#L3-L60
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**For payment calculation, the minimum CI gate is unit tests for boundary values and currency
formats, integration tests against a real or emulated database, and static checks (linter + type
checker).**[^git-git-merge] An error in the calculation carries a high failure risk (financial
loss, incorrect transactions), so skipping any of the three levels is not acceptable. Unit tests
cover the formulas and edge cases, integration tests cover the interaction with the database and
external services, and static checks catch type errors and unused variables before the tests even
run. Merging is allowed only after the full pipeline is green.

## Detailed explanation

A CI gate is a set of automated checks that must pass before a change is allowed to merge into the
main branch.[^github-continuous-integration]

The minimum required set depends on failure risk: the more expensive the error, the wider the
coverage required before merge. For payment calculation, the cost of a defect is money (a wrong
amount, a double charge, a lost cent from rounding), so none of the three check levels can be
skipped.

Unit tests exercise the calculation formula itself – boundary values (zero, negative amounts, the
maximum), rounding, and handling different currencies and locales. Integration tests check that
the calculation interacts correctly with a real or emulated database and external services (for
example, a payment gateway) – this is where bugs like the wrong column type for money get caught.
Static checks (linter, type checker) catch a class of errors that do not depend on the logic –
a wrong argument type, an unused variable – and do it before the tests even run, so it is cheaper
and faster.

An example of a unit test for a boundary value in payment calculation:

```python
def test_rounds_half_cent_down():
    assert calculate_total(cents=1005, tax_rate=0.0725) == 1078  # not 1079
```

**Common mistakes with the CI gate for payment code:**
- treating static checks as a formality and not blocking merge on them, even though they catch
  type errors in money calculations;
- covering only the "happy path" with unit tests, skipping boundary values (zero, rounding,
  negative amounts);
- testing the calculation in isolation from the database, missing that the real column stores the
  amount as a `float` instead of a `decimal`.

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
