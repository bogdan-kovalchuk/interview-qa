# `.apkg` generation and safe update strategy

Research date: 2026-09-03.

## Implemented decision

Publish one full package named `Python Interview Questions.apkg`. Its root deck should be
`Python Interview Questions`, with these 23 child decks:

```text
Python Interview Questions
├── 01 Python Fundamentals
├── 02 Syntax and Control Flow
├── ...
└── 23 Git, CI/CD, and SDLC
```

The existing topic TSV files remain the canonical content source. The package is a generated
release artifact, never a replacement for those files.

The implementation uses `scripts/build_apkg.py`, the persistent collection at
`authoring/collection/Python Interview Questions.anki2`, the identity manifest
`tracking/apkg_note_identity.csv`, and the release artifact
`cards/Python Interview Questions.apkg`. The pinned build dependency is
`requirements/anki-build.txt`.

## Answer to the learning-history concern

Rebuilding and publishing the complete package does **not** inherently reset a learner's review
history. A later `.apkg` import updates an already-imported note when it can identify the same
note and the incoming version is newer. Anki's documented package importer performs this update
by default; recent versions also offer explicit update and note-type merge choices [1].

The import implementation looks up existing notes by their GUID and updates a matching note
without regenerating its cards [2]. Therefore, an unchanged card identity retains its local
scheduling state such as due date, interval, lapse and review count. This is an implementation
property that must be regression-tested against the supported Anki version before each release.

The package must be exported **without scheduling information**. A package author's review
history is not suitable for other learners, and Anki explicitly allows package progress to be
excluded on import [1]. On a later update, the recipient's locally accumulated scheduling remains
in their collection because the card is not replaced.

## Conditions that make this safe

| Condition | Why it matters | Release rule |
|---|---|---|
| Stable note GUID | Package updates identify previously imported notes by GUID. | Preserve the GUID assigned on the first production build for each `card::PYI_*` ID. Never generate a fresh identity for an existing card. |
| Stable note type structure | Field or template-structure changes can prevent normal updates. | Freeze `Python Interview Basic` at two fields, `Front` and `Back`, for v1.0. Treat added, removed, or reordered fields/templates as a migration. |
| Stable card template ordinal | Existing cards are associated with the note template ordinal. | Keep one `Card 1` template. CSS and Front/Back HTML edits are non-structural only after a staging import proves them safe. |
| Monotonic note modification time | Default package updating accepts an incoming note only when it is newer. | Update the modification time only for changed notes; record the release version and build time. |
| Stable root and child deck names | Renaming is a deck migration, not ordinary content editing. | Create all 23 child decks once from `authoring/TAXONOMY.md`; do not rename them in patch releases. |

Do not use an arbitrary deterministic string as Anki's internal GUID. The Anki manual recommends
letting Anki create GUIDs [3]. Instead, create and retain a controlled authoring collection that
already contains the real GUIDs assigned by Anki.

## Recommended build architecture

```text
cards/*.txt + authoring/NOTE_TYPE_TEMPLATE.md
                 │ validate and review
                 ▼
controlled authoring collection (not a learner profile)
                 │ merge changed notes by card::PYI_* identity
                 ▼
Python Interview Questions.apkg (without scheduling)
                 │ import as an update
                 ▼
learner collection: changed text, preserved review state
```

### Controlled authoring collection

Maintain a dedicated, non-personal Anki collection solely for builds. It is the identity carrier,
not a second hand-edited content source.

- On the first release, create the `Python Interview Questions` root deck, all 23 child decks,
  the `Python Interview Basic` note type and one note per accepted card.
- Locate every note by its existing `card::PYI_NN_NNN` tag. The builder must reject a missing or
  duplicated card ID rather than guessing.
- For a changed TSV row, update only `Front`, `Back`, and the permitted tags of the matching
  authoring note. For a new row, add one new note and let Anki assign its GUID.
- Do not rebuild the authoring collection from an empty database for routine releases. That would
  generate new note identities and turn an update into duplicate cards for learners.
- Store an auditable `card_id -> Anki GUID` identity manifest produced by the build. It is a
  validation record, not a substitute for the collection's native identities.

The build tool should use Anki's public collection/import-export APIs, rather than write SQLite
directly. Anki's developer documentation explicitly warns that direct database writes can break
sync metadata or invalidate collection data [4].

### Package export

Export the root deck and its descendants as one package, using a supported Anki Python library
version (the documented package export API requires Anki 23.12 or later [4]). Use:

