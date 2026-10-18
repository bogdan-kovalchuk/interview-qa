---
id: emb-build-0003
title: "What is an interactive rebase?"
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

`git rebase -i` edits commit history before a chosen base.[^dou-embedded-interview] It opens a list of commits where you set an action for each one.

Actions: `pick` – keep the commit; `reword` – change the message; `squash`/`fixup` – combine commits; `edit` – stop to amend; `drop` – remove; commits can also be reordered.

Use it to clean up a local feature branch before a pull request, combine fixup commits or fix a message. It <span class="warn">rewrites history</span>, so be careful with commits already pushed and used by others.

## Detailed explanation

**Interactive rebase** (`git rebase -i`) is a mode for editing commit history that lets you change, combine, rename, or drop commits in a local branch before sharing it with others.[^git-scm-doc]

When you run `git rebase -i HEAD~N` (where N is the number of commits), Git opens a text editor with a list of commits and available actions:

```
pick abc1234 Add initial implementation
pick def5678 Fix typo in comment
pick ghi9012 Add missing error handling
```

**Available actions:**
- `pick` – keep the commit unchanged
- `reword` – change the commit message
- `squash` – combine with the previous commit (both messages)
- `fixup` – combine with the previous commit (only changes, message is discarded)
- `edit` – stop to edit files and amend the commit
- `drop` – remove the commit
- You can also reorder commits by rearranging the lines

**Typical usage:**

```bash
$ git rebase -i HEAD~5

$ git commit --fixup=abc1234
$ git rebase -i --autosquash abc1234~1
```

Interactive rebase is useful for:
- Combining small commits into logical changes (squash/fixup)
- Fixing commit messages (reword)
- Removing temporary or experimental commits (drop)
- Reordering commits for better history readability

**Important:** interactive rebase rewrites history by changing commit hashes. This is safe only for local commits that have not been pushed to a remote. If you have already pushed commits, rebase will create conflicts for other developers working with that branch.

If you need to update the remote after rebase, use `git push --force-with-lease` (a safer option than `--force` because it checks that the remote branch has not changed).

To undo a rebase, you can use `git reflog` to find the previous HEAD and `git reset --hard HEAD@{N}` to roll back.
