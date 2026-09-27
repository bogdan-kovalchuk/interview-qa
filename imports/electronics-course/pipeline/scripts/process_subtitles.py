#!/usr/bin/env python3
"""
Process subtitle files into structured JSON chunks.
"""

import json
import re
from pathlib import Path
from config import SECTIONS, SUBTITLES_DIR, get_subtitle_chunks_path, MAX_CHUNK_WORDS


def clean_subtitle(text):
    """Remove subtitle artifacts (timestamps, line numbers)."""
    lines = text.split('\n')
    cleaned = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if re.match(r'^\d+$', line):
            continue
        if re.match(r'^\d{2}:\d{2}:\d{2}', line):
            continue
        cleaned.append(line)
    return ' '.join(cleaned)


def chunk_text(text, max_words=MAX_CHUNK_WORDS):
    """Split text into chunks of max_words."""
    if not text or not text.strip():
        return []
    
    words = text.split()
    if len(words) <= max_words:
        return [text]
    
    chunks = []
    current = []
    count = 0
    
    for word in words:
        current.append(word)
        count += 1
        if count >= max_words:
            chunks.append(' '.join(current))
            current = []
            count = 0
    
    if current:
        chunks.append(' '.join(current))
    
    return chunks


def process_lecture_file(txt_file, section_id, lecture_num):
    """Process a single subtitle file."""
    text = txt_file.read_text(encoding='utf-8')
    cleaned = clean_subtitle(text)
    chunks = chunk_text(cleaned)
    
    output = {
        "section_id": section_id,
        "lecture_num": lecture_num,
        "source_file": str(txt_file),
        "chunks": []
    }
    
    for i, chunk in enumerate(chunks):
        output["chunks"].append({
            "chunk_index": i,
            "text": chunk,
            "word_count": len(chunk.split())
        })
    
    return output


def process_section(section_id):
    """Process all subtitle files in a section."""
    dir_name, _ = SECTIONS[section_id]
    section_path = SUBTITLES_DIR / dir_name
    
    if not section_path.exists():
        print(f"Warning: Section path not found: {section_path}")
        return None
    
    txt_files = sorted(section_path.glob("*.txt"))
    if not txt_files:
        print(f"Warning: No .txt files found in {section_path}")
        return None
    
    combined_output = {
        "section_id": section_id,
        "lectures": []
    }
    
    for txt_file in txt_files:
        lecture_match = re.search(r'(\d+)', txt_file.stem)
        lecture_num = int(lecture_match.group(1)) if lecture_match else 0
        
        lecture_data = process_lecture_file(txt_file, section_id, lecture_num)
        combined_output["lectures"].append(lecture_data)
        
        print(f"  Processed: {txt_file.name} ({len(lecture_data['chunks'])} chunks)")
    
    return combined_output


def main():
    """Process all sections."""
    print("Processing subtitles...\n")
    
    for section_id in SECTIONS.keys():
        dir_name, _ = SECTIONS[section_id]
        print(f"{section_id}: {dir_name}")
        
        result = process_section(section_id)
        if result:
            output_file = get_subtitle_chunks_path(section_id)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding='utf-8')
            print(f"  Saved to: {output_file.name}\n")
        else:
            print(f"  Skipped (no data)\n")


if __name__ == "__main__":
    main()
