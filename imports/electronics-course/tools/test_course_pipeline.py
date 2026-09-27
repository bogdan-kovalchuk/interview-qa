"""Offline regression checks for paths, subtitle parsing, and Anki packaging."""
from pathlib import Path
from unittest.mock import patch
from zipfile import ZipFile
import json
import sqlite3
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'pipeline/scripts'))
sys.path.insert(0, str(ROOT / 'tools'))

import config
import download_subtitles
import generate_apkg
import run_pipeline


def test_config_paths():
    assert config.BASE_DIR == ROOT
    assert config.PDF_PATH.is_file()
    for name, _ in config.SECTIONS.values():
        assert (config.SUBTITLES_DIR / name).is_dir()
    data = json.loads((ROOT / 'pipeline/output/subtitles/S02_chunks.json').read_text(encoding='utf-8'))
    assert all(Path(lecture['source_file']).is_file() for lecture in data['lectures'])


def test_vtt_comment_does_not_discard_following_captions():
    vtt = 'WEBVTT\n\nNOTE comment\nmore comment\n\n00:00:01.000 --> 00:00:03.000\nHello &amp; <b>world</b>\n'
    assert download_subtitles.vtt_to_text(vtt).strip() == 'Hello & world'


def test_package_missing_or_empty_input_does_not_report_success(tmp_path):
    missing = tmp_path / 'missing.txt'
    assert generate_apkg.generate_apkg('S01', missing) is None
    empty = tmp_path / 'empty.txt'
    empty.write_text('', encoding='utf-8')
    assert generate_apkg.generate_apkg('S01', empty) is None


def test_pipeline_preserves_metadata_in_actual_package(tmp_path):
    chunks = tmp_path / 'chunks.json'
    facts = tmp_path / 'facts.json'
    cards = tmp_path / 'cards.txt'
    package = tmp_path / 'test.apkg'
    card = dict(question='Voltage?', answer='Potential difference', context='Circuit analysis',
                importance='critical', lecture='L01')
    with patch.object(run_pipeline, 'process_section', return_value={'lectures': []}), \
         patch.object(run_pipeline, 'get_subtitle_chunks_path', return_value=chunks), \
         patch.object(run_pipeline, 'get_facts_path', return_value=facts), \
         patch.object(run_pipeline, 'get_cards_path', return_value=cards), \
         patch.object(run_pipeline, 'extract_facts_from_chunks', return_value=[{'content': 'Voltage'}]), \
         patch.object(run_pipeline, 'convert_facts_to_cards', return_value=[card]), \
         patch.object(generate_apkg, 'get_apkg_path', return_value=package):
        run_pipeline.run_pipeline_for_section('S01', 'offline-test')
    assert package.is_file()
    with ZipFile(package) as archive:
        database = tmp_path / 'collection.anki2'
        database.write_bytes(archive.read('collection.anki2'))
    with sqlite3.connect(database) as connection:
        fields = connection.execute('select flds from notes').fetchone()[0].split('\x1f')
        assert fields == [card[k] for k in ('question', 'answer', 'context', 'importance', 'lecture')]
        assert connection.execute('select count(*) from cards').fetchone()[0] == 1


def test_package_cli_missing_input_fails(tmp_path):
    result = subprocess.run([sys.executable, '-B', str(ROOT / 'pipeline/scripts/generate_apkg.py'),
                             '--section', 'S01', '--cards-file', str(tmp_path / 'missing.txt')],
                            capture_output=True)
    assert result.returncode == 1
