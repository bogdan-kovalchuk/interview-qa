---
id: emb-build-0001
title: "What are the three main states in git?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: git-scm-doc
    title: "Git documentation"
    url: https://git-scm.com/doc
---

## Short answer

In the basic Git model, a file goes through three states:[^dou-embedded-interview]

- **Modified** – the file has been changed in the working directory but not yet added to the index.
- **Staged** – the changes have been added to the staging area with `git add`; they are ready to go into the next commit.
- **Committed** – the changes have been saved in the local repository as a commit.

Typical cycle: edit a file, then `git add file`, then `git commit -m "message"`.

## Detailed explanation

In Git, every file passes through three states corresponding to three areas of the repository:[^git-scm-doc]

**Working directory** is your local copy of files where you edit code. When you change a file, it enters the **modified** state – the changes exist, but Git does not yet know about them for the next commit.

**Staging area** (index) is the intermediate area where you add changes with the `git add` command. A file in the **staged** state means you have prepared these changes for the next commit. The staging area allows you to select exactly which changes go into the commit, rather than committing everything at once.

**Git repository** (local repository) is the Git database where commits are stored. When you run `git commit`, staged changes move to the **committed** state – they become part of the repository history.

Typical workflow cycle:

```bash
$ vim file.c

$ git status

$ git add file.c

$ git commit -m "Add feature X"
```

Git stores each commit as a snapshot of the file state. When you commit, Git creates a new commit object that references the snapshot and the previous commit, forming a linear history. The staging area is a key Git feature that distinguishes it from other VCS – it gives precise control over what goes into each commit.
