# Embedded Interview Lab migration batch 5

Work in `C:/Users/bogdan/Desktop/interview-qa`.

## Scope

Continue the exact source order in
`C:/Users/bogdan/Documents/Projects/learning/Embeddedinterviewlab/01_C_Cpp_Foundations/02_Pointers_Arrays_anki_cards.txt`.
Import source cards 61–80, exactly 20 records, as UK/EN pairs under
`content/{uk,en}/embedded`, continuing the established IDs
`emb-cppfound-0061` through `emb-cppfound-0080`. Confirm no overlap with actual
repository files before writing.

## Requirements

- Read repository `AGENTS.md` and relevant shared rules before editing.
- Create exactly 20 Ukrainian and 20 English Markdown files, one pair per source
  card, with reciprocal `reconciled_with` and unique IDs.
- Preserve source Front and Back meaning and source order. Keep inline code and
  inline formulas inline. Preserve standalone code/formula material as the
  established HTML block markup used by both site and Anki templates; do not
  flatten, omit, or turn it into accidental literal escape text.
- English body sections remain `TODO` during migration, as documented.
- Apply repository gates: no U+2014, U+2190, or U+2192. Normalize only as needed
  to U+2013 or ASCII `->`/`<-`.
- Follow the established Lab source citation and section/type mapping.
- Do not edit `meta/id-registry.csv`, taxonomy, PLAN, existing cards, or generated
  outputs. Do not commit or push.
- Run focused checks for 20 pairs, ID uniqueness, required sections by type,
  source Front/Back parity, inline/block code and formula preservation, source
  order, and forbidden characters.
- Write evidence to `temp/agent-reports/lab-batch-5.md` and stop after this batch.
