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
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for toolchain and build concepts; details of specific devices and toolchains can differ."
  - source_id: git-scm-doc
    title: "Git documentation"
    url: "https://git-scm.com/doc"
    accessed: 2026-09-08
    kind: official
    version: "current"
    applicability: "Official Git reference for version control concepts; specific workflows may vary by Git version."
---

## Short answer

`git merge` combines two branches while preserving their history; if the histories have diverged, Git creates a merge commit.[^dou-embedded-interview] Plus: it honestly shows when and where branches were merged; minus: the history can become branched.

`git rebase` moves the current branch's commits on top of another base, as if work had started from a newer commit. Plus: a linear and cleaner history; minus: rebase rewrites commit hashes.

A practical rule: **merge** is safe for shared/published branches; **rebase** is convenient for a local feature branch before merging, but you should not rebase someone else's published history without agreement.

## Detailed explanation

`git merge` and `git rebase` are two ways to integrate changes from one branch into another, but they work differently and produce different history shapes.[^git-scm-doc]

**git merge** creates a new merge commit that has two parents: the current HEAD branch and the branch being merged. This preserves the exact development history – you can see when branches diverged and when they came back together. Merge does not rewrite existing commits, so it is safe for published branches.

**git rebase** takes the commits from the current branch and "replays" them on top of another base. The result is a linear history without merge commits. But rebase creates new commits with new hashes, so the old commits disappear from the history.

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

Rebase is convenient for cleaning up local history before merging: you can combine commits (`squash`), reorder them, or edit commit messages via `git rebase -i` (interactive rebase).


## Comparison

| Criteria | git merge | git rebase |
|---|---|---|
| History shape | Branched with merge commit | Linear without merge commit |
| Rewrites commits | No | Yes (new hashes) |
| Safe for published branches | Yes | No (local only) |
| Conflict resolution | Once at merge time | Per commit separately |
| Revert | Easy (`git revert merge-commit`) | Harder (need old hashes) |

## When to choose which

**Choose merge** when:
- The branch is published and used by other developers
- You need to preserve the exact development history
- Working in a large team with parallel development

**Choose rebase** when:
- You need to clean up local history before merging (squash, reorder, edit)
- The feature branch is not yet published
- You want a linear history without merge commits
- Preparing commits for code review (each commit is a logical change)

**Golden rule**: never rebase published branches that other people use. Rebase rewrites history, and if someone has already pulled the old commits, conflicts will arise on the next push.


## Sources

<!-- generated from frontmatter -->
