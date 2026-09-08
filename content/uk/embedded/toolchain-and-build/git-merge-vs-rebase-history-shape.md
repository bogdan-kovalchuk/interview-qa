---
id: emb-build-0007
title: "В чому полягає різниця між merge та rebase?"
description: "git merge зберігає розгалужену історію через merge commit, а git rebase переносить commits на нову базу і робить історію лінійною, переписуючи хеші."
track: embedded
section: toolchain-and-build
level: junior
type: comparison
tags: []
status: published
updated: 2026-09-08
content_revision: 4
reconciled_with:
  en: 4
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу toolchain-and-build; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
  - source_id: git-scm-doc
    title: "Git documentation"
    url: "https://git-scm.com/doc"
    accessed: 2026-09-08
    kind: official
    version: "current"
    applicability: "Official Git reference for version control concepts; specific workflows may vary by Git version."
---

## Short answer

`git merge` об'єднує дві гілки, зберігаючи їхню історію; якщо історії розійшлися, Git створює merge commit.[^dou-embedded-interview] Плюс: чесно показує, коли й де гілки були об'єднані; мінус: історія може стати розгалуженою.

`git rebase` переносить commits поточної гілки поверх іншої бази, ніби робота починалась від новішого commit. Плюс: лінійна й чистіша історія; Мінус: rebase переписує commit hash-и.

Практичне правило: **merge** безпечний для спільних/published гілок; **rebase** зручний для локальної feature-гілки перед merge, але не варто rebase-ити чужу опубліковану історію без домовленості.

## Detailed explanation

`git merge` і `git rebase` – два способи інтегрувати зміни з однієї гілки в іншу, але вони працюють по-різному і дають різну форму історії.[^git-scm-doc]

**git merge** створює новий merge commit, який має двох батьків: поточний HEAD гілки і гілку, яку merge-ють. Це зберігає точну історію розробки – видно, коли гілки розійшлися і коли знову зустрілися. Merge не переписує існуючі commit-и, тому безпечний для опублікованих гілок.

**git rebase** бере commit-и поточної гілки і "переграє" їх поверх іншої бази (base). Результат – лінійна історія без merge commit-ів. Але rebase створює нові commit-и з новими hash-ами, тому старі commit-и зникають з історії.

```bash
# Merge: preserves branched history
$ git checkout main
$ git merge feature
# Creates a merge commit with two parents

# Rebase: linear history
$ git checkout feature
$ git rebase main
# Replays feature commits on top of main
$ git checkout main
$ git merge feature  # fast-forward merge
```

Rebase зручний для очищення локальної історії перед merge: можна об'єднати commit-и (`squash`), змінити порядок, відредагувати повідомлення через `git rebase -i` (interactive rebase).


## Comparison

| Критерій | git merge | git rebase |
|---|---|---|
| Форма історії | Розгалужена з merge commit | Лінійна без merge commit |
| Переписує commit-и | Ні | Так (нові hash-и) |
| Безпечний для published гілок | Так | Ні (тільки для локальних) |
| Вирішення конфліктів | Один раз при merge | Потрібно для кожного commit окремо |
| Відкат | Легко (`git revert merge-commit`) | Складніше (потрібно знати старі hash-и) |

## When to choose which

**Обирайте merge**, коли:
- Гілка опублікована і використовується іншими розробниками
- Потрібно зберегти точну історію розробки
- Працюєте у великій команді з паралельною розробкою

**Обирайте rebase**, коли:
- Потрібно очистити локальну історію перед merge (squash, reorder, edit)
- Feature-гілка ще не опублікована
- Хочете лінійну історію без merge commit-ів
- Готуєте commit-и до code review (кожен commit – логічна зміна)

**Золоте правило**: ніколи не робіть rebase опублікованих гілок, які використовують інші люди. Rebase переписує історію, і якщо хтось вже pull-ив старі commit-и, виникнуть конфлікти при наступному push.


## Sources

<!-- generated from frontmatter -->
