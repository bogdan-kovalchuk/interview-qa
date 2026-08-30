# DOU embedded import report

Scope: exactly the next 10 not-yet-imported DOU cards in source order after Junior line 75.

## Source range

- `C:\Users\bogdan\Documents\Projects\learning\Embedded Interview\Junior_anki_cards.txt`, lines 76–83.
- `C:\Users\bogdan\Documents\Projects\learning\Embedded Interview\Middle_front_anki_cards.txt`, lines 6–7.
- Junior lines 84–85 are empty, so the batch continues with the first two Middle records.

## Imported IDs

1. `emb-memlink-0009` – Junior 76
2. `emb-cemb-0025` – Junior 77
3. `emb-memlink-0010` – Junior 78
4. `emb-cemb-0026` – Junior 79
5. `emb-cemb-0027` – Junior 80
6. `emb-memlink-0011` – Junior 81
7. `emb-cemb-0028` – Junior 82
8. `emb-fund-0009` – Junior 83
9. `emb-cemb-0029` – Middle 6
10. `emb-cemb-0030` – Middle 7

## Counts

- Cards: 10
- Files: 20
- Ukrainian files: 10
- English files: 10
- Matching UK/EN pairs: 10
- Registry entries added: 0
- Existing questions edited: 0

## Focused checks

- Required sections in all new files: PASS.
- English `Short answer` and `Detailed explanation` bodies are `TODO`: PASS, 10/10.
- UK/EN IDs and pairing: PASS, 10/10.
- Source order and selected source records: PASS.
- Ukrainian source answer parity after the required paragraph and typography normalization: PASS, 10/10.
- Inline HTML and code structure parity: PASS, 10/10.
- Forbidden U+2014, U+2190, U+2192, and literal `\\n`: PASS, 20/20.
- Focused checks total: PASS, 73/73.
- Repository-wide validator: not run; the brief requested focused checks over only the new files.

## Notes

- The batch uses the next source records, including records with similar topics to earlier cards; no source record from the selected range was duplicated.
- No taxonomy, plan, validator, existing question, or `meta/id-registry.csv` file was changed.
- No commit or push was performed.
