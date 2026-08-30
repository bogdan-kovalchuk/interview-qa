# DOU Embedded Interview migration batch 3

Work in `C:/Users/bogdan/Desktop/interview-qa`.

## Scope

Continue migrating source cards from
`C:/Users/bogdan/Documents/Projects/learning/Embedded Interview`.
Inspect the source files and all existing `content/uk/embedded` and
`content/en/embedded` cards. Select exactly the next 10 source records not yet
represented in the repository, preserving the established global source order
across the DOU Junior, Middle, and Senior files. Do not duplicate any existing
question. The previous DOU batch ended at Junior records 76–83 and Middle records
6–7; determine the next records from the actual files and existing content.

## Requirements

- Read repository `AGENTS.md` and the relevant shared rules before editing.
- Create exactly one UK and one EN Markdown file per selected record, with unique
  deterministic IDs and reciprocal `reconciled_with` values.
- Preserve source Front and Back meaning and order. Keep inline code/formulas inline;
  render standalone code or formula material using the established HTML block style
  shared by the site and Anki note type. Do not flatten or drop markup.
- Use the established DOU source citation and migration conventions. English body
  sections remain `TODO` during migration.
- Apply repository gates: no U+2014, U+2190, or U+2192; use U+2013 or ASCII `->`/`<-`
  where needed.
- Do not change `meta/id-registry.csv`, taxonomy, PLAN, existing cards, or generated
  outputs. Do not commit or push.
- Run focused checks for exactly 10 pairs, no ID collisions, source Front/Back
  preservation, required sections by card type, inline/block code and formula
  preservation, and forbidden characters.
- Write an evidence report to `temp/agent-reports/dou-batch-3.md` and stop after this
  batch.
