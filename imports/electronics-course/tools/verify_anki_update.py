"""Import and update a temporary Anki collection; verify real learner state."""
from pathlib import Path
import contextlib
import io
import json
import shutil
import tempfile
import time

import anki.lang
from anki.collection import Collection
from anki.importing.apkg import AnkiPackageImporter

import build_course_anki as builder


def main():
    # The package importer logs note text through Anki's i18n layer, which is
    # only initialised by the desktop app; set it up for standalone use.
    anki.lang.set_lang('en_US')
    original_dir = builder.CARD_DIR
    package = original_dir / 'Electronics_Sections_1-4.apkg'
    with tempfile.TemporaryDirectory(prefix='electronics-anki-update-') as tmp:
        tmp = Path(tmp)
        collection = Collection(str(tmp / 'learner.anki2'))
        try:
            AnkiPackageImporter(collection, str(package)).run()
            original_notes = collection.db.all('select id, guid from notes order by guid')
            count = len(original_notes)
            row = collection.db.first('select id, nid from cards order by id limit 1')
            card = collection.get_card(row[0])
            card.type = 2
            card.queue = 2
            card.due = collection.sched.today + 15
            card.ivl = 15
            card.reps = 8
            card.lapses = 1
            card.factor = 2500
            collection.update_card(card)
            state_sql = 'select id,nid,type,queue,due,ivl,reps,lapses,factor from cards where id=?'
            before = collection.db.first(state_sql, card.id)
            # Change one Back in isolated source files, retaining its identity tag.
            sources = tmp / 'sources'
            sources.mkdir()
            for filename in ['electronics_basic_template.md'] + [f'Section_{n}_anki_cards.txt' for n in range(1, 5)]:
                shutil.copy2(original_dir / filename, sources / filename)
            note = collection.get_note(row[1])
            identity = next(tag for tag in note.tags if tag.startswith('id::'))
            updated = False
            for path in sources.glob('Section_*_anki_cards.txt'):
                lines = path.read_text(encoding='utf-8').splitlines()
                for i, line in enumerate(lines):
                    if line.startswith('#') or not line.strip():
                        continue
                    front, back, tags = line.split('\t')
                    if identity in tags.split():
                        lines[i] = '\t'.join([front, back + '<br>Update smoke check.', tags])
                        updated = True
                path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
            assert updated
            builder.CARD_DIR = sources
            with contextlib.redirect_stdout(io.StringIO()):
                builder.build(timestamp=time.time() + 60)
            AnkiPackageImporter(collection, str(sources / package.name)).run()
            assert collection.db.all('select id, guid from notes order by guid') == original_notes
            assert collection.db.first(state_sql, card.id) == before
            assert 'Update smoke check.' in collection.get_note(row[1])['Back']
            assert collection.note_count() == count
        finally:
            builder.CARD_DIR = original_dir
            collection.close()
    result = {'passed': True, 'notes': count, 'duplicate_notes': 0,
              'note_ids_and_guids_preserved': True, 'back_updated': True,
              'review_schedule_preserved': True, 'used_temporary_collection': True}
    target = Path(__file__).resolve().parents[1] / 'reports/anki-update-verification.json'
    target.write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
