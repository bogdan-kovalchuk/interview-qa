# DOU Embedded Interview migration batch 4 report

## Scope

Migrated exactly the next 10 source records after the previous batch, preserving the established global source order:

- Source: `C:/Users/bogdan/Documents/Projects/learning/Embedded Interview/Middle_front_anki_cards.txt`
- Selected records: Middle 18–27
- Previous batch boundary: Middle 8–17
- Overlap check: PASS; none of Middle 18–27 was represented before this batch

## Imported records

| Source record | ID | Section | Type |
|---:|---|---|---|
| Middle 18 | `emb-cemb-0035` | `c-in-embedded` | `concept` |
| Middle 19 | `emb-cemb-0036` | `c-in-embedded` | `pitfall` |
| Middle 20 | `emb-cemb-0037` | `c-in-embedded` | `concept` |
| Middle 21 | `emb-cemb-0038` | `c-in-embedded` | `concept` |
| Middle 22 | `emb-build-0011` | `toolchain-and-build` | `concept` |
| Middle 23 | `emb-build-0012` | `toolchain-and-build` | `concept` |
| Middle 24 | `emb-build-0013` | `toolchain-and-build` | `concept` |
| Middle 25 | `emb-cemb-0039` | `c-in-embedded` | `concept` |
| Middle 26 | `emb-cemb-0040` | `c-in-embedded` | `concept` |
| Middle 27 | `emb-memlink-0015` | `memory-and-linker` | `concept` |

## Counts

- Cards: 10
- Files: 20
- Ukrainian files: 10
- English files: 10
- Reciprocal language pairs: 10/10
- Registry entries added: 0, as required
- Existing questions edited: 0

## Focused checks

- Exactly 10 selected records and 10 UK/EN pairs: PASS.
- Source order and no overlap with existing cards: PASS.
- Question IDs unique among UK questions and paired one-to-one with EN files: PASS.
- Reciprocal `reconciled_with` values: PASS, 10/10.
- Required sections (`Short answer`, `Detailed explanation`, `Sources`): PASS, 20/20.
- English `Short answer` and `Detailed explanation` bodies are `TODO`: PASS, 10/10.
- Source Front preservation: PASS, 10/10.
- Source Back meaning and order preservation: PASS, 10/10 after required em-dash to en-dash normalization in Middle 19 and Middle 23.
- Inline code and span markup preservation: PASS, 10/10. No standalone code or formula blocks occurred in these source records, so no block conversion was required.
- Forbidden U+2014, U+2190, and U+2192: PASS, 20/20 files.
- UTF-8 report and content files: PASS.

## Repository validator

`python -m iqa validate` was run. It remains blocked by pre-existing checkout-wide baseline failures, including:

- `id-immutable`: the existing Embedded corpus, including these newly migrated IDs, is not present in `meta/id-registry.csv`.
- `sources`: the existing Embedded corpus requires at least one non-community source, while the DOU migration uses the established community source provenance.

These failures are outside this batch and were not changed because the brief explicitly forbids modifying `meta/id-registry.csv`, taxonomy, existing cards, or generated outputs.

## Files and protected scope

Only 20 new files under `content/uk/embedded/` and `content/en/embedded/` were added for this batch, plus this report. `meta/id-registry.csv`, taxonomy, generated outputs, existing cards, and the pre-existing `PLAN.md` modification were not changed by this batch.

No commit or push was performed. Batch complete; stopped after Middle records 18–27.
