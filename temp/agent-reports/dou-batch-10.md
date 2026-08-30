# DOU Embedded Interview migration batch 10 report

## Scope

Migrated exactly the next five source records in source order: Senior 33-37 from `Senior_front_anki_cards.txt`.

- Source: `C:/Users/bogdan/Documents/Projects/learning/Embedded Interview`
- Pre-edit overlap check: PASS; the five selected Front values were not represented by tracked Ukrainian cards.
- New files: five Ukrainian and five English files, one reciprocal pair per record.

## Imported records

| Source record | Section | Type | ID |
|---|---|---|---|
| Senior 33 | bootloaders-and-ota | concept | emb-boot-0005 |
| Senior 34 | peripherals-and-buses | concept | emb-periph-0018 |
| Senior 35 | connectivity | concept | emb-conn-0005 |
| Senior 36 | connectivity | concept | emb-conn-0006 |
| Senior 37 | connectivity | concept | emb-conn-0007 |

## Focused checks

- Exactly five selected source records: PASS.
- Exactly five UK and five EN files: PASS.
- IDs unique within the batch and globally unique in existing UK content: PASS.
- New IDs absent from the pre-edit registry snapshot: PASS.
- Reciprocal `reconciled_with` values and shared IDs: PASS, 5/5.
- Source Front parity: PASS, 5/5.
- Source Back parity and order: PASS, 5/5; the DOU citation token was appended to each Ukrainian short answer.
- Required sections (`Short answer`, `Detailed explanation`, `Evaluation guide`, `Sources`): PASS, 10/10.
- English short answer and detailed explanation remain `TODO`: PASS, 5/5.
- Established inline HTML markup was preserved; no standalone code or formula blocks were present in these source Backs.
- Forbidden U+2014, U+2190, U+2192, and literal escape text: PASS, 10/10.
- UTF-8 decoding: PASS.

## Repository-wide validation

`python -m iqa validate` was not run because the module is not installed in the current environment. The repository baseline also contains the known registry mismatch for migrated embedded IDs; `meta/id-registry.csv` was not edited because the brief prohibited it.

## Protected scope

No `meta/id-registry.csv`, taxonomy, `PLAN.md`, existing cards, or generated outputs were edited. No commit or push was performed. Batch 10 is complete; stopped after Senior 33-37.
