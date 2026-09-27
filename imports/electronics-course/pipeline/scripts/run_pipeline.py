#!/usr/bin/env python3
"""
Master pipeline script: Subtitles + PDF → Anki Decks (.apkg)
Uses Qwen3.7 Plus via OpenCode Go API.

Usage:
    python pipeline/scripts/run_pipeline.py --section S02 --api-key YOUR_OPENCODE_GO_KEY
    python pipeline/scripts/run_pipeline.py --all --api-key YOUR_OPENCODE_GO_KEY
"""

import json
import argparse
import sys
import logging
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from config import SECTIONS, get_subtitle_chunks_path, get_pdf_chunks_path, get_facts_path, get_cards_path, OUTPUT_DIR, LOGS_DIR
from process_subtitles import process_section
from process_pdf import main as process_pdf_main
from extract_facts import extract_facts_from_chunks
from write_cards import convert_facts_to_cards
from generate_apkg import generate_apkg

LOGS_DIR.mkdir(parents=True, exist_ok=True)

# Configure logging once at module level
if not logging.root.handlers:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(LOGS_DIR / 'pipeline.log', encoding='utf-8'),
            logging.StreamHandler()
        ]
    )


def run_pipeline_for_section(section_id, api_key):
    """Run complete pipeline for one section."""
    
    logging.info(f"{'='*60}")
    logging.info(f"Processing {section_id}: {SECTIONS[section_id][1]}")
    logging.info(f"{'='*60}")
    
    # Step 1: Process subtitles
    logging.info("Step 1: Processing subtitles...")
    subtitle_data = process_section(section_id)
    if subtitle_data:
        chunks_file = get_subtitle_chunks_path(section_id)
        chunks_file.parent.mkdir(parents=True, exist_ok=True)
        chunks_file.write_text(json.dumps(subtitle_data, indent=2, ensure_ascii=False), encoding='utf-8')
    else:
        logging.warning("No subtitle data, skipping...")
        return
    
    # Step 2: Extract facts (Step A) - using Qwen3.7 Plus
    logging.info("Step 2: Extracting facts from chunks (Qwen3.7 Plus)...")
    facts_file = get_facts_path(section_id)
    facts = extract_facts_from_chunks(chunks_file, api_key, source_type="subtitle")
    facts_file.parent.mkdir(parents=True, exist_ok=True)
    facts_file.write_text(json.dumps(facts, indent=2, ensure_ascii=False), encoding='utf-8')
    logging.info(f"Extracted {len(facts)} facts")
    
    # Step 3: Write cards (Step B) - using Qwen3.7 Plus
    logging.info("Step 3: Converting facts to Anki cards (Qwen3.7 Plus)...")
    cards_file = get_cards_path(section_id)
    cards = convert_facts_to_cards(facts_file, api_key)
    cards_file.parent.mkdir(parents=True, exist_ok=True)
    with open(cards_file, 'w', encoding='utf-8') as f:
        for card in cards:
            f.write('\t'.join(str(card.get(field, '')).replace('\t', ' ').replace('\n', '<br>')
                              for field in ('question', 'answer', 'context', 'importance', 'lecture')) + '\n')
    logging.info(f"Generated {len(cards)} cards")
    
    # Step 4: Generate .apkg
    logging.info("Step 4: Generating Anki package...")
    apkg_file = generate_apkg(section_id, cards_file)
    
    if apkg_file:
        logging.info(f"Completed {section_id}: {apkg_file.name}")
    else:
        logging.warning(f"Completed {section_id}: No output file generated")


def run_full_pipeline(api_key, include_pdf=False):
    """Run pipeline for all sections."""
    
    logging.info("Starting full pipeline...")
    logging.info("Using Qwen3.7 Plus via OpenCode Go API")
    
    if include_pdf:
        logging.info("Processing PDF textbook...")
        try:
            process_pdf_main()
        except Exception as e:
            logging.error(f"PDF processing failed: {e}")
    
    for section_id in SECTIONS.keys():
        try:
            run_pipeline_for_section(section_id, api_key)
        except Exception as e:
            logging.error(f"Error processing {section_id}: {e}")
            continue
    
    logging.info("="*60)
    logging.info("Pipeline complete!")
    logging.info(f"Output: {OUTPUT_DIR / 'apkg'}")
    logging.info("="*60)


def main():
    parser = argparse.ArgumentParser(
        description="Run Anki card generation pipeline using Qwen3.7 Plus via OpenCode Go"
    )
    parser.add_argument("--section", type=str, help="Process specific section (e.g., S02)")
    parser.add_argument("--all", action="store_true", help="Process all sections")
    parser.add_argument("--pdf", action="store_true", help="Include PDF textbook processing")
    parser.add_argument("--api-key", type=str, required=True, help="OpenCode Go API key")
    
    args = parser.parse_args()
    
    if args.section:
        if args.section not in SECTIONS:
            logging.error(f"Invalid section. Choose from: {', '.join(SECTIONS.keys())}")
            sys.exit(1)
        run_pipeline_for_section(args.section, args.api_key)
    elif args.all:
        run_full_pipeline(args.api_key, include_pdf=args.pdf)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
