# DOU Embedded Interview migration batch 7 report

## Scope

Migrated exactly 20 not-yet-represented source records in source order:

- Source: C:/Users/bogdan/Documents/Projects/learning/Embedded Interview
- Middle_front_anki_cards.txt: records 58–70, physical source lines 63–75
- Senior_front_anki_cards.txt: records 1–7, physical source lines 6–12
- Pre-edit overlap check: PASS; the 20 selected Front values were absent from the existing Ukrainian cards

## Imported records

| Source record | ID | Section | Type |
|---|---|---|---|
| Middle 58 | emb-fund-0017 | fundamentals | concept |
| Middle 59 | emb-build-0017 | toolchain-and-build | pitfall |
| Middle 60 | emb-conn-0001 | connectivity | concept |
| Middle 61 | emb-conn-0002 | connectivity | concept |
| Middle 62 | emb-conn-0003 | connectivity | concept |
| Middle 63 | emb-safety-0002 | safety-and-standards | concept |
| Middle 64 | emb-conn-0004 | connectivity | concept |
| Middle 65 | emb-hwbasic-0003 | hardware-basics | pitfall |
| Middle 66 | emb-periph-0013 | peripherals-and-buses | pitfall |
| Middle 67 | emb-periph-0014 | peripherals-and-buses | pitfall |
| Middle 68 | emb-periph-0015 | peripherals-and-buses | concept |
| Middle 69 | emb-debug-0003 | debugging-and-tracing | concept |
| Middle 70 | emb-hwbasic-0004 | hardware-basics | concept |
| Senior 1 | emb-testemb-0001 | testing-embedded | concept |
| Senior 2 | emb-testemb-0002 | testing-embedded | concept |
| Senior 3 | emb-testemb-0003 | testing-embedded | concept |
| Senior 4 | emb-testemb-0004 | testing-embedded | concept |
| Senior 5 | emb-testemb-0005 | testing-embedded | concept |
| Senior 6 | emb-fund-0018 | fundamentals | concept |
| Senior 7 | emb-fund-0019 | fundamentals | concept |

## Focused checks

- Exactly 20 selected records: PASS.
- Exactly 20 Ukrainian and 20 English files: PASS.
- Unique IDs across the batch and reciprocal UK/EN pairing: PASS, 20/20.
- Source Front parity: PASS, 20/20. Required repository en dash normalization was applied.
- Source Back parity and order: PASS, 20/20. Required repository en dash normalization was applied.
- Required section sequence (Short answer, Detailed explanation, Evaluation guide, Sources): PASS, 40/40.
- English Short answer and Detailed explanation remain TODO: PASS, 20/20.
- DOU citation token in Ukrainian short answers: PASS, 20/20.
- Inline HTML/code markup preservation: PASS, 20/20.
- Standalone source code or formula blocks: none in this batch.
- Forbidden U+2014, U+2190, U+2192, and literal escape text: PASS, 40/40.
- UTF-8 decoding: PASS, all 40 new files and this report.
- git diff --check: PASS for tracked diff output.

## Repository-wide validation

python -m iqa validate exited 1 with the existing checkout-wide baseline failures, including missing embedded IDs in meta/id-registry.csv and the established community-only DOU source gate. The brief prohibited changing the registry or adding authoritative sources, so this result was not used as a batch failure.

## Protected scope

No registry, taxonomy, PLAN.md, generated output, or intended pre-existing question content was changed. No commit or push was performed. Batch 7 is complete; stopped after Middle 58–70 and Senior 1–7.
