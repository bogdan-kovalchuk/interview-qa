---
id: eng-codeq-0001
title: "Коли reviewer має схвалити неідеальну зміну, яка покращує overall code health, а коли defect risk або новий technical debt вимагає доопрацювання?"
description: "Reviewer має схвалити зміну, якщо вона беззаперечно покращує загальний стан кодової бази, навіть якщо не ідеальна; відмовити – якщо зміна погіршує code health, додає небажану функціональність або створює критичний..."
track: engineering
section: code-quality
level: senior
type: practical
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: git-git-merge
    title: "Git docs: Git Merge"
    url: https://git-scm.com/docs/git-merge
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація Git."
  - source_id: git-git-rebase
    title: "Git docs: Git Rebase"
    url: https://git-scm.com/docs/git-rebase
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація Git."
  - source_id: git-git-revert
    title: "Git docs: Git Revert"
    url: https://git-scm.com/docs/git-revert
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація Git."
  - source_id: git-git-reset
    title: "Git docs: Git Reset"
    url: https://git-scm.com/docs/git-reset
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація Git."
  - source_id: git-git-reflog
    title: "Git docs: Git Reflog"
    url: https://git-scm.com/docs/git-reflog
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація Git."
  - source_id: github-continuous-integration
    title: "GitHub Docs: Continuous Integration"
    url: https://docs.github.com/en/actions/get-started/continuous-integration
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація GitHub."
  - source_id: gcloud-deployment-strategies
    title: "Google Cloud docs: Deployment Strategies"
    url: https://docs.cloud.google.com/deploy/docs/deployment-strategies
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація Google Cloud."
  - source_id: google-standard
    title: "Google Engineering Practices: Standard"
    url: https://google.github.io/eng-practices/review/reviewer/standard.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційний матеріал Google Engineering Practices."
---

## Short answer

**Reviewer має схвалити зміну, якщо вона беззаперечно покращує загальний стан кодової бази, навіть якщо не ідеальна; відмовити – якщо зміна погіршує code health, додає небажану функціональність або створює критичний technical debt.**[^git-git-merge] Незначні зауваження (стилістика, освітні поради) варто позначати префіксом «Nit:» і не блокувати через них merge. Натомість порушення style guide, некоректний дизайн або неконсистентність із кодовою базою вимагають доопрацювання. Баланс: не перешкоджати прогресу заради дрібниць, але й не накопичувати борг, який згодом змусить переписувати зміну.

## Detailed explanation

TODO

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
