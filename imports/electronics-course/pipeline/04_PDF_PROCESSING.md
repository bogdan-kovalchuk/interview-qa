# Step 2: PDF Processing

## Challenge
**Problem:** Cannot load entire PDF (500+ pages) into LLM context
**Solution:** Convert PDF to structured text locally, then chunk for LLM processing

## Approach

### 2.1 PDF to Text Conversion
Use local tools (NOT LLM) to extract text:

**Option A: PyMuPDF (fitz)** - Recommended
```python
import fitz  # PyMuPDF

def extract_pdf_text(pdf_path):
    doc = fitz.open(pdf_path)
    pages = []
    for page in doc:
        text = page.get_text()
        pages.append({
            "page_num": page.number + 1,
            "text": text
        })
    return pages
```

**Option B: pdfplumber** - Better for tables
```python
import pdfplumber

def extract_pdf_text(pdfplumber_path):
    pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            pages.append({
                "page_num": i + 1,
                "text": text
            })
    return pages
```

**Option C: PyPDF2** - Simple but less reliable
```python
import PyPDF2

def extract_pdf_text(pdf_path):
    reader = PyPDF2.PdfReader(pdf_path)
    pages = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        pages.append({
            "page_num": i + 1,
            "text": text
        })
    return pages
```

### 2.2 Structure Detection
Identify chapters/sections from text:

```python
import re

def detect_structure(pages):
    """Detect chapter/section headings."""
    structure = []
    
    for page in pages:
        text = page["text"]
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            
            # Detect chapter headings (e.g., "Chapter 1", "CHAPTER ONE")
            if re.match(r'^(Chapter|CHAPTER)\s+\d+', line):
                structure.append({
                    "type": "chapter",
                    "title": line,
                    "page": page["page_num"]
                })
            
            # Detect section headings (e.g., "1.1 Introduction", "Section 2")
            elif re.match(r'^\d+\.\d+\s+[A-Z]', line):
                structure.append({
                    "type": "section",
                    "title": line,
                    "page": page["page_num"]
                })
    
    return structure
```

### 2.3 Chunking Strategy
Split PDF into logical chunks by structure:

```python
def chunk_by_structure(pages, structure, max_words=800):
    """Chunk PDF by detected structure."""
    chunks = []
    current_chunk = []
    current_words = 0
    current_section = None
    
    for page in pages:
        text = page["text"]
        words = text.split()
        
        # Check if new section starts on this page
        for item in structure:
            if item["page"] == page["page_num"]:
                # Save current chunk if exists
                if current_chunk:
                    chunks.append({
                        "text": ' '.join(current_chunk),
                        "section": current_section,
                        "word_count": current_words
                    })
                    current_chunk = []
                    current_words = 0
                
                current_section = item["title"]
        
        # Add text to current chunk
        current_chunk.extend(words)
        current_words += len(words)
        
        # Split if too large
        if current_words >= max_words:
            chunks.append({
                "text": ' '.join(current_chunk),
                "section": current_section,
                "word_count": current_words
            })
            current_chunk = []
            current_words = 0
    
    # Final chunk
    if current_chunk:
        chunks.append({
            "text": ' '.join(current_chunk),
            "section": current_section,
            "word_count": current_words
        })
    
    return chunks
```

### 2.4 Text Cleaning
Remove PDF artifacts:

```python
def clean_pdf_text(text):
    """Clean PDF extraction artifacts."""
    # Remove page numbers
    text = re.sub(r'\n\d+\n', '\n', text)
    
    # Remove headers/footers (repeated lines)
    lines = text.split('\n')
    cleaned = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Skip common header/footer patterns
        if re.match(r'^(Page|©|Copyright)', line):
            continue
        cleaned.append(line)
    
    return ' '.join(cleaned)
```

### 2.5 Output Format
Store as JSON:

```json
{
  "source_file": "Design_Game_Console_013.pdf",
  "total_pages": 523,
  "structure": [
    {"type": "chapter", "title": "Chapter 1", "page": 1},
    {"type": "section", "title": "1.1 Introduction", "page": 3}
  ],
  "chunks": [
    {
      "chunk_index": 0,
      "text": "Chapter 1 covers...",
      "section": "Chapter 1",
      "word_count": 750,
      "pages": [1, 2, 3]
    }
  ]
}
```

### 2.6 Output Location
```
pipeline/output/
├── pdf/
│   ├── textbook_full.json
│   └── textbook_chunks.json
```

## Script: `process_pdf.py`

```python
#!/usr/bin/env python3
"""
Process PDF textbook into structured JSON chunks.
"""

import json
import re
from pathlib import Path
import fitz  # PyMuPDF

PDF_PATH = "C:/Users/bogdan/Documents/Projects/learning/course-electronics-and-pcb-design/books/Design_Game_Console_013.pdf"
OUTPUT_DIR = Path("pipeline/output/pdf")

def extract_pdf_text(pdf_path):
    """Extract text from all pages."""
    doc = fitz.open(pdf_path)
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

def chunk_by_structure(pages, structure, max_words=800):
    """Chunk PDF by structure."""
    chunks = []
    current_chunk = []
    current_words = 0
    current_section = None
    current_pages = []
    
    for page in pages:
        text = clean_pdf_text(page["text"])
        words = text.split()
        
        # Check for new section
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
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    print(f"Extracting text from PDF: {PDF_PATH}")
    pages = extract_pdf_text(PDF_PATH)
    print(f"Extracted {len(pages)} pages")
    
    print("Detecting structure...")
    structure = detect_structure(pages)
    print(f"Found {len(structure)} sections/chapters")
    
    print("Chunking by structure...")
    chunks = chunk_by_structure(pages, structure)
    print(f"Created {len(chunks)} chunks")
    
    # Save full output
    output = {
        "source_file": PDF_PATH,
        "total_pages": len(pages),
        "structure": structure,
        "chunks": chunks
    }
    
    output_file = OUTPUT_DIR / "textbook_chunks.json"
    output_file.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    print(f"Saved to: {output_file}")

if __name__ == "__main__":
    main()
```

## Dependencies
```bash
pip install PyMuPDF
```

## Usage
```bash
cd "C:\Users\bogdan\Documents\Projects\learning\course-electronics-and-pcb-design"
python pipeline/scripts/process_pdf.py
```

## Verification
```bash
# Check output
ls pipeline/output/pdf/
cat pipeline/output/pdf/textbook_chunks.json | python -m json.tool | head -50
```

## Notes
- **Do NOT** load entire PDF into LLM context
- Process locally first, then feed chunks to LLM
- Adjust `max_words` based on LLM context limits
- Preserve page numbers for source tracking
