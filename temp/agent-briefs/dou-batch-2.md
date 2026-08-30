# Bounded continuation: DOU embedded interview import, batch 2

Work in `C:\Users\bogdan\Desktop\interview-qa`.

Read `AGENTS.md`, `meta/QUESTIONS.md`, `meta/TAXONOMY.md`, `meta/ANKI.md`, `packaging/anki/notetype/front.html`, `packaging/anki/notetype/back.html`, and `packaging/anki/notetype/card.css`. Inspect existing DOU-imported files and their matching English files.

Continue the DOU migration. Already imported: Junior source cards 1–75, represented by 70 cards in the repository because the earlier 60-card import and the latest 10-card batch cover the first 70 source records. Determine the exact next unimported cards by comparing source questions and existing ids. Import exactly the next 10 not-yet-imported DOU cards in source order, starting after Junior lines 75, without duplicating any card. If the source comparison shows an ambiguity, stop and report it instead of guessing.

Create one Ukrainian and one English file per card, preserving the Ukrainian source question and short answer. English body sections remain `TODO`; Ukrainian Detailed explanation and all other unwritten sections remain `TODO`. Follow existing DOU id prefixes and taxonomy mapping. Keep formulas, inline code, standalone code blocks, and HTML code highlighting structurally faithful to the source and compatible with the frozen site/Anki note type. Do not flatten display mathematics or code blocks into inline text.

Do not edit `meta/id-registry.csv`, taxonomy, validators, plans, existing questions, or another worker's files. Community-only source, long Short answers, and absent registry entries are accepted temporary migration gates. Do not commit or push. Avoid U+2014, U+2190, U+2192, and literal backslash-n.

Run focused checks over only the new files: exactly 10 UK/EN pairs, ids and source order, required sections, English TODO bodies, preservation of inline/block formula and code structure, and forbidden characters. Write the report to `temp/agent-reports/dou-batch-2.md`. Stop after exactly this batch.
