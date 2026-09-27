#!/usr/bin/env python3
"""
Process PDF textbook into structured JSON chunks.
"""

import json
import re
import logging
from pathlib import Path

try:
    import fitz
except ImportError:
    print("Error: PyMuPDF not installed. Run: pip install PyMuPDF")
    exit(1)

from config import PDF_PATH, get_pdf_chunks_path, MAX_CHUNK_WORDS, LOGS_DIR

LOGS_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOGS_DIR / 'extraction.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)


def extract_pdf_text(pdf_path):
    """Extract text from all pages using PyMuPDF."""
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        logging.error(f"Failed to open PDF: {e}")
        raise
    
    pages = []
    for page in doc:
        text = page.get_text()
        pages.append({
            "page_num": page.number + 1,
            "text": text
        })
    return pages


def detect_structure(pages):
    """Detect chapter/section headings."""
    structure = []
    for page in pages:
        lines = page["text"].split('\n')
        for line in lines:
            line = line.strip()
            if re.match(r'^(Chapter|CHAPTER)\s+\d+', line):
                structure.append({
                    "type": "chapter",
                    "title": line,
                    "page": page["page_num"]
                })
            elif re.match(r'^\d+\.\d+\s+[A-Z]', line):
                structure.append({
                    "type": "section",
                    "title": line,
                    "page": page["page_num"]
                })
    return structure


def clean_pdf_text(text):
    """Clean PDF artifacts."""
    text = re.sub(r'\n\d+\n', '\n', text)
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    return ' '.join(lines)


def chunk_by_structure(pages, structure, max_words=MAX_CHUNK_WORDS):
    """Chunk PDF by detected structure."""
    chunks = []
    current_chunk = []
    current_words = 0
    current_section = None
    current_pages = []
    
    for page in pages:
        text = clean_pdf_text(page["text"])
        words = text.split()
        
        for item in structure:
            if item["page"] == page["page_num"]:
                if current_chunk:
                    chunks.append({
                        "text": ' '.join(current_chunk),
                        "section": current_section,
                        "word_count": current_words,
                        "pages": current_pages
                    })
                    current_chunk = []
                    current_words = 0
                    current_pages = []
                current_section = item["title"]
        
        current_chunk.extend(words)
        current_words += len(words)
        current_pages.append(page["page_num"])
        
        if current_words >= max_words:
            chunks.append({
                "text": ' '.join(current_chunk),
                "section": current_section,
                "word_count": current_words,
                "pages": current_pages
            })
            current_chunk = []
            current_words = 0
            current_pages = []
    
    if current_chunk:
        chunks.append({
            "text": ' '.join(current_chunk),
            "section": current_section,
            "word_count": current_words,
            "pages": current_pages
        })
    
    return chunks


def main():
    """Process PDF textbook."""
    if not PDF_PATH.exists():
        logging.error(f"PDF not found at {PDF_PATH}")
        return
    
    logging.info(f"Extracting text from PDF: {PDF_PATH.name}")
    pages = extract_pdf_text(PDF_PATH)
    logging.info(f"Extracted {len(pages)} pages")
    
    logging.info("Detecting structure...")
    structure = detect_structure(pages)
    logging.info(f"Found {len(structure)} sections/chapters")
    
    logging.info("Chunking by structure...")
    chunks = chunk_by_structure(pages, structure)
    logging.info(f"Created {len(chunks)} chunks")
    
    output = {
        "source_file": str(PDF_PATH),
        "total_pages": len(pages),
        "structure": structure,
        "chunks": []
    }
    
    for i, chunk in enumerate(chunks):
        output["chunks"].append({
            "chunk_index": i,
            "text": chunk["text"],
            "section": chunk["section"],
            "word_count": chunk["word_count"],
            "pages": chunk["pages"]
        })
    
    output_file = get_pdf_chunks_path()
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding='utf-8')
    logging.info(f"Saved to: {output_file}")


if __name__ == "__main__":
    main()
