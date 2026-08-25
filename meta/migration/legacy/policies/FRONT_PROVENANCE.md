# Front provenance and future Back linkage

Front-only cards must remain traceable to the existing Q&A material that motivated them. This
traceability is stored outside the TSV so the Anki note type remains `Front / Back / Tags`.

## Stable identifier

Every front carries exactly one tag in this format:

```text
card::PYI_NN_NNN
```

- `PYI` means Python Interview.
- `NN` is the two-digit topic ID from `authoring/manifest.json`.
- `NNN` is a stable sequence within the topic.
- An ID is never reused after a front is rejected.
- Rewording a front does not change its ID.

## Provenance register

`tracking/front_sources.csv` contains one row per card ID with these columns:

| Column | Meaning |
|---|---|
| `card_id` | ID without the `card::` prefix, for example `PYI_05_014` |
| `topic_tag` | Exact `topic::NN_slug` tag |
| `card_file` | Repository-relative package-source TSV path |
| `front_sha256` | SHA-256 of the exact UTF-8 Front field |
| `community_answer_ref` | Commit-pinned URL to the exact existing Q&A answer section; empty only for official-only fronts |
| `official_refs` | One or more authoritative URLs separated by `|` |
| `source_role` | `candidate_plus_official` or `official_only` |
| `back_status` | `pending`, later `drafted`, `reviewed`, or `accepted` |
| `notes` | Short provenance caveat, never a copied answer |

## Rules

0. `verify_front_sources.py` enforces `back_status`: `pending` while the card is front-only,
   and `drafted`, `reviewed`, or `accepted` once its Back is filled.
1. A community answer is a starting point for future Back drafting, not factual authority.
2. Use a GitHub permalink pinned to a commit and exact line range whenever the source is GitHub.
3. Do not copy the community answer into this repository.
4. Official references must be sufficient to verify version/runtime-sensitive premises.
5. The front hash detects accidental drift between the TSV and register.
6. A future Back author starts from `community_answer_ref`, verifies against `official_refs`,
   rewrites concisely, and updates only `back_status` after review.

## Source reference tags

Cards may carry one internal `ref::*` tag that is removed from neither the TSV nor the
provenance workflow:

- `ref::TV_*` identifies one exact question-and-answer section in the audited tavor118 snapshot.
- `ref::OFFICIAL` marks a front designed directly from the official sources in its topic brief.

`sources/community/tavor118_answer_index.csv` maps every `ref::TV_*` value to a source file,
section ordinal, exact line range, and commit-pinned permalink. It deliberately stores no copied
answer text. Rebuild that index only from the audited source commit:

```powershell
python scripts/build_tavor_answer_index.py <path-to-audited-tavor118-checkout>
```

After adding or rewording fronts, rebuild the complete register from the card tags and topic
briefs, then validate it:

```powershell
python scripts/rebuild_front_sources.py
python scripts/verify_front_sources.py
```

For a hash-only update that must preserve hand-written provenance notes, synchronize hashes and
then verify the linkage:

```powershell
python scripts/sync_front_hashes.py
python scripts/verify_front_sources.py
```
