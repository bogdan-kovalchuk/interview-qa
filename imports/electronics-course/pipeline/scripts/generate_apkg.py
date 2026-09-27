#!/usr/bin/env python3
"""
Generate .apkg Anki deck files from card files.
Uses Electronics Q&A model based on Extra Spanish template.
"""

import hashlib
import argparse
import logging
from pathlib import Path

try:
    import genanki
except ImportError:
    print("Error: genanki not installed. Run: pip install genanki")
    exit(1)

from config import SECTIONS, get_cards_path, get_apkg_path, OUTPUT_DIR, LOGS_DIR
from anki_model import (
    ELECTRONICS_MODEL_NAME, ELECTRONICS_FIELDS,
    ELECTRONICS_QFMT, ELECTRONICS_AFMT, ELECTRONICS_CSS
)

LOGS_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOGS_DIR / 'extraction.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)


ELECTRONICS_MODEL = genanki.Model(
    model_id=1607392319,
    name=ELECTRONICS_MODEL_NAME,
    fields=[{"name": f} for f in ELECTRONICS_FIELDS],
    templates=[
        {
            "name": "Electronics Card",
            "qfmt": ELECTRONICS_QFMT,
            "afmt": ELECTRONICS_AFMT,
        },
    ],
    css=ELECTRONICS_CSS
)


def generate_deck_id(section_id):
    """Generate consistent deck ID from section ID (64-bit)."""
    return int(hashlib.md5(section_id.encode()).hexdigest()[:15], 16)


def load_cards(cards_file):
    """Load cards from tab-separated file.
    
    Format: Question\tAnswer\tContext\tImportance\tLecture
    """
    cards = []
    try:
        with open(cards_file, 'r', encoding='utf-8', errors='replace') as f:
            for line_num, line in enumerate(f, 1):
                parts = line.strip().split('\t')
                if len(parts) >= 2:
                    question = parts[0].strip()
                    answer = parts[1].strip()
                    context = parts[2].strip() if len(parts) > 2 else ""
                    importance = parts[3].strip() if len(parts) > 3 else ""
                    lecture = parts[4].strip() if len(parts) > 4 else ""
                    
                    if question and answer:
                        cards.append((question, answer, context, importance, lecture))
                else:
                    logging.warning(f"Skipping malformed line {line_num}: {line[:50]}")
    except Exception as e:
        logging.error(f"Error reading cards file: {e}")
    
    return cards


def generate_apkg(section_id, cards_file=None):
    """Generate .apkg file for a section.
    
    Returns:
        Path to generated .apkg file, or None if no cards found.
    """
    _, deck_name = SECTIONS[section_id]
    full_deck_name = f"Electronics and PCB Design::{section_id}: {deck_name}"
    deck_id = generate_deck_id(section_id)
    
    deck = genanki.Deck(deck_id=deck_id, name=full_deck_name)
    
    if cards_file is None:
        cards_file = get_cards_path(section_id)
    else:
        cards_file = Path(cards_file)
    
    output_file = get_apkg_path(section_id)
    
    if not cards_file.exists():
        logging.error(f"Cards file not found: {cards_file}")
        return None
    
    cards = load_cards(cards_file)
    
    if not cards:
        logging.warning(f"No cards found in {cards_file}")
        return None
    
    for question, answer, context, importance, lecture in cards:
        note = genanki.Note(
            model=ELECTRONICS_MODEL,
            fields=[question, answer, context, importance, lecture]
        )
        deck.add_note(note)
    
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    package = genanki.Package(deck)
    package.write_to_file(str(output_file))
    
    logging.info(f"Generated: {output_file.name} ({len(cards)} cards)")
    return output_file


def main():
    parser = argparse.ArgumentParser(description="Generate Anki .apkg files")
    parser.add_argument("--section", choices=SECTIONS, help="Section ID (e.g., S02)")
    parser.add_argument("--all", action="store_true", help="Generate for all sections")
    parser.add_argument("--cards-file", type=str, help="Custom cards file path")
    
    args = parser.parse_args()
    
    if args.section:
        if generate_apkg(args.section, args.cards_file) is None:
            raise SystemExit(1)
    elif args.all:
        failed = []
        for section_id in SECTIONS.keys():
            try:
                if generate_apkg(section_id) is None:
                    failed.append(section_id)
            except Exception as e:
                logging.error(f"Error generating {section_id}: {e}")
                failed.append(section_id)
        if failed:
            raise SystemExit(1)
    else:
        parser.error("Provide --section or --all")


if __name__ == "__main__":
    main()
