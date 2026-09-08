---
id: emb-build-0003
title: "Що таке інтерактивний rebase?"
description: "git rebase -i відкриває список commits перед обраною базою, дозволяючи pick, reword, squash, edit чи drop кожен commit, переписуючи історію."
track: embedded
section: toolchain-and-build
level: junior
type: concept
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
  - source_id: git-scm-doc
    title: "Git documentation"
    url: "https://git-scm.com/doc"
    accessed: 2026-09-08
    kind: official
    version: "current"
    applicability: "Official Git reference for version control concepts; specific workflows may vary by Git version."
---

## Short answer

`git rebase -i` – режим редагування історії commits перед обраною базою.[^dou-embedded-interview] Він відкриває список commits, де можна змінити дії для кожного commit.

Типові дії: `pick` – залишити commit; `reword` – змінити повідомлення; `squash`/`fixup` – об'єднати commits; `edit` – зупинитися для правки commit; `drop` – видалити commit; можна також змінити порядок commits.

Використання: почистити локальну feature-гілку перед pull request, об'єднати дрібні fixup commits, виправити commit message. Важливо: це <span class="warn">переписує історію</span>, тому обережно з commits, які вже були відправлені й використовуються іншими.

## Detailed explanation

**Interactive rebase** (`git rebase -i`) – це режим редагування історії commits, який дозволяє змінити, об'єднати, перейменувати або видалити commits у локальній гілці перед тим, як поділитися нею з іншими.[^git-scm-doc]

Коли ви виконуєте `git rebase -i HEAD~N` (де N – кількість commits), Git відкриває текстовий редактор зі списком commits та доступними діями:

```
pick abc1234 Add initial implementation
pick def5678 Fix typo in comment
pick ghi9012 Add missing error handling
```

**Доступні дії:**
- `pick` – залишити commit без змін
- `reword` – змінити commit message
- `squash` – об'єднати з попереднім commit (обидва messages)
- `fixup` – об'єднати з попереднім commit (тільки changes, message відкидається)
- `edit` – зупинитися для редагування файлів та amend commit
- `drop` – видалити commit
- Можна також змінити порядок commits, переставивши рядки

**Типове використання:**

```bash
$ git rebase -i HEAD~5

$ git commit --fixup=abc1234
$ git rebase -i --autosquash abc1234~1
```

Interactive rebase корисний для:
- Об'єднання дрібних commits у логічні зміни (squash/fixup)
- Виправлення commit messages (reword)
- Видалення тимчасових або експериментальних commits (drop)
- Зміни порядку commits для кращої читабельності історії

**Важливо:** interactive rebase переписує історію, змінюючи commit hashes. Це безпечно лише для локальних commits, які ще не були відправлені на remote. Якщо ви вже push-или commits, rebase створить конфлікти для інших розробників, які працюють з цією гілкою.

Якщо потрібно оновити remote після rebase, використовуйте `git push --force-with-lease` (безпечніший варіант ніж `--force`, бо перевіряє, що remote гілка не змінилася).

Для скасування rebase можна використати `git reflog` для знаходження попереднього HEAD та `git reset --hard HEAD@{N}` для відкату.

## Sources

<!-- generated from frontmatter -->
