---
id: emb-build-0002
title: "Name the basic git commands."
description: "Basic git commands cover the local cycle (init, add, commit, log, diff) and branch synchronization (branch, switch, merge, rebase, pull, push)."
track: embedded
section: toolchain-and-build
level: junior
type: concept
tags: []
status: published
updated: 2026-09-08
content_revision: 4
reconciled_with:
  uk: 4
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of this question and answer; the answer text is not independently verified against the original community Anki deck."
  - source_id: git-scm-doc
    title: "Git documentation"
    url: "https://git-scm.com/doc"
    accessed: 2026-09-08
    kind: official
    version: "current"
    applicability: "Official Git reference for version control concepts; specific workflows may vary by Git version."
---

## Short answer

Basic commands:[^dou-embedded-interview]

`git init` – create a repository; `git clone URL` – copy an existing one; `git status` – check the state; `git add` – add changes to the staging area; `git commit` – create a commit; `git log` – history; `git diff` – view differences.

Branches and synchronization: `git branch` – list/create branches; `git switch` or `git checkout` – switch to a branch; `git merge` – merge branches; `git rebase` – move commits to another base; `git pull` – fetch and integrate changes; `git push` – send commits to a remote.

## Detailed explanation

Basic Git commands can be grouped by purpose:[^git-scm-doc]

**Repository setup:**
- `git init` – create a new repository
- `git clone URL` – clone an existing repository

**Modify -> stage -> commit cycle:**
- `git status` – show file states (modified/staged/untracked)
- `git add file` – add changes to the staging area
- `git commit -m "message"` – create a commit from staged changes
- `git diff` – show changes between working directory and staging area
- `git diff --staged` – show changes between staging area and last commit

**History inspection:**
- `git log` – show commit history
- `git log --oneline` – compact history view
- `git blame file` – show who changed each line and when

**Branches and synchronization:**
- `git branch` – list, create, or delete branches
- `git switch branch` – switch to another branch
- `git merge branch` – integrate changes from another branch
- `git rebase` – move commits to another base (linear history)
- `git pull` – fetch changes from remote and integrate them (fetch + merge)
- `git push` – send local commits to a remote
- `git fetch` – fetch changes from remote without integration

Typical workflow:

```bash
$ git switch -c feature-x

$ vim file.c

$ git add file.c
$ git commit -m "Implement feature X"

$ git push origin feature-x
```

Git commands work together to manage history and collaboration. Understanding the three states (modified, staged, committed) helps you understand what each command does.

## Sources

<!-- generated from frontmatter -->