- package filename: `Python Interview Questions.apkg`;
- root deck: `Python Interview Questions`;
- `with_scheduling=False`;
- media included when the deck later gains media;
- deck configuration included only after a separate test confirms it does not overwrite a
  learner's intentional deck settings.

`cards/` currently supplies one TSV per topic. The builder maps each topic code to a child
deck name from `authoring/TAXONOMY.md`; it must not infer a deck from a human-written question.

## Update workflow for a corrected card

1. Fix the canonical TSV and run the normal card, provenance, project and code-evidence gates.
2. Run the package builder against a copy of the controlled authoring collection.
3. Verify that only intended `card::` IDs changed, existing GUIDs did not change, and only new
   cards have new GUIDs.
4. Export the **entire** root deck again as the next version of `Python Interview Questions.apkg`.
5. Run the scheduling-preservation smoke test below in a disposable learner profile.
6. Publish the new `.apkg` and concise update instructions.

For the learner, importing the newer package updates changed notes while retaining existing card
scheduling. New cards appear as new. The learner should leave package progress import disabled:
that option concerns progress embedded by the author, not the learner's own existing progress [1].

If a learner edited the same note locally, the default newer-version rule can keep the local text.
Anki 23.10+ also offers an unconditional update choice, but that deliberately overwrites the
learner's note content [1]. Neither path should reset the scheduling of an unchanged card.

## Changes that require a migration release

Do not silently ship any of these as a normal correction:

- adding, removing, renaming, or reordering note fields;
- adding/removing card templates or changing template ordinals;
- changing the root or child deck names;
- intentionally splitting one existing note into several notes;
- intentionally deleting a published note;
- replacing the controlled authoring collection or its GUID manifest.

Anki documents that note-type changes can block ordinary package updates [1]. A migration release
needs a versioned procedure, backup instruction, disposable-profile rehearsal and an explicit
conflict policy. In particular, package import is additive/update-oriented: the importer iterates
over incoming notes and updates or adds them; it does not make absence from the new package an
automatic deletion command [2]. Retired cards should therefore be tagged or suspended through a
separately tested migration, not silently removed from the TSV and package.

## Required automated smoke test

For each release, use a disposable learner profile and record results in
`tracking/anki_smoke.csv`:

1. Import v1 with progress excluded. Assert one root deck, 23 child decks, expected note count,
   expected card count, and no author review history.
2. Review at least three cards. Record each card's note GUID, card ID, queue, due, interval,
   reps, lapses and ease.
3. Change the Back of one existing card and add one new card in the authoring collection; export
   v2 without scheduling.
4. Import v2 with note updates enabled and progress excluded.
5. Assert the corrected Back is visible; the three original cards keep the same GUID, card ID,
   queue, due, interval, reps, lapses and ease; and the new card is `new`.
6. Repeat with a CSS-only template change. Assert the original scheduling still remains and the
   expected UI is rendered in day and night modes.
7. Re-import v2. Assert it creates neither duplicate notes nor duplicate cards.

## Recommendation

Adopt the single-package, 23-subdeck model. It gives the user one simple installation artifact
and remains safe for incremental corrections **only** when releases are built from a persistent
authoring collection that preserves Anki identities. Do not make a fresh `.apkg` from TSV files
alone for every release.

## Implemented validation commands

```powershell
.\.venv\Scripts\python.exe scripts\build_apkg.py
.\.venv\Scripts\python.exe scripts\verify_apkg.py
.\.venv\Scripts\python.exe scripts\anki_update_smoke.py
```

`verify_apkg.py` imports the release into a disposable collection and checks the 23 child decks,
392 note/card identities, zero author review history, and GUID manifest. `anki_update_smoke.py`
performs a disposable v1-to-v2 correction and asserts that the existing learner card's GUID, card
ID, queue, due, interval, repetitions, lapses, and ease factor remain unchanged.

## Sources

1. [Anki Manual: Packaged Decks](https://docs.ankiweb.net/importing/packaged-decks.html), accessed 2026-09-03.
2. [Anki package importer: note update implementation](https://github.com/ankitects/anki/blob/main/rslib/src/import_export/package/apkg/import/notes.rs#L2783-L3042), accessed 2026-09-03.
3. [Anki Manual: Text Files, GUID Column](https://docs.ankiweb.net/importing/text-files.html#guid-column), accessed 2026-09-03.
4. [Anki developer documentation: package import/export and collection writes](https://github.com/ankitects/anki/blob/main/docs-site/addons/the-anki-module.mdx#L238-L324), accessed 2026-09-03.
