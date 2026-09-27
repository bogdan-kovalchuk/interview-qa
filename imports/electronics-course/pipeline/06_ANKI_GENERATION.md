# Step 5: Anki Package Generation

## Goal
Convert tab-separated cards into `.apkg` files (Anki deck packages).

## Output
- One `.apkg` file per section
- Deck naming: `Electronics and PCB Design::S01: Introduction to Electronics`
- Cards with proper tags and formatting

## Dependencies

```bash
pip install genanki
```

## Basic genanki Usage

```python
import genanki

# Create deck
deck = genanki.Deck(
    deck_id=1234567890,
    name="Electronics and PCB Design::S02: Introduction to Electronics"
)

# Create note (card)
note = genanki.Note(
    model=BASIC_MODEL,
    fields=["What is Ohm's Law?", "V = IR", "Section_02,Ohm's_Law"]
)

# Add note to deck
deck.add_note(note)

# Generate package
genanki.Package(deck).write_to_file("S02_Introduction_to_Electronics.apkg")
```

## Card Model

### Basic Model (Front/Back)
```python
BASIC_MODEL = genanki.Model(
    model_id=1607392319,
    name="Electronics Basic",
    fields=[
        {"name": "Question"},
        {"name": "Answer"},
        {"name": "Tags"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Question}}",
            "afmt": "{{FrontSide}}<hr id='answer'>{{Answer}}",
        },
    ],
    css="""
    .card {
        font-family: Arial, sans-serif;
        font-size: 16px;
        text-align: center;
        color: black;
        background-color: white;
    }
    .formula {
        font-family: 'Courier New', monospace;
        background-color: #f0f0f0;
        padding: 5px;
        border-radius: 3px;
    }
    """
)
```

## Conversion Script

```python
#!/usr/bin/env python3
"""
Generate .apkg files from tab-separated card files.
"""

import genanki
import hashlib
from pathlib import Path

# Model definition
BASIC_MODEL = genanki.Model(
    model_id=1607392319,
    name="Electronics Basic",
    fields=[
        {"name": "Question"},
        {"name": "Answer"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Question}}",
            "afmt": "{{FrontSide}}<hr id='answer'>{{Answer}}",
        },
    ],
    css="""
    .card {
        font-family: Arial, sans-serif;
        font-size: 16px;
        text-align: center;
        color: black;
        background-color: white;
    }
    """
)

SECTIONS = {
    "S01": "The Starting Line",
    "S02": "Introduction to Electronics",
    "S03": "Advanced Circuit Analysis",
    "S04": "Electrical Engineering 101",
    "S05": "Digital Logic Systems",
    "S06": "Digital Scale Integration",
    "S07": "PCB Design Technology",
    "S08": "CircuitMaker Projects",
    "S09": "Bonus Lectures",
}

def generate_deck_id(section_id):
    """Generate consistent deck ID from section ID."""
    return int(hashlib.md5(section_id.encode()).hexdigest()[:8], 16)

def load_cards(cards_file):
    """Load cards from tab-separated file."""
    cards = []
    with open(cards_file, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) >= 2:
                question = parts[0].strip()
                answer = parts[1].strip()
                cards.append((question, answer))
    return cards

def generate_apkg(section_id, cards, output_dir="pipeline/output/apkg"):
    """Generate .apkg file for a section."""
    
    deck_name = f"Electronics and PCB Design::{section_id}: {SECTIONS[section_id]}"
    deck_id = generate_deck_id(section_id)
    
    deck = genanki.Deck(deck_id=deck_id, name=deck_name)
    
    for question, answer in cards:
        note = genanki.Note(
            model=BASIC_MODEL,
            fields=[question, answer]
        )
        deck.add_note(note)
    
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Generate package
    filename = f"{section_id}_{SECTIONS[section_id].replace(' ', '_')}.apkg"
    output_file = output_path / filename
    
    package = genanki.Package(deck)
    package.write_to_file(str(output_file))
    
    print(f"Generated: {output_file} ({len(cards)} cards)")
    return output_file

def main():
    """Generate .apkg for all sections."""
    
    cards_dir = Path("pipeline/output/cards")
    
    for section_id in SECTIONS.keys():
        # Find all card files for this section
        card_files = list(cards_dir.glob(f"{section_id}_*.txt"))
        
        if not card_files:
            print(f"No cards found for {section_id}")
            continue
        
        # Load all cards for this section
        all_cards = []
        for card_file in card_files:
            cards = load_cards(card_file)
            all_cards.extend(cards)
            print(f"Loaded {len(cards)} cards from {card_file.name}")
        
        if all_cards:
            generate_apkg(section_id, all_cards)
        else:
            print(f"No cards to generate for {section_id}")

if __name__ == "__main__":
    main()
```

