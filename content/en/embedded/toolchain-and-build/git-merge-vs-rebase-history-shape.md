---
id: emb-build-0007
title: "What is the difference between merge and rebase?"
description: "git merge preserves branch history with a merge commit, while git rebase rewrites commits onto a new base for a linear history."
track: embedded
section: toolchain-and-build
level: junior
type: comparison
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

`git merge` combines two branches while preserving their history; if the histories have diverged, Git creates a merge commit.[^dou-embedded-interview] Plus: it honestly shows when and where branches were merged; minus: the history can become branched.

`git rebase` moves the current branch's commits on top of another base, as if work had started from a newer commit. Plus: a linear and cleaner history; minus: rebase rewrites commit hashes.

A practical rule: **merge** is safe for shared/published branches; **rebase** is convenient for a local feature branch before merging, but you should not rebase someone else's published history without agreement.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
