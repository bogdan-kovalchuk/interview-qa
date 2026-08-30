# DOU Embedded Interview migration batch 6 report

## Scope

Migrated exactly the next 20 source records after the previous batch boundary:

- Source: `C:/Users/bogdan/Documents/Projects/learning/Embedded Interview/Middle_front_anki_cards.txt`
- Selected records: Middle 38–57
- Previous batch boundary: Middle 28–37
- Overlap check: PASS; exact Front matching against pre-existing Ukrainian cards found 0 hits before considering the 20 new files

## Imported records

| Source record | ID | Section | Type |
|---:|---|---|---|
| Middle 38 | `emb-fund-0010` | `fundamentals` | `concept` |
| Middle 39 | `emb-fund-0011` | `fundamentals` | `concept` |
| Middle 40 | `emb-periph-0009` | `peripherals-and-buses` | `concept` |
| Middle 41 | `emb-irq-0005` | `interrupts-and-timing` | `concept` |
| Middle 42 | `emb-periph-0010` | `peripherals-and-buses` | `concept` |
| Middle 43 | `emb-periph-0011` | `peripherals-and-buses` | `concept` |
| Middle 44 | `emb-periph-0012` | `peripherals-and-buses` | `concept` |
| Middle 45 | `emb-debug-0001` | `debugging-and-tracing` | `concept` |
| Middle 46 | `emb-debug-0002` | `debugging-and-tracing` | `concept` |
| Middle 47 | `emb-fund-0012` | `fundamentals` | `concept` |
| Middle 48 | `emb-fund-0013` | `fundamentals` | `concept` |
| Middle 49 | `emb-fund-0014` | `fundamentals` | `concept` |
| Middle 50 | `emb-rtos-0008` | `rtos` | `concept` |
| Middle 51 | `emb-fund-0015` | `fundamentals` | `concept` |
| Middle 52 | `emb-rtos-0009` | `rtos` | `concept` |
| Middle 53 | `emb-fund-0016` | `fundamentals` | `concept` |
| Middle 54 | `emb-rtos-0010` | `rtos` | `concept` |
| Middle 55 | `emb-irq-0006` | `interrupts-and-timing` | `concept` |
| Middle 56 | `emb-build-0014` | `toolchain-and-build` | `concept` |
| Middle 57 | `emb-build-0015` | `toolchain-and-build` | `concept` |

## Counts and focused checks

- Files: 40 total, exactly 20 Ukrainian and 20 English files: PASS.
- Language pairing and reciprocal `reconciled_with`: PASS, 20/20 pairs.
- IDs: unique across the batch, 20/20; section prefixes follow existing conventions.
- Source Front parity: PASS, 20/20.
- Source Back parity and order: PASS, 20/20. Source em dashes were normalized to repository-required en dashes.
- Required sections (`Short answer`, `Detailed explanation`, `Sources`): PASS, 40/40.
- English `Short answer` and `Detailed explanation` remain `TODO`: PASS, 20/20.
- Inline HTML/code markup preservation: PASS, 20/20 Ukrainian source answers.
- Forbidden U+2014, U+2190, U+2192, and literal escape text: PASS, 40/40 files.
- `git diff --check`: PASS.

## Full validator

`python -m iqa validate` exited 1 on the existing checkout with 2573 blocking failures and 41 warnings. The blocking failures include the embedded corpus IDs being absent from `meta/id-registry.csv`; the brief explicitly prohibited editing that registry. The validator also reports the repository's pre-existing short-answer length warnings. This full-repository result is separate from the focused batch gates above.

## Protected scope

The registry, taxonomy, `PLAN.md`, existing cards, and generated outputs were not edited. No commit or push was performed. Batch complete; stopped after Middle records 38–57.
