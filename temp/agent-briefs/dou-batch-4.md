# DOU Embedded Interview migration batch 4

Work in `C:/Users/bogdan/Desktop/interview-qa`.

## Scope

Continue migrating source cards from
`C:/Users/bogdan/Documents/Projects/learning/Embedded Interview`.
Inspect the actual source files and existing repository cards. Select exactly the
next 10 source records not yet represented, preserving the established global
source order. The previous DOU batch ended at Middle records 8–17; determine the
next records from the actual files and confirm no overlap before writing.

## Requirements

- Read repository `AGENTS.md` and relevant shared rules before editing.
- Create exactly one UK and one EN Markdown file per selected record, with unique
  deterministic IDs and reciprocal `reconciled_with` values.
- Preserve source Front and Back meaning and order. Keep inline code and formulas
  inline; preserve standalone code/formula material using the established HTML
  block style shared by site and Anki. Do not flatten or drop markup.
- Use the established DOU citation, section, type, and ID-prefix conventions.
  English body sections remain `TODO` during migration.
- No U+2014, U+2190, or U+2192; normalize only as required to U+2013 or ASCII
  `->`/`<-`.
- Do not change `meta/id-registry.csv`, taxonomy, PLAN, existing cards, or
  generated outputs. Do not commit or push.
- Run focused checks for exactly 10 pairs, ID uniqueness, source parity,
  required sections by type, inline/block code and formula preservation, and
  forbidden characters.
- Write evidence to `temp/agent-reports/dou-batch-4.md` and stop after this batch.
