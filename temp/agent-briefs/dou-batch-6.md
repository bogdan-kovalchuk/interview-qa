# DOU Embedded Interview migration batch 6

Work in `C:/Users/bogdan/Desktop/interview-qa`.

## Scope

Continue migrating `C:/Users/bogdan/Documents/Projects/learning/Embedded Interview`.
The previous DOU batch ended at Middle records 28–37. Inspect the actual source and
all existing cards, then import exactly the next 20 not-yet-represented source
records, preserving source order. They should be Middle records 38–57 unless the
actual files prove a different boundary. Confirm no overlap before editing.

## Requirements

- Read repository `AGENTS.md` and relevant shared rules before editing.
- Create exactly one UK and one EN Markdown file per selected record: 20 pairs,
  unique deterministic IDs, reciprocal `reconciled_with`.
- Preserve source Front and Back meaning and order. Keep inline code and formulas
  inline. Preserve standalone code/formula material with the established HTML block
  style shared by site and Anki; do not flatten or drop markup.
- Use established DOU citation, section, type, naming and ID-prefix conventions.
  English body remains TODO during migration.
- Apply gates: no U+2014, U+2190, U+2192, or literal escape text. Normalize only
  as required to U+2013 or ASCII `->`/`<-`.
- Do not edit `meta/id-registry.csv`, taxonomy, PLAN, existing cards, or generated
  outputs. Do not commit or push.
- Run focused checks for exactly 20 pairs, ID uniqueness, source Front/Back parity,
  required sections, inline/block code and formula preservation, and forbidden
  characters.
- Write evidence to `temp/agent-reports/dou-batch-6.md` and stop after this batch.
