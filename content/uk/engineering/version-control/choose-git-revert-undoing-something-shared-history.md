---
id: eng-vcs-0004
title: "Коли для undo в shared history обрати `git revert`, коли `git reset` допустимий для unpublished commits і як reflog допомагає відновити lost local tip?"
description: "git revert – для скасування комітів у shared history (створює новий commit із протилежними змінами); git reset допустимий лише для ще не push-нутих комітів; git reflog зберігає всі попередні позиції HEAD і дозволяє..."
track: engineering
section: version-control
level: middle
type: comparison
tags: [git-revert, git-reset]
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

**`git revert` – для скасування комітів у shared history (створює новий commit із протилежними змінами); `git reset` допустимий лише для ще не push-нутих комітів; `git reflog` зберігає всі попередні позиції `HEAD` і дозволяє знайти SHA втраченого коміту.**[^git-git-merge] Revert не переписує існуючу історію, тому безпечний для push. Reset переміщує вказівник гілки назад – `--hard` додатково очищає index і working tree. Якщо reset видалив потрібний коміт з гілки, `git reflog` показує, де був `HEAD` раніше (наприклад, `HEAD@{2}`), і коміт можна відновити через `git reset` або `git cherry-pick` на цей SHA, поки reflog не протерміновано (типово 30–90 днів).

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
