# Bounded continuation: Embedded Interview Lab import, batch 3

Work in `C:\Users\bogdan\Desktop\interview-qa`.

Read `AGENTS.md`, `meta/QUESTIONS.md`, `meta/TAXONOMY.md`, `meta/ANKI.md`, `packaging/anki/notetype/front.html`, `packaging/anki/notetype/back.html`, and `packaging/anki/notetype/card.css`. Inspect at least five existing Lab-imported files, including one with code and one with mathematical notation if available.

Continue the Lab migration. Already imported: source file 01 cards 1–100 as `emb-dtypes-0001..0100`, and source file 02 cards 1–20 as `emb-cppfound-0001..0020`. Import exactly source file `02_Pointers_Arrays_anki_cards.txt` cards 21–40, no more and no fewer, into the existing `embedded/c-in-embedded` taxonomy section. Do not duplicate or edit existing files.

Create one Ukrainian and one English file per card. Preserve the Ukrainian source Front as the question and source Back as the Ukrainian Short answer with only the established repository formatting normalization. English title/description may be translated, but every English body section remains `TODO`; Ukrainian Detailed explanation and all other unwritten sections remain `TODO`.

Formatting is a hard requirement: preserve inline code as inline code; preserve fenced or standalone code blocks as standalone blocks; preserve mathematical expressions as inline or display math according to their source role. Use the repository's existing Markdown/HTML conventions and frozen Anki templates so the same content renders consistently on the site and in Anki. Do not flatten a display formula into prose or put a block formula in an inline span. Inspect generated source text, not just metadata.

Use the next Lab id range `emb-cppfound-0021` through `emb-cppfound-0040`; stop on any collision. Do not edit `meta/id-registry.csv`, taxonomy, validators, plans, existing questions, or another worker's files. Community-only source, long Short answers, and absent registry entries are accepted temporary import gates. Do not commit or push.

Avoid U+2014, U+2190, U+2192, and literal backslash-n. Run focused checks over only this batch: 20 UK files, 20 EN files, id pairing, required sections by type, English TODO bodies, source order, formula/code block preservation, and forbidden characters. The repository-wide validator is expected to fail on the accepted migration gates and is not a batch pass criterion.

Write the report to `temp/agent-reports/lab-batch-3.md` with source range, ids, counts, formatting checks, and judgment calls. Stop after exactly this batch.
