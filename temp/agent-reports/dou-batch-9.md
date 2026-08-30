# DOU Embedded Interview migration batch 9 report

## Scope

Migrated exactly the next five source records in source order: Senior 28–32 from `Senior_front_anki_cards.txt`.

- Source: `C:/Users/bogdan/Documents/Projects/learning/Embedded Interview`
- Pre-edit overlap check: PASS; the five selected Front values were not represented by tracked Ukrainian cards.
- New files: five Ukrainian and five English files, one reciprocal pair per record.

## Imported records

| Source record | Section | Type | ID |
|---|---|---|---|
| Senior 28 | rtos | concept | emb-rtos-0012 |
| Senior 29 | rtos | concept | emb-rtos-0013 |
| Senior 30 | rtos | concept | emb-rtos-0014 |
| Senior 31 | peripherals-and-buses | concept | emb-periph-0016 |
| Senior 32 | peripherals-and-buses | pitfall | emb-periph-0017 |

## Focused checks

- Exactly five selected source records: PASS.
- Exactly five UK and five EN files: PASS.
- IDs unique within the batch and globally unique in existing UK content: PASS.
- New IDs absent from the pre-edit registry snapshot: PASS.
- Reciprocal `reconciled_with` values and shared IDs: PASS, 5/5.
- Source Front parity: PASS, 5/5.
- Source Back parity and order: PASS, 5/5; the DOU citation token was appended to each Ukrainian short answer.
- Required sections and section/type mapping: PASS, 10/10.
- English short answer and detailed explanation remain `TODO`: PASS, 5/5; the pitfall sections also remain `TODO`.
- Established inline HTML markup was preserved; no standalone code or formula blocks were present in these source Backs.
- Forbidden U+2014, U+2190, U+2192, and literal escape text: PASS, 10/10.
- UTF-8 decoding: PASS.
- `git diff --check`: PASS for the working tree diff; the new untracked files were additionally checked for trailing whitespace during focused review.

## Repository-wide validation

`python -m iqa validate` was run with UTF-8 console output. It reached the validator but failed on the pre-existing repository baseline: migrated embedded IDs are absent from `meta/id-registry.csv`, and embedded community-source cards lack a non-community source. The run also reported one unrelated pre-existing cross-reference error and warnings. No registry or source metadata was changed because the brief prohibited those edits.

## Protected scope

No `meta/id-registry.csv`, taxonomy, `PLAN.md`, existing cards, or generated outputs were edited. No commit or push was performed. Batch 9 is complete; stopped after Senior 28–32.