## Advanced: Multiple Card Types

### Card with Code/Formula Formatting
```python
CODE_MODEL = genanki.Model(
    model_id=1607392320,
    name="Electronics with Code",
    fields=[
        {"name": "Question"},
        {"name": "Answer"},
        {"name": "Code"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Question}}",
            "afmt": """
                {{FrontSide}}
                <hr id='answer'>
                {{Answer}}
                {{#Code}}
                <pre style="text-align: left; background: #f4f4f4; padding: 10px; border-radius: 5px;">
                    {{Code}}
                </pre>
                {{/Code}}
            """,
        },
    ],
    css="""
    .card {
        font-family: Arial, sans-serif;
        font-size: 16px;
        color: black;
        background-color: white;
    }
    """
)
```

## Tagging Strategy

### Add Tags to Cards
```python
def add_tags_to_card(question, answer, section_id, lecture_num, topic):
    """Generate tags for card."""
    tags = [
        section_id,
        f"L{lecture_num:02d}",
        topic.replace(" ", "_")
    ]
    return ",".join(tags)
```

### Filter by Tags in Anki
- Study specific section: `tag:S02`
- Study specific lecture: `tag:L05`
- Study specific topic: `tag:Ohm's_Law`

## Batch Processing with Progress

```python
from tqdm import tqdm

def generate_all_apkg():
    """Generate .apkg for all sections with progress bar."""
    
    cards_dir = Path("pipeline/output/cards")
    
    for section_id in tqdm(SECTIONS.keys(), desc="Generating decks"):
        card_files = list(cards_dir.glob(f"{section_id}_*.txt"))
        
        all_cards = []
        for card_file in card_files:
            cards = load_cards(card_file)
            all_cards.extend(cards)
        
        if all_cards:
            generate_apkg(section_id, all_cards)
```

## Output Structure

```
pipeline/output/
├── apkg/
│   ├── S01_The_Starting_Line.apkg
│   ├── S02_Introduction_to_Electronics.apkg
│   ├── S03_Advanced_Circuit_Analysis.apkg
│   └── ...
```

## Import to Anki

1. Open Anki
2. File → Import
3. Select `.apkg` file
4. Cards will be added to deck with specified name

## Verification

### Check Card Count
```python
import genanki

def check_apkg(apkg_file):
    """Check number of cards in .apkg file."""
    import sqlite3
    import zipfile
    import tempfile
    
    with zipfile.ZipFile(apkg_file, 'r') as z:
        with tempfile.TemporaryDirectory() as tmpdir:
            z.extractall(tmpdir)
            db_path = Path(tmpdir) / "collection.anki2"
            conn = sqlite3.connect(db_path)
            cursor = conn.execute("SELECT COUNT(*) FROM notes")
            count = cursor.fetchone()[0]
            print(f"{apkg_file}: {count} cards")
            conn.close()
```

### Manual Check
```bash
# List generated files
ls -lh pipeline/output/apkg/

# Check file size (should be > 0)
file S02_Introduction_to_Electronics.apkg
```

## Troubleshooting

### Problem: Cards not showing in Anki
**Solution:** Check model ID matches between generation and Anki

### Problem: Formatting lost
**Solution:** Ensure CSS is included in model definition

### Problem: Tags not working
**Solution:** Tags must be comma-separated, no spaces

## Dependencies
```bash
pip install genanki tqdm
```
