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
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
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

Стандарт code review, на якому базується ця відповідь, каже: reviewer має схвалювати зміну, коли
вона однозначно покращує загальний стан кодової бази (overall code health), навіть якщо зміна не
ідеальна.[^google-standard]

Вимога ідеальності кожної окремої зміни на практиці гальмує весь проєкт: автори змін уникають
рефакторингу і покращень, бо кожна зміна ризикує застрягти в нескінченному циклі правок. Натомість
якщо зміна рухає код у правильному напрямку і не вносить нових серйозних проблем, її варто
пропустити, а дрібні зауваження залишити на майбутнє.

Блокувати зміну варто, коли вона погіршує code health, а не просто відрізняється від того, як
reviewer написав би її сам: критичні баги, порушення архітектурних принципів, незрозумілий або
невірний дизайн, відсутність тестів для нової логіки, або технічний борг, який ускладнить майбутні
зміни. Це якісно інша категорія зауважень, ніж стилістичні вподобання.

**Як відрізняти блокуючі зауваження від необов'язкових:**
- незначні зауваження (стиль, альтернативне іменування, освітні поради) варто позначати префіксом
  «Nit:» і явно дозволяти автору змержити зміну, не чекаючи на них;
- зауваження про порушення style guide чи некоректний дизайн блокують merge, навіть якщо решта
  зміни хороша;
- новий technical debt, який автор не задокументував і не запланував усунути, – привід попросити
  доопрацювання, а не просто зауваження в коментарі.

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
