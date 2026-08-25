# Anki compatibility spike harness

`run_spike.py` executes experiments A–J from the M0.4 compatibility brief and writes detailed JSON
evidence. It never accepts the live Anki profile as a work target. Pass copied or restored
collections located in an isolated scratch directory.

The harness uses two fixtures because the exact 392-note target model and genuine scheduling
history may live in different collections:

- `--target-collection-source`: a copied collection containing model `1788409800655` and its 392
  notes;
- `--history-collection-source`: a copied or restored real-profile collection with at least 20
  live cards where `reps > 0` on the two-field model `1778510992002`;
- `--current-profile-copy`: the copied current profile, used for read-only fixture diagnostics.

Run it from a disposable virtual environment containing `anki` and `genanki`:

```powershell
python packaging/anki/spike/run_spike.py `
  --work-dir C:\path\to\scratch\run `
  --current-profile-copy C:\path\to\scratch\Bogdan `
  --target-collection-source C:\path\to\copied-target.anki2 `
  --history-collection-source C:\path\to\restored-history.anki2 `
  --output C:\path\to\scratch\evidence.json
```

Import behavior is measured with `update_notes=always`, `update_notetypes=always`, note-type
merging enabled, scheduling disabled, and deck-config import disabled. The output records these
options so a later run can be compared correctly.

## Tag-refresh experiment F

`run_tag_refresh.py` is the corrected, self-contained experiment F. It creates three notes on
`Interview QA Basic` in a controlled collection, then imports a newer package with the same GUIDs
and changed tag sets. It measures both the project settings and the package-import preset returned
by the Anki Desktop backend. It never reads or accepts a real profile.

Run it with `anki 26.8.1` and `genanki 0.13.1` in the active Python environment. The work directory
must not already exist:

```powershell
python packaging/anki/spike/run_tag_refresh.py `
  --work-dir C:\path\to\scratch\tag-refresh `
  --output C:\path\to\scratch\tag-refresh-evidence.json
```
