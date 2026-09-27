#!/usr/bin/env python3
"""
Step B: Convert extracted facts to Anki cards using Qwen3.7 Plus via OpenCode Go.
Output format: Question\tAnswer\tContext\tImportance\tLecture
"""

import json
import argparse
import logging
from pathlib import Path
from config import (
    get_facts_path, get_cards_path,
    LLM_TEMPERATURE_CARDS, LOGS_DIR
)
from llm_client import call_llm

LOGS_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOGS_DIR / 'extraction.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)


CARD_WRITING_PROMPT = """Convert this electronics fact into an Anki flashcard.

FACT:
Type: {fact_type}
Content: {content}
Detail: {detail}
Importance: {importance}

Create:
- Question: Specific testable question in Ukrainian (1 sentence)
- Answer: Concise answer in Ukrainian (1-2 sentences)
- Context: Brief example or application context (1 sentence, or empty if not needed)

Output as tab-separated line (5 fields):
Question\tAnswer\tContext\tImportance\tLecture

Rules:
- Question should test recall, not recognition
- Answer should be atomic (one fact only)
- Use Ukrainian language
- Keep questions short and specific
- Context is optional - use for examples/applications
- Importance: copy from fact (critical/important/nice-to-know)
- Lecture: copy from source
- Do NOT wrap in markdown code blocks

Example:
Що таке закон Ома?\tV = IR, де V - напруга (В), I - струм (А), R - опір (Ом)\tВикористовується для розрахунку струму в колі\tcritical\tL06"""


def write_card_from_fact(fact, api_key):
    """Convert fact to Anki card using LLM."""
    prompt = CARD_WRITING_PROMPT.format(
        fact_type=fact.get("type", "fact"),
        content=fact.get("content", ""),
        detail=fact.get("detail", ""),
        importance=fact.get("importance", "important")
    )
    
    try:
        card_text = call_llm(prompt, api_key, LLM_TEMPERATURE_CARDS)
        card_text = card_text.strip()
        
        # Strip markdown code blocks if present
        if card_text.startswith('```'):
            lines = card_text.split('\n')
            card_text = '\n'.join(lines[1:-1] if lines[-1].startswith('```') else lines[1:])
        
        parts = card_text.split('\t')
        if len(parts) >= 2:
            src = fact.get("source", {})
            lecture_num = src.get("lecture_num", 0)
            
            return {
                "question": parts[0].strip(),
                "answer": parts[1].strip(),
                "context": parts[2].strip() if len(parts) > 2 else "",
                "importance": parts[3].strip() if len(parts) > 3 else fact.get("importance", ""),
                "lecture": parts[4].strip() if len(parts) > 4 else f"L{lecture_num:02d}"
            }
        else:
            logging.warning(f"Invalid card format: {card_text[:100]}")
            return None
    
    except Exception as e:
        logging.error(f"Failed to write card: {e}")
        return None


def convert_facts_to_cards(facts_file, api_key):
    """Convert all facts in file to cards."""
    with open(facts_file, encoding='utf-8') as f:
        facts = json.load(f)
    
    cards = []
    seen_questions = set()
    
    for i, fact in enumerate(facts):
        logging.info(f"Converting fact {i+1}/{len(facts)}...")
        
        card = write_card_from_fact(fact, api_key)
        if card:
            # Deduplicate by question
            q_lower = card["question"].lower()
            if q_lower not in seen_questions:
                seen_questions.add(q_lower)
                card["source_fact"] = fact
                cards.append(card)
            else:
                logging.info(f"  Skipping duplicate: {card['question'][:50]}")
    
    return cards


def main():
    parser = argparse.ArgumentParser(description="Convert facts to cards (Step B)")
    parser.add_argument("--input", type=str, help="Input facts JSON file")
    parser.add_argument("--output", type=str, help="Output cards TXT file")
    parser.add_argument("--section", type=str, help="Section ID (e.g., S02)")
    parser.add_argument("--api-key", type=str, required=True, help="OpenCode Go API key")
    
    args = parser.parse_args()
    
    if args.section:
        input_file = get_facts_path(args.section)
        output_file = get_cards_path(args.section)
    elif args.input and args.output:
        input_file = Path(args.input)
        output_file = Path(args.output)
    else:
        parser.error("Provide --section or both --input and --output")
    
    logging.info(f"Converting facts to cards: {input_file}")
    
    cards = convert_facts_to_cards(input_file, args.api_key)
    
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        for card in cards:
            f.write(f"{card['question']}\t{card['answer']}\t{card['context']}\t{card['importance']}\t{card['lecture']}\n")
    
    logging.info(f"Saved {len(cards)} cards to: {output_file}")


if __name__ == "__main__":
    main()
