# DOU Embedded Interview migration batch 3 report

Scope: exactly the next 10 not-yet-represented DOU source records after the previous batch.

## Source range

- Source: `C:/Users/bogdan/Documents/Projects/learning/Embedded Interview/Middle_front_anki_cards.txt`.
- Selected records: Middle 8–17, in source order.
- Junior records 76–83 and Middle records 6–7 were already represented by the previous batch.
- The selected records were checked against all existing `content/uk/embedded` and `content/en/embedded` cards before creation.

## Imported IDs

1. `emb-memlink-0012` – Middle 8
2. `emb-memlink-0013` – Middle 9
3. `emb-memlink-0014` – Middle 10
4. `emb-cemb-0031` – Middle 11
5. `emb-build-0008` – Middle 12
6. `emb-build-0009` – Middle 13
7. `emb-build-0010` – Middle 14
8. `emb-cemb-0032` – Middle 15
9. `emb-cemb-0033` – Middle 16
10. `emb-cemb-0034` – Middle 17

## Counts

- Cards: 10
- Files: 20
- Ukrainian files: 10
- English files: 10
- Matching UK/EN pairs: 10
- Registry entries added: 0
- Existing questions edited: 0

## Focused checks

- Exactly 10 selected records and 10 UK/EN pairs: PASS.
- Unique IDs and no collisions with existing IDs: PASS.
- Reciprocal `reconciled_with` values: PASS, 10/10.
- Required sections (`Short answer`, `Detailed explanation`, `Sources`): PASS, 20/20 files.
- English `Short answer` and `Detailed explanation` bodies are `TODO`: PASS, 10/10.
- Ukrainian source Front preservation: PASS, 10/10 after required typography normalization.
- Ukrainian source Back preservation and source order: PASS, 10/10; citation token appended using the established DOU convention.
- Inline code markup preservation: PASS, 10/10.
- Forbidden U+2014, U+2190, U+2192, and literal backslash-n: PASS, 20/20 files.

## Judgment calls

- Source tags were mapped with the established migration mapping: `Concept` to `concept`, `Trap` to `pitfall`.
- Sections and ID prefixes follow existing DOU conventions: allocator and storage topics to `memory-and-linker`, C language topics to `c-in-embedded`, and build topics to `toolchain-and-build`.
- Source answer text was retained. Only repository-required typography normalization was applied where needed: em dash to en dash and arrows to ASCII `->` or `<-`.
- No taxonomy, plan, validator, generated output, existing question, or `meta/id-registry.csv` file was changed.

No commit or push was performed. Batch complete; stopped after Middle records 8–17.
