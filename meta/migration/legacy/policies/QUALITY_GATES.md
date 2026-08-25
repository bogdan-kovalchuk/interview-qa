# Quality gates

## Package-source stage

Before a changed TSV in `cards/` can be packaged:

1. Every `type::Code` card must have an entry in `tracking/code_checks.csv` with status `verified`
   or a reviewer-approved `not_executable` reason.
2. Safe deterministic snippets must be executed with the declared Python version. The recorded
   observation must cover output, exception type, or warning behavior asserted by the Back.
3. Unsafe, environment-dependent, I/O, network, subprocess, or free-threaded scenarios require a
   bounded manual test record instead of automatic execution.
4. The completed TSV must pass the normal card validator.
5. A staging-profile Anki import, render, and update smoke test must pass before
   `accepted_cards` becomes nonzero. Record it in `tracking/anki_smoke.csv`.

These checks are deferred only while a topic has no completed Back cards.

## Anki smoke checklist

- Use Anki 2.1.54 or newer because the project relies on text-file headers.
- Build `cards/Python Interview Questions.apkg` only from the 23 reviewed TSV files in `cards/`.
- Import the package into a disposable learner profile with author scheduling disabled.
- Confirm desktop day and night rendering, code wrapping, the "Розгорнуте пояснення" placeholder link, and that neither tags nor source blocks are visible.
- Confirm the expected behavior of a repeated package import in a disposable staging profile.
- Run `scripts/anki_update_smoke.py`; existing GUIDs, card IDs and scheduling fields must stay
  unchanged after a corrected Back is imported.
- Do not change the two-field or one-template structure of `Python Interview Basic` in a patch
  release. A structural change requires a migration procedure.
- Record the tested Anki version and result before promotion.

## Deferred status

`deferred_until_back` is not allowed in package-source TSV files.
