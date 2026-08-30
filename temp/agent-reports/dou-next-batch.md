# DOU embedded import report

Timestamp: 2026-09-06 10:05:30 +03:00
Scope: exactly the next 10 not-yet-imported cards after the existing 60-card DOU import.

## Source range

- `C:\Users\bogdan\Documents\Projects\learning\Embedded Interview\Junior_anki_cards.txt`, lines 66–75.
- Source order was preserved within the Junior file. Middle and Senior files were not consumed because the bounded batch ended at Junior line 75.

## Imported IDs

1. `emb-cemb-0019`
2. `emb-cemb-0020`
3. `emb-rtos-0007`
4. `emb-cemb-0021`
5. `emb-cemb-0022`
6. `emb-cemb-0023`
7. `emb-memlink-0007`
8. `emb-memlink-0008`
9. `emb-cemb-0024`
10. `emb-periph-0008`

## Counts

- Cards: 10
- Files: 20
- Ukrainian files: 10
- English files: 10
- Registry entries added: 0
- Existing questions edited: 0

## Focused checks

- UK/EN pairing by ID: PASS, 10/10 pairs.
- Required sections (`Short answer`, `Detailed explanation`, `Sources`): PASS, 20/20 files.
- English `Short answer` and `Detailed explanation` bodies equal `TODO`: PASS, 10/10 files.
- Forbidden U+2014, U+2190, U+2192 in new files: PASS, 20/20 files.
- Repository-wide validator: not run, as instructed.

## Judgment calls

- Existing DOU titles were matched against source questions with Markdown and punctuation differences; the next unimported source range was unambiguous.
- Section mapping continued the existing DOU prefixes: C/C++ basics to `c-in-embedded`, memory barrier/cache coherence to `rtos`, memory storage topics to `memory-and-linker`, and UART to `peripherals-and-buses`.
- Source answer wording was retained. Forbidden source typography was normalized only where required: em dash to en dash and right arrows to `->`.
- The source line 76 card was initially created accidentally during drafting, then removed before the final checks; it is not part of this batch.

No commit or push was performed.
