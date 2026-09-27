"""Independently verify package databases, exact TSV content and coverage."""
from pathlib import Path
from zipfile import ZipFile
from html.parser import HTMLParser
import contextlib
import json
import re
import sqlite3
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CARDS = ROOT / 'anki cards'


def read_package(path):
    with ZipFile(path) as archive, tempfile.TemporaryDirectory(prefix='course-apkg-check-') as tmp:
        assert archive.testzip() is None
        database = Path(tmp) / 'collection.anki2'
        database.write_bytes(archive.read('collection.anki2'))
        # sqlite3's context manager only commits; close explicitly so Windows
        # can delete the temporary database afterwards.
        with contextlib.closing(sqlite3.connect(database)) as connection:
            assert connection.execute('pragma integrity_check').fetchone()[0] == 'ok'
            models, decks = connection.execute('select models, decks from col').fetchone()
            rows = connection.execute('select guid, mid, flds, tags from notes').fetchall()
            cards = connection.execute('select count(*) from cards').fetchone()[0]
        return json.loads(models), json.loads(decks), rows, cards


def main():
    identity = json.loads((CARDS / 'note-identities.json').read_text(encoding='utf-8'))
    by_id = {x['id']: x for x in identity}
    assert len(by_id) == len(identity)
    expected = {}
    section_guids = {}
    coverage = {}
    for section in range(1, 5):
        path = CARDS / f'Section_{section}_anki_cards.txt'
        lines = path.read_text(encoding='utf-8-sig').splitlines()
        assert lines[:2] == ['#separator:tab', '#html:true']
        assert f'::S{section:02d}:' in lines[2]
        assert lines[3:5] == ['#notetype:Electronics Basic', '#tags column:3']
        section_guids[section] = set()
        coverage[section] = set()
        for line in lines[5:]:
            front, back, tagtext = line.split('\t')
            assert front.strip() and back.strip()
            assert '\ufffd' not in line
            assert not re.search(r'(?i)TODO|PLACEHOLDER|TBD', front + back)
            parser = HTMLParser()
            parser.feed(front + back)
            # A raw '<' (e.g. inside a MathJax formula) is parsed as a tag and
            # swallows the rest of the field; it must be written as &lt;.
            stray = re.search(r'<(?!/?(?:span|code|strong|br|b|i|em|sub|sup|u)\b)', front + back)
            assert not stray, f'{path.name}: unescaped "<": {(front + back)[stray.start():stray.start() + 30]}'
            tags = tagtext.split()
            key = next(t for t in tags if t.startswith('id::'))
            guid = by_id[key]['guid']
            assert guid not in expected
            expected[guid] = (front + '\x1f' + back, set(tags))
            section_guids[section].add(guid)
            coverage[section].update(int(t.removeprefix('Лекція_')) for t in tags if t.startswith('Лекція_'))
    assert coverage == {1: {1}, 2: set(range(2, 27)), 3: set(range(27, 32)), 4: set(range(32, 81))}
    results = []
    for section in [1, 2, 3, 4, None]:
        path = CARDS / (f'Section_{section}.apkg' if section else 'Electronics_Sections_1-4.apkg')
        models, decks, notes, count = read_package(path)
        assert len(models) == 1
        model = next(iter(models.values()))
        assert model['name'] == 'Electronics Basic'
        assert [f['name'] for f in model['flds']] == ['Front', 'Back']
        assert len(notes) == count
        actual = {row[0] for row in notes}
        assert len(actual) == len(notes)
        assert actual == (section_guids[section] if section else set(expected))
        for guid, mid, fields, tags in notes:
            assert fields == expected[guid][0]
            assert set(tags.split()) == expected[guid][1]
            assert str(mid) in models
        results.append({'file': path.name, 'notes': count, 'model_id': model['id']})
    result = {'passed': True, 'packages': results, 'lectures_covered': 80,
              'notes': len(expected), 'guid_count': len(expected)}
    (ROOT / 'reports/course-anki-verification.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
