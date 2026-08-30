# Repair report: Embedded Interview Lab card 32

## Scope

- Source: `C:/Users/bogdan/Documents/Projects/learning/Embeddedinterviewlab/01_C_Cpp_Foundations/02_Pointers_Arrays_anki_cards.txt`
- Source order: zero-based order `32`, between migrated cards `emb-cppfound-0031` and `emb-cppfound-0033`.
- Imported ID: `emb-cppfound-0032`.
- Source tags: `Code Pointers C`.
- Source punctuation U+2014 was normalized to U+2013 to satisfy the repository gate.

## Files added

- `content/uk/embedded/c-in-embedded/pointer-subtraction-counts-elements.md`
- `content/en/embedded/c-in-embedded/pointer-subtraction-counts-elements.md`

The Ukrainian file contains the source answer in `Short answer` plus the citation suffix used by adjacent migrated cards. The English body remains `TODO` for migration. Both files use the same deterministic slug and ID.

## Focused checks

All focused checks passed:

- UK/EN pair structure and deterministic filenames.
- Unique `emb-cppfound-0032` ID and reciprocal language reconciliation.
- Source Front/Back parity after the required U+2014 to U+2013 normalization and citation suffix.
- Standalone code block markup and `%td` / `ptrdiff_t` formula content.
- No U+2014, U+2190, or U+2192 in either new file.
- `git diff --check` reported no whitespace errors for the target files.

## Repository-wide validator

`python -m iqa validate` was run. It remains non-zero with `1745 blocking failure(s)` and `37 warning(s)`. The output includes the repository-wide existing missing-`id-registry.csv` and source-gate failures across the Embedded content set, including the newly added ID. The task explicitly forbids changing the registry or other existing/generated files, so those baseline failures were not altered.

No commit or push was performed.
