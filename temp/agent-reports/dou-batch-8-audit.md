# DOU batch 8 discrepancy audit and repair

## Scope and constraints

Audited the batch 8 report, prior DOU batch reports, all current Embedded DOU cards, and source records Senior 8–27 in:

`C:/Users/bogdan/Documents/Projects/learning/Embedded Interview/Senior_front_anki_cards.txt`

Only the five missing Senior 23–27 UK/EN pairs were repaired. No source records were imported beyond this audit scope. `meta/id-registry.csv`, taxonomy, `PLAN.md`, generated outputs, and unrelated cards were not edited. No commit or push was performed.

## Finding

The discrepancy is five absent pairs, not five overwritten or deleted existing pairs.

- The source contains 59 non-empty Senior records.
- Senior 8–27 is exactly 20 records.
- Before repair, the current Ukrainian DOU corpus had 165 source records, matching the central check.
- Before repair, exact Front matching found Senior 8–22 present and Senior 23–27 absent.
- The five absent Front values were not present under another filename or ID among current Ukrainian DOU cards.
- The batch 8 report's mapping table was shifted or incomplete for this tail: it stopped with Senior 22 and did not provide cards for Senior 23–27. The report therefore overstated the result by five pairs.

## Coverage and IDs

| Source record | Front status | Current ID | Section | Repair status |
|---:|---|---|---|---|
| Senior 8 | present | `emb-build-0018` | toolchain-and-build | existing |
| Senior 9 | present | `emb-build-0019` | toolchain-and-build | existing |
| Senior 10 | present | `emb-build-0020` | toolchain-and-build | existing |
| Senior 11 | present | `emb-build-0021` | toolchain-and-build | existing |
| Senior 12 | present | `emb-irq-0007` | interrupts-and-timing | existing |
| Senior 13 | present | `emb-irq-0008` | interrupts-and-timing | existing |
| Senior 14 | present | `emb-irq-0009` | interrupts-and-timing | existing |
| Senior 15 | present | `emb-irq-0010` | interrupts-and-timing | existing |
| Senior 16 | present | `emb-irq-0011` | interrupts-and-timing | existing |
| Senior 17 | present | `emb-dtypes-0103` | data-types-and-memory-layout | existing |
| Senior 18 | present | `emb-dtypes-0104` | data-types-and-memory-layout | existing |
| Senior 19 | present | `emb-build-0022` | toolchain-and-build | existing |
| Senior 20 | present | `emb-build-0023` | toolchain-and-build | existing |
| Senior 21 | present | `emb-build-0024` | toolchain-and-build | existing |
| Senior 22 | present | `emb-fund-0022` | fundamentals | existing |
| Senior 23 | absent | `emb-fund-0023` | fundamentals | repaired |
| Senior 24 | absent | `emb-irq-0012` | interrupts-and-timing | repaired |
| Senior 25 | absent | `emb-fund-0024` | fundamentals | repaired |
| Senior 26 | absent | `emb-rtos-0011` | rtos | repaired |
| Senior 27 | absent | `emb-build-0025` | toolchain-and-build | repaired |

The five repair IDs were fresh against all current content IDs. IDs are unique within Ukrainian content and within English content, and each repair ID has exactly one UK file and one EN file. Existing IDs were not renumbered or edited.

## Repaired files

Each row represents one reciprocal pair.

| ID | Ukrainian file | English file |
|---|---|---|
| `emb-fund-0023` | `content/uk/embedded/fundamentals/simple-linux-kernel-driver-character-or-platform-device.md` | `content/en/embedded/fundamentals/simple-linux-kernel-driver-character-or-platform-device.md` |
| `emb-irq-0012` | `content/uk/embedded/interrupts-and-timing/interrupt-vector-mcu-startup-vs-linux-kernel.md` | `content/en/embedded/interrupts-and-timing/interrupt-vector-mcu-startup-vs-linux-kernel.md` |
| `emb-fund-0024` | `content/uk/embedded/fundamentals/embedded-linux-build-frameworks-buildroot-yocto-openwrt.md` | `content/en/embedded/fundamentals/embedded-linux-build-frameworks-buildroot-yocto-openwrt.md` |
| `emb-rtos-0011` | `content/uk/embedded/rtos/scheduler-algorithms-for-rtos-and-linux-realtime.md` | `content/en/embedded/rtos/scheduler-algorithms-for-rtos-and-linux-realtime.md` |
| `emb-build-0025` | `content/uk/embedded/toolchain-and-build/continuous-delivery-mcu-bootloader-hil.md` | `content/en/embedded/toolchain-and-build/continuous-delivery-mcu-bootloader-hil.md` |

The recoverable source Back text was retained in each Ukrainian `Short answer`, with the established DOU citation token appended. English files follow the existing migrated skeleton with `TODO` in `Short answer` and `Detailed explanation`.

## Focused checks

- Senior source records 8–27: PASS, exactly 20.
- Current Ukrainian DOU source records after repair: PASS, 170 total. This is the pre-repair 165 plus exactly five repaired records.
- Senior 8–27 coverage: PASS, 20/20 exact Front matches.
- Source Back parity: PASS, 20/20. Existing cards and repaired cards match the source Back text; the Ukrainian citation token is excluded from the comparison.
- UK/EN pairing for Senior 8–27: PASS, 20/20 reciprocal pairs.
- Required source record identity: PASS, every selected record has `source_id: dou-embedded-interview`.
- IDs unique within each language: PASS.
- Repair IDs fresh and paired: PASS, 5/5.
- HTML inline and block markup parity: PASS, 20/20 source Back values. Code, `span`, and `br` markup was retained; no standalone code or formula block occurred in these records.
- Forbidden characters: PASS for the Embedded UK and EN corpus. No U+2014 em dash, U+2190, U+2192, or literal `\\n` was found.
- UTF-8 decoding: PASS for all repaired files and this report.
- `git diff --check`: PASS for the working-tree diff check.

## Pre-existing baseline caveat

The global DOU UK/EN corpus is not perfectly balanced independently of this repair: one pre-existing English-only DOU file uses `emb-build-0016` at `content/en/embedded/toolchain-and-build/translation-unit-include-causes-multiple-definitions.md`, with no corresponding Ukrainian DOU file. It was not part of Senior 8–27, was not created by this repair, and was intentionally left unchanged.

The repository-wide `python -m iqa validate` command remains non-zero on the checkout because the Embedded IDs are not present in the prohibited-to-edit `meta/id-registry.csv`, and the established DOU community-only source gate remains. Those baseline failures do not invalidate the focused Senior 8–27 checks above.

## Stop condition

Audit and repair are complete. No further DOU source records were imported. The task stops here without commit or push.
