# Quick Start Guide

## Installation

```bash
cd "C:\Users\bogdan\Documents\Projects\learning\course-electronics-and-pcb-design"

# Install dependencies
pip install -r pipeline/requirements.txt
```

## Отримання API ключа OpenCode Go

1. Зареєструйтесь на [opencode.ai/auth](https://opencode.ai/auth)
2. Підпишіться на Go ($5 перший місяць, потім $10/місяць)
3. Скопіюйте API ключ з console
4. Використовуйте цей ключ для запуску pipeline

## Quick Test (Single Section)

```bash
# Process Section 2 only
python pipeline/scripts/run_pipeline.py --section S02 --api-key YOUR_OPENCODE_GO_KEY
```

## Full Pipeline

```bash
# Process all sections (subtitles only)
python pipeline/scripts/run_pipeline.py --all --api-key YOUR_OPENCODE_GO_KEY

# Include PDF textbook
python pipeline/scripts/run_pipeline.py --all --pdf --api-key YOUR_OPENCODE_GO_KEY
```

## Manual Step-by-Step

### 1. Process Subtitles
```bash
python pipeline/scripts/process_subtitles.py
```
Output: `pipeline/output/subtitles/S{XX}_chunks.json`

### 2. Process PDF (Optional)
```bash
python pipeline/scripts/process_pdf.py
```
Output: `pipeline/output/pdf/textbook_chunks.json`

### 3. Extract Facts (Step A)
```bash
python pipeline/scripts/extract_facts.py --section S02 --api-key YOUR_OPENCODE_GO_KEY
```
Output: `pipeline/output/facts/S{XX}_facts.json`

### 4. Write Cards (Step B)
```bash
python pipeline/scripts/write_cards.py --section S02 --api-key YOUR_OPENCODE_GO_KEY
```
Output: `pipeline/output/cards/S{XX}_cards.txt`

### 5. Generate Anki Package
```bash
python pipeline/scripts/generate_apkg.py --section S02
```
Output: `pipeline/output/apkg/S02_Introduction_to_Electronics.apkg`

## Output Structure

```
pipeline/output/
├── subtitles/          # Chunked subtitle data
│   ├── S01_chunks.json
│   ├── S02_chunks.json
│   └── ...
├── pdf/               # Chunked PDF data
│   └── textbook_chunks.json
├── facts/             # Extracted facts (Step A)
│   ├── S01_facts.json
│   ├── S02_facts.json
│   └── ...
├── cards/             # Generated cards (Step B)
│   ├── S01_cards.txt
│   ├── S02_cards.txt
│   └── ...
└── apkg/              # Final Anki decks
    ├── S01_The_Starting_Line.apkg
    ├── S02_Introduction_to_Electronics.apkg
    └── ...
```

## Import to Anki

1. Open Anki desktop app
2. File → Import
3. Select `.apkg` file from `pipeline/output/apkg/`
4. Cards will be added to deck

## LLM Configuration

Pipeline використовує **Qwen3.7 Plus** через **OpenCode Go API**:
- Model: `qwen3.7-plus`
- Endpoint: `https://opencode.ai/zen/go/v1/messages`
- Ліміт: 4,300 requests per 5 hours
- Ціна: $0.40/1M input tokens, $1.60/1M output tokens

### Очікувана вартість для всього курсу:
- ~161 лекція × ~3 chunks × ~2 LLM calls = ~966 API calls
- Вартість: ~$0.50-1.00 (значно дешевше за OpenAI GPT-4)

## Troubleshooting

### "Internal server error" from opencode
- Це тимчасова помилка на стороні сервера
- opencode автоматично повторює запит (до 3 разів)
- Якщо повторюється, перевірте інтернет-з'єднання

### API rate limit errors
- OpenCode Go має ліміт 4,300 requests per 5 hours
- Для всього курсу потрібно ~966 calls — вкладається в ліміт
- Якщо перевищено, зачекайте або використовуйте `--resume` flag

### PDF extraction fails
- Ensure PyMuPDF is installed: `pip install PyMuPDF`
- Check PDF file path is correct
- Some PDFs may have protected text (scanned images)

### Cards not showing in Anki
- Verify `.apkg` file size > 0
- Check model ID matches
- Try re-importing the file

## Next Steps

1. Отримайте API ключ OpenCode Go
2. Test with one section first
3. Review generated cards for quality
4. Run full pipeline
5. Import to Anki and start studying!
