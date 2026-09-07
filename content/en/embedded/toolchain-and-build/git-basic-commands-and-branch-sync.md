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
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
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
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for toolchain and build concepts; details of specific devices and toolchains can differ."
---

## Short answer

Basic commands:[^dou-embedded-interview]

`git init` – create a repository; `git clone URL` – copy an existing one; `git status` – check the state; `git add` – add changes to the staging area; `git commit` – create a commit; `git log` – history; `git diff` – view differences.

Branches and synchronization: `git branch` – list/create branches; `git switch` or `git checkout` – switch to a branch; `git merge` – merge branches; `git rebase` – move commits to another base; `git pull` – fetch and integrate changes; `git push` – send commits to a remote.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
