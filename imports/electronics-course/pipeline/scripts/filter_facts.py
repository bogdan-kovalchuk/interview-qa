#!/usr/bin/env python3
"""
Filter extracted facts to target ~12-15 per lecture.
Priority: critical > important > nice-to-know
Then: formula > trap > concept > definition
"""

import json
import argparse
import logging
from pathlib import Path
from collections import defaultdict
from config import get_facts_path, LOGS_DIR

LOGS_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOGS_DIR / 'filter.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)


IMPORTANCE_SCORE = {
    "critical": 100,
    "important": 50,
    "nice-to-know": 10,
    # Legacy values from old prompt
    "high": 80,
    "medium": 40,
    "low": 5,
}

TYPE_SCORE = {
    "formula": 30,
    "trap": 25,
    "concept": 20,
    "definition": 15,
    "fact": 10,
}

TARGET_PER_LECTURE = 13  # Middle of 12-15 range


def score_fact(fact):
    """Calculate priority score for a fact."""
    importance = fact.get("importance", "medium")
    fact_type = fact.get("type", "fact")
    
    imp_score = IMPORTANCE_SCORE.get(importance, 30)
    type_score = TYPE_SCORE.get(fact_type, 10)
    
    return imp_score + type_score


def filter_facts_by_lecture(facts, target=TARGET_PER_LECTURE):
    """Filter facts to target count per lecture."""
    # Group by lecture
    by_lecture = defaultdict(list)
    for fact in facts:
        src = fact.get("source", {})
        lec_num = src.get("lecture_num", 0)
        by_lecture[lec_num].append(fact)
    
    filtered = []
    
    for lec_num in sorted(by_lecture.keys()):
        lec_facts = by_lecture[lec_num]
        
        # Score and sort
        scored = [(score_fact(f), f) for f in lec_facts]
        scored.sort(key=lambda x: -x[0])  # Descending
        
        # Take top N
        top_facts = [f for _, f in scored[:target]]
        filtered.extend(top_facts)
        
        logging.info(f"Lecture {lec_num}: {len(lec_facts)} → {len(top_facts)} facts")
    
    return filtered


def main():
    parser = argparse.ArgumentParser(description="Filter facts to ~12-15 per lecture")
    parser.add_argument("--section", type=str, help="Section ID (e.g., S02)")
    parser.add_argument("--input", type=str, help="Input facts JSON")
    parser.add_argument("--output", type=str, help="Output filtered JSON")
    parser.add_argument("--target", type=int, default=TARGET_PER_LECTURE, help="Target facts per lecture")
    
    args = parser.parse_args()
    
    if args.section:
        input_file = get_facts_path(args.section)
        output_file = input_file.parent / f"{input_file.stem}_filtered.json"
    elif args.input and args.output:
        input_file = Path(args.input)
        output_file = Path(args.output)
    else:
        parser.error("Provide --section or both --input and --output")
    
    logging.info(f"Loading facts from: {input_file}")
    with open(input_file, encoding='utf-8') as f:
        facts = json.load(f)
    
    logging.info(f"Total facts: {len(facts)}")
    
    filtered = filter_facts_by_lecture(facts, target=args.target)
    
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(json.dumps(filtered, indent=2, ensure_ascii=False), encoding='utf-8')
    
    logging.info(f"Filtered: {len(facts)} → {len(filtered)} facts")
    logging.info(f"Saved to: {output_file}")


if __name__ == "__main__":
    main()
