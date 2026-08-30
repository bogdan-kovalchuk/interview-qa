# DOU Embedded Interview migration batch 5 report

## Scope

Migrated exactly the next 10 source records after the previous batch, preserving the established source order:

- Source: `C:/Users/bogdan/Documents/Projects/learning/Embedded Interview/Middle_front_anki_cards.txt`
- Selected records: Middle 28–37
- Previous batch boundary: Middle 18–27
- Overlap check: PASS; none of Middle 28–37 was represented by the existing question IDs before this batch

## Imported records

| Source record | ID | Section | Type |
|---:|---|---|---|
| Middle 28 | `emb-memlink-0016` | `memory-and-linker` | `pitfall` |
| Middle 29 | `emb-boot-0004` | `bootloaders-and-ota` | `concept` |
| Middle 30 | `emb-irq-0004` | `interrupts-and-timing` | `concept` |
| Middle 31 | `emb-safety-0001` | `safety-and-standards` | `concept` |
| Middle 32 | `emb-cemb-0041` | `c-in-embedded` | `concept` |
| Middle 33 | `emb-cemb-0042` | `c-in-embedded` | `concept` |
| Middle 34 | `emb-cemb-0043` | `c-in-embedded` | `concept` |
| Middle 35 | `emb-dtypes-0101` | `data-types-and-memory-layout` | `concept` |
| Middle 36 | `emb-dtypes-0102` | `data-types-and-memory-layout` | `pitfall` |
| Middle 37 | `emb-cppemb-0001` | `cpp-in-embedded` | `concept` |

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
- Question IDs unique and paired one-to-one across languages: PASS.
- IDs match established section prefixes and remain unique against the full embedded corpus: PASS.
- Reciprocal `reconciled_with` values: PASS, 10/10.
- Required DOU sections (`Short answer`, `Detailed explanation`, `Sources`): PASS, 20/20.
- English `Short answer` and `Detailed explanation` bodies are `TODO`: PASS, 10/10.
- Ukrainian source Front preservation: PASS, 10/10.
- Ukrainian source Back meaning and order preservation: PASS, 10/10. Source U+2014 was normalized to the repository-required U+2013 where present.
- Source citation token: PASS, 10/10.
- Inline code and span markup preservation: PASS, 10/10.
- Forbidden U+2014, U+2190, U+2192, and literal escape text: PASS, 20/20 files.
- UTF-8 decoding of all new content files: PASS.

## Protected scope

Only the 20 new question files under `content/uk/embedded/` and `content/en/embedded/`, plus this report, were written for this batch. `meta/id-registry.csv`, `meta/TAXONOMY.md`, `PLAN.md`, existing cards, and generated outputs were not edited.

No commit or push was performed. Batch complete; stopped after Middle records 28–37.
