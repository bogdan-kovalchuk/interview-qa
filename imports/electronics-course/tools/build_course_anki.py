"""Build the four course decks and a combined package from canonical TSVs.

Stable id:: tags are persisted in the source files; retain them when editing.
The older five-field LLM experiment uses a different model and is independent.
"""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re

import genanki

ROOT = Path(__file__).resolve().parents[1]
CARD_DIR = ROOT / 'anki cards'
MODEL_ID = 2026092701
TITLES = {1: 'The Starting Line', 2: 'Introduction to Electronics',
          3: 'Advanced Circuit Analysis Techniques and Tools', 4: 'Electrical Engineering 101'}
EXPECTED = {1: set(range(1, 2)), 2: set(range(2, 27)),
            3: set(range(27, 32)), 4: set(range(32, 81))}


def load_section(number):
    path = CARD_DIR / f'Section_{number}_anki_cards.txt'
    lines = path.read_text(encoding='utf-8-sig').splitlines()
    rows = []
    used = set()
    for lineno, line in enumerate(lines, 1):
        if not line.strip() or line.startswith('#'):
            continue
        parts = line.split('\t')
        if len(parts) != 3 or not all(p.strip() for p in parts):
            raise ValueError(f'{path.name}:{lineno}: expected three nonempty fields')
        front, back, tags = parts
        tags = tags.split()
        identities = [t for t in tags if t.startswith('id::')]
        if len(identities) > 1 or (identities and identities[0] in used):
            raise ValueError(f'{path.name}:{lineno}: duplicate identity')
        if identities:
            used.add(identities[0])
        rows.append([front, back, tags])
    next_number = 1
    for front, back, tags in rows:
        if not any(t.startswith('id::') for t in tags):
            while f'id::electronics-s{number:02d}-{next_number:04d}' in used:
                next_number += 1
            identity = f'id::electronics-s{number:02d}-{next_number:04d}'
            tags.append(identity)
            used.add(identity)
            next_number += 1
    lectures = {int(t.removeprefix('Лекція_')) for _, _, tags in rows
                for t in tags if t.startswith('Лекція_')}
    if lectures != EXPECTED[number]:
        raise ValueError(f'Section {number}: incorrect lecture coverage {lectures ^ EXPECTED[number]}')
    header = ['#separator:tab', '#html:true',
              f'#deck:Electronics and PCB Design::S{number:02d}: {TITLES[number]}',
              '#notetype:Electronics Basic', '#tags column:3']
    text = '\n'.join(header + ['\t'.join([front, back, ' '.join(tags)])
                                for front, back, tags in rows]) + '\n'
    if path.read_text(encoding='utf-8-sig') != text:
        path.write_text(text, encoding='utf-8')
    return rows


def create_model():
    template = (CARD_DIR / 'electronics_basic_template.md').read_text(encoding='utf-8')
    html = re.findall(r'```html\n(.*?)```', template, flags=re.S)
    css = re.search(r'```css\n(.*?)```', template, flags=re.S).group(1)
    assert len(html) == 2
    return genanki.Model(MODEL_ID, 'Electronics Basic',
                        fields=[{'name': 'Front'}, {'name': 'Back'}],
                        templates=[{'name': 'Electronics Card', 'qfmt': html[0], 'afmt': html[1]}],
                        css=css)


def build(timestamp=None):
    model = create_model()
    decks, manifest, all_ids = [], [], set()
    for number in TITLES:
        rows = load_section(number)
        deck = genanki.Deck(2026092710 + number,
                           f'Electronics and PCB Design::S{number:02d}: {TITLES[number]}')
        for front, back, tags in rows:
            identity = next(t for t in tags if t.startswith('id::'))
            assert identity not in all_ids, identity
            all_ids.add(identity)
            guid = genanki.guid_for('electronics-course-basic-v1', identity)
            note = genanki.Note(model=model, fields=[front, back], tags=tags, guid=guid)
            deck.add_note(note)
            manifest.append({'id': identity, 'guid': guid, 'section': number,
                             'source': f'Section_{number}_anki_cards.txt',
                             'content_sha256': hashlib.sha256((front+'\t'+back).encode()).hexdigest()})
        package = CARD_DIR / f'Section_{number}.apkg'
        genanki.Package(deck).write_to_file(str(package), timestamp=timestamp)
        decks.append(deck)
    combined = CARD_DIR / 'Electronics_Sections_1-4.apkg'
    genanki.Package(decks).write_to_file(str(combined), timestamp=timestamp)
    (CARD_DIR / 'note-identities.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    result = {'combined_package': str(combined), 'notes': len(manifest),
              'sections': dict(Counter(m['section'] for m in manifest)), 'model_id': MODEL_ID}
    print(json.dumps(result, indent=2))
    return result


if __name__ == '__main__':
    build()
