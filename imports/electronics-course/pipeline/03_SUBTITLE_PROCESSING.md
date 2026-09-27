# Step 1: Subtitle Processing

## Input
- Location: `subtitles/Section_X/`
- Format: `.txt` files (one per lecture)
- Naming: `lecture_XX.txt` or similar

## Processing Steps

### 1.1 File Discovery
```python
import glob
from pathlib import Path

sections = {
    "S01": "subtitles/Section 1 - The Starting Line",
    "S02": "subtitles/Section 2 - Introduction to Electronics",
    # ... etc
}

def find_subtitle_files(section_path):
    return list(Path(section_path).glob("*.txt"))
```

### 1.2 Text Cleaning
Remove subtitle artifacts:
- Timestamps (if present)
- Line numbers
- Duplicate lines (common in VTT→TXT conversion)
- Excessive whitespace

```python
def clean_subtitle(text):
    lines = text.split('\n')
    cleaned = []
    for line in lines:
        # Skip timestamps and line numbers
        if re.match(r'^\d+$', line.strip()):
            continue
        if re.match(r'^\d{2}:\d{2}:\d{2}', line.strip()):
            continue
        if line.strip():
            cleaned.append(line.strip())
    return ' '.join(cleaned)
```

### 1.3 Chunking Strategy
**Goal:** Split into 500-1000 word chunks for LLM processing

```python
def chunk_text(text, max_words=800):
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0
    
    for word in words:
        current_chunk.append(word)
        current_length += 1
        
        if current_length >= max_words:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_length = 0
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks
```

**Edge Cases:**
- If lecture < 500 words: keep as single chunk
- If lecture > 2000 words: split into multiple chunks
- Preserve sentence boundaries when possible

### 1.4 Metadata Extraction
Extract from filename/path:
- Section number
- Lecture number
- Lecture title (if available)

```python
def extract_metadata(filepath, section_id):
    filename = Path(filepath).stem
    # Parse lecture number from filename
    lecture_match = re.search(r'(\d+)', filename)
    lecture_num = int(lecture_match.group(1)) if lecture_match else 0
    
    return {
        "section_id": section_id,
        "lecture_num": lecture_num,
        "source_file": str(filepath),
        "chunk_index": 0  # Updated during chunking
    }
```

### 1.5 Output Format
Store as JSON for processing:

```json
{
  "section_id": "S02",
  "lecture_num": 5,
  "source_file": "subtitles/Section 2/lecture_05.txt",
  "chunks": [
    {
      "chunk_index": 0,
      "text": "Today we'll discuss resistors...",
      "word_count": 750,
      "metadata": {
        "section_id": "S02",
        "lecture_num": 5,
        "chunk_index": 0
      }
    }
  ]
}
```

### 1.6 Output Location
```
pipeline/output/
├── subtitles/
│   ├── S01_L01.json
│   ├── S02_L01.json
│   ├── S02_L02.json
│   └── ...
```

## Script: `process_subtitles.py`

```python
#!/usr/bin/env python3
"""
Process subtitle files into structured JSON chunks.
"""

import json
import re
from pathlib import Path

SECTIONS = {
    "S01": "Section 1 - The Starting Line",
    "S02": "Section 2 - Introduction to Electronics",
    "S03": "Section 3 - Advanced Circuit Analysis",
    "S04": "Section 4 - Electrical Engineering 101",
    "S05": "Section 5 - Digital Logic Systems",
    "S06": "Section 6 - Digital Scale Integration",
    "S07": "Section 7 - PCB Design Technology",
    "S08": "Section 8 - CircuitMaker Projects",
    "S09": "Section 9 - Bonus Lectures",
}

def clean_subtitle(text):
    """Remove subtitle artifacts."""
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

def chunk_text(text, max_words=800):
    """Split text into chunks of max_words."""
    words = text.split()
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

def process_section(section_id, section_path):
    """Process all subtitle files in a section."""
    base_path = Path("subtitles") / section_path
    output_dir = Path("pipeline/output/subtitles")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for txt_file in sorted(base_path.glob("*.txt")):
        # Read and clean
        text = txt_file.read_text(encoding='utf-8')
        cleaned = clean_subtitle(text)
        
        # Extract metadata
        lecture_match = re.search(r'(\d+)', txt_file.stem)
        lecture_num = int(lecture_match.group(1)) if lecture_match else 0
        
        # Chunk
        chunks = chunk_text(cleaned)
        
        # Build output
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
                "word_count": len(chunk.split()),
                "metadata": {
                    "section_id": section_id,
                    "lecture_num": lecture_num,
                    "chunk_index": i
                }
            })
        
        # Write output
        output_file = output_dir / f"{section_id}_L{lecture_num:02d}.json"
        output_file.write_text(json.dumps(output, indent=2, ensure_ascii=False))
        print(f"Processed: {txt_file.name} → {output_file.name} ({len(chunks)} chunks)")

if __name__ == "__main__":
    for section_id, section_name in SECTIONS.items():
        print(f"\nProcessing {section_id}: {section_name}")
        process_section(section_id, section_name)
```

## Usage
```bash
cd "C:\Users\bogdan\Documents\Projects\learning\course-electronics-and-pcb-design"
python pipeline/scripts/process_subtitles.py
```

## Verification
Check output:
```bash
ls pipeline/output/subtitles/
# Should show: S01_L01.json, S02_L01.json, etc.

# Check content
cat pipeline/output/subtitles/S02_L01.json | python -m json.tool | head -30
```
