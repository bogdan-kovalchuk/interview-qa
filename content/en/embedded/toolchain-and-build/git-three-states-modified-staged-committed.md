---
id: emb-build-0001
title: "What are the three main states in git?"
description: "A file in Git passes through three states – modified, staged, and committed – corresponding to the working directory, staging area, and local repository."
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

In the basic Git model, a file goes through three states:[^dou-embedded-interview]

- **Modified** – the file has been changed in the working directory but not yet added to the index.
- **Staged** – the changes have been added to the staging area with `git add`; they are ready to go into the next commit.
- **Committed** – the changes have been saved in the local repository as a commit.

Typical cycle: edit a file, then `git add file`, then `git commit -m "message"`.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
