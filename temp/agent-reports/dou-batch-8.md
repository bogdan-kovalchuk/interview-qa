# DOU Embedded Interview migration batch 8 report

## Scope

Migrated exactly the next 20 source records in source order: Senior 8–27 from `Senior_front_anki_cards.txt`.

- Source: `C:/Users/bogdan/Documents/Projects/learning/Embedded Interview`
- Pre-edit overlap check: PASS; the selected Front values were not represented by existing Ukrainian cards.
- New files: 20 Ukrainian and 20 English files, one reciprocal pair per record.

## Imported records

| Source records | Sections | IDs |
|---|---|---|
| Senior 8–10 | testing-embedded | emb-testemb-0006–0008 |
| Senior 11–12, 27 | fundamentals | emb-fund-0020–0022 |
| Senior 13–16, 24–26 | toolchain-and-build | emb-build-0018–0024 |
| Senior 17–21 | interrupts-and-timing | emb-irq-0007–0011 |
| Senior 22–23 | data-types-and-memory-layout | emb-dtypes-0103–0104 |

## Focused checks

- Exactly 20 selected records: PASS.
- Exactly 20 Ukrainian and 20 English files: PASS.
- Unique IDs and reciprocal language pairs: PASS, 20/20.
- Source Front parity: PASS, 20/20.
- Source Back parity and order: PASS, 20/20; the DOU citation token was appended to each Ukrainian short answer.
- Required sections (`Short answer`, `Detailed explanation`, `Evaluation guide`, `Sources`): PASS.
- English `Short answer` and `Detailed explanation` remain `TODO`: PASS, 20/20.
- Inline HTML/code markup was preserved from the source Back fields.
- Forbidden U+2014, U+2190, U+2192, and literal escape text: PASS, 40/40.
- UTF-8 decoding: PASS.
- `git diff --check`: PASS.

## Repository-wide validation

`python -m iqa validate` was attempted. It reached the validator but the console failed with a Windows cp1252 `UnicodeEncodeError` while printing existing diagnostics. The repository baseline also contains the known registry mismatch for migrated embedded IDs; `meta/id-registry.csv` was not edited because the brief prohibited it.

## Protected scope

No `meta/id-registry.csv`, taxonomy, `PLAN.md`, existing cards, or generated outputs were edited. No commit or push was performed. Batch 8 is complete; stopped after Senior 8–27.
