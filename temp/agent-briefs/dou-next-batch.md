# Bounded continuation: DOU embedded interview import

Work in `C:\Users\bogdan\Desktop\interview-qa`.

Read first: `AGENTS.md`, `meta/QUESTIONS.md`, `meta/TAXONOMY.md`, and at least five existing DOU-imported files under `content/uk/embedded` and their English counterparts.

Continue the interrupted import from `C:\Users\bogdan\Documents\Projects\learning\Embedded Interview`. The previous DOU worker imported 60 cards total, stopping after its current batch. Inspect existing ids and titles to determine exactly which source cards are already present; do not duplicate them. Then import exactly the next 10 not-yet-imported DOU cards, preserving the source order across `Junior_anki_cards.txt`, `Middle_front_anki_cards.txt`, and `Senior_front_anki_cards.txt`.

For each card, preserve the source question and Ukrainian short answer under the repository's Markdown structure. Create a matching English file with English title/description as appropriate, but keep the whole English body `TODO`. Keep Ukrainian Detailed explanation and all other unwritten sections `TODO`. Follow the existing DOU files' id prefixes, section mapping, metadata, formatting, and source frontmatter exactly. Do not invent or materially rewrite answers.

The owner explicitly accepted these temporary import gates: source is community-only, Short answer may be outside the 2–5 sentence limit, and ids are not yet added to `meta/id-registry.csv`. Do not edit the registry, taxonomy, validators, plans, existing questions, or another worker's files. Do not add authoritative sources or shorten answers in this batch. Do not commit.

Avoid U+2014, U+2190, and U+2192 in written content. If the next ten cards cannot be identified unambiguously from the existing files, stop and report the ambiguity rather than guessing. Run focused checks over only the new files for UK/EN pairing, required sections, English TODO bodies, and forbidden characters. Do not repair repository-wide validator errors.

Write the concise report to `temp/agent-reports/dou-next-batch.md` with source files/line ranges, ids, counts, checks, and judgment calls. Stop after this one 10-card batch, even if more source cards remain.
