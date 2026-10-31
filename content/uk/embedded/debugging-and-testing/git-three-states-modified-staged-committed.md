---
id: emb-build-0001
title: "Які три основні стани має git?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: git-scm-doc
    title: "Git documentation"
    url: https://git-scm.com/doc
---

## Short answer

У базовій моделі Git файл проходить три стани:[^dou-embedded-interview]

- **Modified** – файл змінено у робочій директорії, але ще не додано в індекс.
- **Staged** – зміни додано в staging area командою `git add`; вони готові потрапити в наступний commit.
- **Committed** – зміни збережені в локальному репозиторії як commit.

Типовий цикл: редагування файлу, потім `git add file`, потім `git commit -m "message"`.

## Detailed explanation

У Git кожен файл проходить три стани, які відповідають трьом областям сховища:[^git-scm-doc]

**Working directory** (робоча директорія) – це ваша локальна копія файлів, де ви редагуєте код. Коли ви змінюєте файл, він переходить у стан **modified** – зміни є, але Git ще не знає про них для наступного commit.

**Staging area** (index) – це проміжна область, куди ви додаєте зміни командою `git add`. Файл у стані **staged** означає, що ви підготували ці зміни для наступного commit. Staging area дозволяє обрати, які саме зміни потраплять у commit, а не commit-ити все одразу.

**Git repository** (локальний репозиторій) – це база даних Git, де зберігаються commit-и. Коли ви виконуєте `git commit`, staged зміни переходять у стан **committed** – вони стають частиною історії репозиторію.

Типовий цикл роботи:

```bash
$ vim file.c

$ git status

$ git add file.c

$ git commit -m "Add feature X"
```

Git зберігає кожний commit як snapshot (знімок) стану файлів. Коли ви commit-ите, Git створює новий об’єкт commit, який посилається на snapshot та попередній commit, формуючи лінійну історію. Staging area є ключовою особливістю Git, яка відрізняє його від інших VCS – вона дає точний контроль над тим, що потрапляє у кожний commit.
