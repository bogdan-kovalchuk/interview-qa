---
id: eng-codeq-0001
title: "When should a reviewer approve an imperfect change that improves overall code health, and when do defect risk or new technical debt require more work first?"
description: "When should a reviewer approve an imperfect change that improves overall code health, and when do defect risk or new technical debt require more work first?"
track: engineering
section: code-quality
level: senior
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
---

## Short answer

**A reviewer should approve a change when it unambiguously improves the overall health of the codebase, even if it is not perfect; and refuse it when it degrades code health, adds unwanted functionality or creates critical technical debt.**[^git-git-merge] Minor remarks (style, educational suggestions) are worth prefixing with "Nit:" and should not block the merge. Style guide violations, incorrect design or inconsistency with the codebase, on the other hand, do require rework. The balance: do not hold up progress over trifles, but do not accumulate debt that later forces the change to be rewritten either.

## Detailed explanation

The code review standard this answer rests on says that a reviewer should approve a change once it
unambiguously improves the overall code health of the codebase, even when that change is not
perfect.[^google-standard]

Demanding perfection of every individual change slows the whole project down in practice: authors
avoid refactoring and improvements, because every change risks getting stuck in an endless cycle of
revisions. If instead a change moves the code in the right direction and introduces no new serious
problems, it is worth letting through, leaving the small remarks for later.

A change is worth blocking when it degrades code health, not merely when it differs from how the
reviewer would have written it: critical bugs, violations of architectural principles, unclear or
wrong design, missing tests for new logic, or technical debt that will complicate future changes.
That is a qualitatively different category of remark from a stylistic preference.

**How to tell a blocking remark from an optional one:**
- minor remarks (style, alternative naming, educational suggestions) are worth prefixing with
  "Nit:" and explicitly letting the author merge without waiting on them;
- a remark about a style guide violation or incorrect design blocks the merge, even when the rest
  of the change is good;
- new technical debt the author has neither documented nor planned to remove is a reason to ask for
  rework, not just a comment.

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
