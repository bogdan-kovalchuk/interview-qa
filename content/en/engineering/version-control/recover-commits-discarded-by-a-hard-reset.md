---
id: eng-vcs-0001
title: "Recover two commits that a hard reset removed from the branch"
description: "The commits are still in the object database; the reflog is what still names them."
track: engineering
section: version-control
level: middle
type: practical
tags: [git, reflog, reset, recovery, object-database]
status: published
updated: 2026-09-03
content_revision: 2
reconciled_with:
  uk: 2
execution:
  language: shell
  standard: null
  toolchain:
    name: git
    version: "2.52.0"
  flags: []
applies_to:
  - product: Git
    version: "2.52"
anki:
  export: true
sources:
  - source_id: git-reflog-docs
    title: "git-reflog documentation"
    url: https://git-scm.com/docs/git-reflog
    accessed: 2026-09-03
    kind: official
    version: "2.52"
    applicability: "Reflog contents, the ref@{n} syntax and expiry subcommands; the reflog is local to a repository and is never transferred by push or fetch."
  - source_id: git-reset-docs
    title: "git-reset documentation"
    url: https://git-scm.com/docs/git-reset
    accessed: 2026-09-03
    kind: official
    version: "2.52"
    applicability: "What --soft, --mixed and --hard each change, and which of them discards working tree content."
  - source_id: git-config-gc-reflog
    title: "git-config documentation: gc.reflogExpire and gc.reflogExpireUnreachable"
    url: https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcreflogExpire
    accessed: 2026-09-03
    kind: official
    version: "2.52"
    applicability: "Default reflog retention of 90 days, and 30 days for entries unreachable from the current tip."
---

## Short answer

**`git reset --hard` moves the branch pointer; it does not delete the commits.** They stay in the
object database, unreachable but still named by the reflog, so recovery is a lookup rather than a
repair.[^git-reflog-docs] Read `git reflog` to find the hash the branch pointed at before the reset,
then create a branch at that hash instead of resetting again, so the recovery is itself reversible. <span class="warn">Work that was never committed is a different matter: unstaged
changes were never objects, and staged ones survive only as dangling blobs.</span>[^git-reset-docs]

## Detailed explanation

Two separate things happen in a hard reset, and only one of them is reversible. The branch ref is
rewritten to the target commit, which is bookkeeping and undoable. The working tree and index are
overwritten to match, which destroys anything that was never committed.[^git-reset-docs] The panic
usually concerns the commits, and those are the recoverable half.

Commits are content-addressed objects. Nothing about a commit changes when a branch stops pointing at
it; it simply becomes unreachable, and unreachable objects survive until garbage collection removes
them. What keeps them from being collected in the meantime is the reflog: every update of `HEAD` and
of each branch tip is recorded there with its previous value, so the pre-reset hash is written down
even though no branch names it.[^git-reflog-docs]

That gives the recovery its shape. Find the hash, verify it is the right one, then make it reachable
again. Prefer creating a new branch over moving the current one: it is additive, so if the hash turns
out to be wrong nothing further is lost, and the two states can be compared side by side.

There is a deadline. Reflog entries expire, by default after 90 days, and after 30 days for entries
unreachable from the current tip, after which garbage collection may remove the objects for
real.[^git-config-gc-reflog] The reflog is also strictly local: it is not pushed, not fetched, and not
present in a fresh clone, so a colleague's clone cannot supply your reflog entry, although a stale
remote-tracking ref or an open pull request may still name the same commit.

## Environment

- A local Git repository, Git 2.52 or newer, on any platform. The measured run was Git 2.52.0 on
  Windows.
- A branch with at least three commits, the last two of which exist only locally and have not been
  pushed.
- No garbage collection has been run since the reset, and the repository has default expiry settings.
- Shell access only; no hosting provider, GUI or IDE feature may be used.

Set up the starting state with:

```sh
git init recover-demo && cd recover-demo
printf 'a\n' > f && git add f && git commit -m first
printf 'b\n' >> f && git commit -am second
printf 'c\n' >> f && git commit -am third
git reset --hard HEAD~2
```

## Deliverable

A short shell transcript, suitable for a team runbook, that:

1. Establishes what the branch pointed at before the reset, without guessing the hash.
2. Restores the two lost commits onto a branch, with their original hashes, authorship and dates
   unchanged.
3. Leaves the post-reset state also available for comparison, so the recovery itself is reversible.
4. States in one line why the same procedure would not recover uncommitted changes.

A worked answer:

```sh
git reflog                                  # find the pre-reset hash of HEAD
git branch rescue 58fd2a2                   # make it reachable again, additively
git log --oneline rescue                    # verify: third, second, first
git diff HEAD rescue                        # confirm what the reset removed
git switch rescue                           # adopt the recovered state when satisfied
```

`git reset --hard HEAD@{1}` reaches the same commit in one step and is the common shortcut, but it
moves the current branch, so a wrong guess needs a second recovery. The additive form is the one to
put in a runbook.

## Acceptance criteria

- `git log --oneline rescue` lists all three commits, and `git rev-parse rescue` equals the hash the
  reflog recorded before the reset.
- The recovered commit hashes are identical to the originals, which also confirms authorship, dates
  and message are unchanged; a solution that recreates equivalent commits with new hashes does not
  pass.
- The branch that was reset still points at its post-reset commit, so both states exist.
- The hash was obtained from the reflog or from an equivalent record in the transcript, not typed from
  memory or from scrollback.
- No `git gc`, `git prune` or `--prune=now` appears anywhere in the transcript.
- The transcript states that changes which were never committed are not recoverable this way, and, if
  they were staged, points at `git fsck --lost-found` as a partial recovery.

## Evaluation guide

### Expected signals

- Distinguishes committed work, which is recoverable, from uncommitted work, which is not.
- Knows the commits are unreachable rather than deleted, and names the reflog as what still refers to
  them.
- Recovers by creating a branch or tag at the hash instead of another `reset --hard`.
- Knows the reflog is local and time-limited, so recovery is not indefinitely available.

### Red flags

- Reaches for `git pull` or a fresh clone as the recovery method, which would only work if the commits
  had been pushed.
- Believes `git reset --hard` is unrecoverable and advises rewriting the work by hand.
- Cannot say why a fresh clone has no reflog.
- Runs `git gc --prune=now` while diagnosing.

### Level-up follow-up

Ask how they would recover a change that was staged with `git add` and then destroyed by
`reset --hard` before any commit existed. The strong answer knows the blob was written to the object
database by `git add` and can be found among dangling objects with `git fsck --lost-found`, and that
this is a per-file recovery with no commit message, tree or ordering.

## Sources

<!-- generated from frontmatter -->
