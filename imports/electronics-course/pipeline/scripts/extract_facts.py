#!/usr/bin/env python3
"""
Step A: Extract facts from text chunks using Qwen3.7 Plus via OpenCode Go.
Supports incremental saving and resume.
"""

import json
import argparse
import logging
from pathlib import Path
from config import (
    get_subtitle_chunks_path, get_pdf_chunks_path, get_facts_path,
    LLM_TEMPERATURE_FACTS, LOGS_DIR
)
from llm_client import call_llm_json

LOGS_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOGS_DIR / 'extraction.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)


FACT_EXTRACTION_PROMPT = """You are extracting TECHNICAL facts from electronics course subtitles for Anki flashcards.

TEXT CHUNK:
{text}

Extract ONLY 3-5 technical facts per chunk about ELECTRONICS CONCEPTS.

EXTRACT ONLY:
- Electronic components (resistors, capacitors, transistors, diodes, etc.)
- Circuit laws and formulas (Ohm's law, Kirchhoff's laws, power calculations)
- Circuit analysis techniques (series/parallel, voltage dividers, Thevenin)
- Electrical units and measurements (voltage, current, resistance, power)
- Practical circuit design principles
- Common circuit mistakes and how to avoid them

DO NOT EXTRACT (skip completely):
- Information about the course itself ("this course covers...", "the instructor...")
- Book recommendations or references
- Teaching methodology or approach
- Student prerequisites or background
- General advice without technical content
- Historical information about electronics

For each fact:
- type: "concept" | "formula" | "trap" | "definition"
- content: Brief technical statement (1 sentence)
- detail: Why it matters technically (1 sentence)
- importance: "critical" | "important" | "nice-to-know"

Output as JSON:
{{"facts": [{{"type": "...", "content": "...", "detail": "...", "importance": "..."}}]}}

JSON OUTPUT:"""


def extract_facts_from_text(chunk_text, api_key):
    """Extract facts from text chunk using LLM."""
    prompt = FACT_EXTRACTION_PROMPT.format(text=chunk_text)
    
    try:
        result = call_llm_json(prompt, api_key, LLM_TEMPERATURE_FACTS)
        return result.get("facts", [])
    except Exception as e:
        logging.error(f"Failed to extract facts: {e}")
        raise


def _save_checkpoint(facts, output_file):
    """Save current facts to disk."""
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(json.dumps(facts, indent=2, ensure_ascii=False), encoding='utf-8')


def _load_checkpoint(output_file):
    """Load existing facts from disk for resume."""
    if output_file.exists():
        try:
            with open(output_file, encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, Exception):
            return []
    return []


def extract_facts_from_chunks(chunks_file, api_key, source_type="subtitle", resume=True):
    """Process all chunks in a file and extract facts with checkpointing."""
    output_file = get_facts_path(chunks_file.stem.split("_")[0])
    
    with open(chunks_file, encoding='utf-8') as f:
        data = json.load(f)
    
    all_facts = _load_checkpoint(output_file) if resume else []
    processed_chunks = set()
    for fact in all_facts:
        src = fact.get("source", {})
        key = (src.get("lecture_num"), src.get("chunk_index"))
        processed_chunks.add(key)
    
    if processed_chunks:
        logging.info(f"Resuming: {len(processed_chunks)} chunks done, {len(all_facts)} facts collected")
    
    if source_type == "subtitle":
        lectures = data.get("lectures", [])
        
        for lecture in lectures:
            lecture_num = lecture.get("lecture_num", 0)
            chunks = lecture.get("chunks", [])
            
            all_done = all(
                (lecture_num, c.get("chunk_index", 0)) in processed_chunks
                for c in chunks
            )
            if all_done:
                logging.info(f"Lecture {lecture_num}: already done, skipping")
                continue
            
            for chunk in chunks:
                chunk_idx = chunk.get("chunk_index", 0)
                
                if (lecture_num, chunk_idx) in processed_chunks:
                    continue
                
                logging.info(f"Processing lecture {lecture_num}, chunk {chunk_idx}...")
                
                try:
                    facts = extract_facts_from_text(chunk["text"], api_key)
                    
                    for fact in facts:
                        fact["source"] = {
                            "section_id": data.get("section_id"),
                            "lecture_num": lecture_num,
                            "chunk_index": chunk_idx
                        }
                        all_facts.append(fact)
                    
                    logging.info(f"  Extracted {len(facts)} facts (total: {len(all_facts)})")
                    _save_checkpoint(all_facts, output_file)
                
                except Exception as e:
                    logging.error(f"Error processing lecture {lecture_num} chunk {chunk_idx}: {e}")
                    _save_checkpoint(all_facts, output_file)
                    continue
    
    else:
        chunks = data.get("chunks", [])
        
        for chunk in chunks:
            chunk_idx = chunk.get("chunk_index", 0)
            section = chunk.get("section", "Unknown")
            
            if chunk_idx in {f.get("source", {}).get("chunk_index") for f in all_facts}:
                continue
            
            logging.info(f"Processing PDF chunk {chunk_idx} ({section})...")
            
            try:
                facts = extract_facts_from_text(chunk["text"], api_key)
                
                for fact in facts:
                    fact["source"] = {
                        "type": "pdf",
                        "chunk_index": chunk_idx,
                        "section": section
                    }
                    all_facts.append(fact)
                
                logging.info(f"  Extracted {len(facts)} facts (total: {len(all_facts)})")
                _save_checkpoint(all_facts, output_file)
            
            except Exception as e:
                logging.error(f"Error processing chunk {chunk_idx}: {e}")
                _save_checkpoint(all_facts, output_file)
                continue
    
    return all_facts


def main():
    parser = argparse.ArgumentParser(description="Extract facts from chunks (Step A)")
    parser.add_argument("--input", type=str, help="Input chunks JSON file")
    parser.add_argument("--output", type=str, help="Output facts JSON file")
    parser.add_argument("--section", type=str, help="Section ID (e.g., S02)")
    parser.add_argument("--api-key", type=str, required=True, help="OpenCode Go API key")
    parser.add_argument("--include-pdf", action="store_true", help="Include PDF chunks")
    parser.add_argument("--no-resume", action="store_true", help="Start from scratch")
    
    args = parser.parse_args()
    
    if args.section:
        input_file = get_subtitle_chunks_path(args.section)
        output_file = get_facts_path(args.section)
        source_type = "subtitle"
    elif args.input and args.output:
        input_file = Path(args.input)
        output_file = Path(args.output)
        source_type = "pdf" if "pdf" in str(input_file).lower() else "subtitle"
    else:
        parser.error("Provide --section or both --input and --output")
    
    logging.info(f"Extracting facts from: {input_file}")
    
    all_facts = extract_facts_from_chunks(input_file, args.api_key, source_type, resume=not args.no_resume)
    
    if args.include_pdf:
        pdf_file = get_pdf_chunks_path()
        if pdf_file.exists():
            logging.info(f"Also extracting from PDF: {pdf_file}")
            pdf_facts = extract_facts_from_chunks(pdf_file, args.api_key, source_type="pdf", resume=not args.no_resume)
            all_facts.extend(pdf_facts)
    
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(json.dumps(all_facts, indent=2, ensure_ascii=False), encoding='utf-8')
    logging.info(f"Done! Saved {len(all_facts)} facts to: {output_file}")


if __name__ == "__main__":
    main()
