---
id: emb-build-0003
title: "What is an interactive rebase?"
description: "git rebase -i opens a list of commits before a chosen base and lets you pick, reword, squash, edit, drop, or reorder each commit, rewriting history."
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

`git rebase -i` is a mode for editing commit history before a chosen base.[^dou-embedded-interview] It opens a list of commits where you can change the action for each one.

Typical actions: `pick` – keep the commit; `reword` – change the message; `squash`/`fixup` – combine commits; `edit` – stop to amend the commit; `drop` – remove the commit; you can also reorder commits.

Usage: clean up a local feature branch before a pull request, combine small fixup commits, fix a commit message. Important: this <span class="warn">rewrites history</span>, so be careful with commits that have already been pushed and are used by others.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
