# Embedded Interview Lab migration batch 6

Work in `C:/Users/bogdan/Desktop/interview-qa`.

## Scope

Continue the exact source order in
`C:/Users/bogdan/Documents/Projects/learning/Embeddedinterviewlab/01_C_Cpp_Foundations/02_Pointers_Arrays_anki_cards.txt`.
Import source cards 81–100, exactly 20 records, as UK/EN pairs under
`content/{uk,en}/embedded`, continuing IDs `emb-cppfound-0081` through
`emb-cppfound-0100`. Confirm no overlap with actual repository files first.

## Requirements

- Read repository `AGENTS.md` and relevant shared rules before editing.
- Create exactly 20 Ukrainian and 20 English files, one pair per source card,
  with unique IDs and reciprocal `reconciled_with` values.
- Preserve source Front and Back meaning and order. Keep inline code and formulas
  inline. Preserve standalone code or formula material using the established HTML
  block style shared by site and Anki; do not flatten or drop markup.
- English body sections remain `TODO` during migration.
- No U+2014, U+2190, or U+2192; normalize only as required to U+2013 or ASCII
  `->`/`<-`.
- Follow established Lab citation, section, type, and naming conventions.
- Do not edit `meta/id-registry.csv`, taxonomy, PLAN, existing cards, or generated
  outputs. Do not commit or push.
- Run focused checks for exactly 20 pairs, ID uniqueness, source Front/Back parity,
  required sections by type, inline/block code and formula preservation, source
  order, and forbidden characters.
- Write evidence to `temp/agent-reports/lab-batch-6.md` and stop after this batch.
