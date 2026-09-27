# Pipeline: Subtitles + PDF → Anki Decks (.apkg)

## Overview
Automated pipeline to convert course subtitles and textbook PDF into structured Anki flashcard decks.

**LLM:** Qwen3.7 Plus via OpenCode Go API (Anthropic-compatible)

**Input:**
- Subtitles: `.txt` files in `subtitles/Section N - <title>/`
- Textbook: `books/Design_Game_Console_013.pdf` (relative to the course root)

**Output:**
- `.apkg` files (one per section)
- Deck naming: `Electronics and PCB Design::S01: The Starting Line`

## Pipeline Steps

### Step 1: Subtitle Processing
- Read `.txt` subtitle files
- Clean artifacts (timestamps, line numbers)
- Split into chunks (~800 words each)
- Store as `pipeline/output/subtitles/{section_id}_chunks.json`

### Step 2: PDF Processing (Optional)
- Convert PDF to text using PyMuPDF
- Detect chapters/sections
- Chunk by structure (~800 words each)
- Store as `pipeline/output/pdf/textbook_chunks.json`

### Step 3: LLM Fact Extraction (Step A)
- Process each chunk through Qwen3.7 Plus
- Extract key facts, concepts, formulas, traps
- Store as `pipeline/output/facts/{section_id}_facts.json`

### Step 4: LLM Card Writing (Step B)
- Convert each fact to atomic Anki card
- Generate Q&A pairs in Ukrainian
- Store as `pipeline/output/cards/{section_id}_cards.txt`

### Step 5: Anki Package Generation
- Convert cards to `.apkg` format
- One deck per section
- Output: `pipeline/output/apkg/{section_id}_{name}.apkg`

## File Structure
```
pipeline/
├── 00_QUICK_START.md          # Quick start guide
├── 01_README.md               # This file
├── 02_ARCHITECTURE.md         # Two-step LLM architecture
├── 03_SUBTITLE_PROCESSING.md  # Subtitle processing details
├── 04_PDF_PROCESSING.md       # PDF processing details
├── 05_LLM_EXTRACTION.md       # LLM extraction prompts
├── 06_ANKI_GENERATION.md      # Anki package generation
├── requirements.txt           # Python dependencies
├── logs/                      # Pipeline logs
├── output/                    # Generated files
│   ├── subtitles/             # Chunked subtitle data
│   ├── pdf/                   # Chunked PDF data
│   ├── facts/                 # Extracted facts (Step A)
│   ├── cards/                 # Generated cards (Step B)
│   └── apkg/                  # Final Anki decks
└── scripts/
    ├── anki_model.py          # Anki note model definition
    ├── config.py              # Configuration (paths, sections, LLM)
    ├── llm_client.py          # Qwen3.7 Plus API client
    ├── process_subtitles.py   # Step 1: Subtitle processing
    ├── process_pdf.py         # Step 2: PDF processing
    ├── extract_facts.py       # Step 3: LLM fact extraction
    ├── filter_facts.py        # Step 3b: fact filtering
    ├── write_cards.py         # Step 4: LLM card writing
    ├── generate_apkg.py       # Step 5: Anki package generation
    └── run_pipeline.py        # Master orchestrator
```

## Quick Start
```bash
# Install dependencies
pip install -r pipeline/requirements.txt

# Get API key from https://opencode.ai/auth

# Process single section
python pipeline/scripts/run_pipeline.py --section S02 --api-key YOUR_OPENCODE_GO_KEY

# Process all sections
python pipeline/scripts/run_pipeline.py --all --api-key YOUR_OPENCODE_GO_KEY

# Include PDF textbook
python pipeline/scripts/run_pipeline.py --all --pdf --api-key YOUR_OPENCODE_GO_KEY
```

## LLM Configuration

Pipeline uses **Qwen3.7 Plus** via OpenCode Go:
- **Model**: `qwen3.7-plus`
- **Endpoint**: `https://opencode.ai/zen/go/v1/messages`
- **API Format**: Anthropic-compatible (Messages API)
- **Limits**: 4,300 requests per 5 hours
- **Pricing**: $0.40/1M input tokens, $1.60/1M output tokens

### Estimated Costs
For full course (161 lectures):
- ~966 API calls total
- **Total cost: ~$0.50-1.00** (much cheaper than OpenAI GPT-4)

## Manual Step-by-Step
```bash
# Step 1: Process subtitles
python pipeline/scripts/process_subtitles.py

# Step 2: Process PDF (optional)
python pipeline/scripts/process_pdf.py

# Step 3: Extract facts
python pipeline/scripts/extract_facts.py --section S02 --api-key YOUR_KEY

# Step 4: Write cards
python pipeline/scripts/write_cards.py --section S02 --api-key YOUR_KEY

# Step 5: Generate Anki package
python pipeline/scripts/generate_apkg.py --section S02
```

## Configuration
Edit `pipeline/scripts/config.py` to customize:
- Section names and paths
- Chunk sizes
- LLM model and parameters
- Anki model settings

## Dependencies
```bash
pip install PyMuPDF genanki httpx
```

## Output Structure
```
pipeline/output/
├── subtitles/
│   ├── S01_chunks.json
│   ├── S02_chunks.json
│   └── ...
├── pdf/
│   └── textbook_chunks.json
├── facts/
│   ├── S01_facts.json
│   ├── S02_facts.json
│   └── ...
├── cards/
│   ├── S01_cards.txt
│   ├── S02_cards.txt
│   └── ...
└── apkg/
    ├── S01_The_Starting_Line.apkg
    ├── S02_Introduction_to_Electronics.apkg
    └── ...
```

## Import to Anki
1. Open Anki desktop app
2. File → Import
3. Select `.apkg` file from `pipeline/output/apkg/`
4. Cards will be added to deck
