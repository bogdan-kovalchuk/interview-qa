# Step 3 & 4: LLM Extraction (Two-Step Process)

## Overview
Two-phase LLM processing:
1. **Step A:** Extract facts from text chunks
2. **Step B:** Convert facts to Anki cards

---

## Step A: Fact Extraction

### Goal
Extract ALL key facts, concepts, formulas, and common mistakes from text chunk.

### Input
Single text chunk (500-1000 words) from subtitles or PDF.

### Output
JSON array of facts:

```json
[
  {
    "type": "concept",
    "content": "Ohm's Law relates voltage, current, and resistance",
    "detail": "V = IR where V is voltage in volts, I is current in amps, R is resistance in ohms",
    "context": "Basic circuit analysis",
    "importance": "high"
  },
  {
    "type": "formula",
    "content": "Power formula: P = VI",
    "detail": "Power equals voltage times current",
    "context": "Circuit power calculations",
    "importance": "high"
  },
  {
    "type": "trap",
    "content": "Confusing series and parallel resistance calculations",
    "detail": "Series: R_total = R1 + R2. Parallel: 1/R_total = 1/R1 + 1/R2",
    "context": "Common student mistake",
    "importance": "medium"
  }
]
```

### Prompt Template (Step A)

```
You are extracting key facts from electronics course material for flashcard creation.

TEXT CHUNK:
{text}

Extract ALL important facts, concepts, formulas, definitions, and common mistakes/traps.

For each fact, provide:
- type: "concept" | "formula" | "fact" | "definition" | "trap"
- content: Brief statement of the fact
- detail: Additional context or explanation (1-2 sentences)
- context: Where/how this is used
- importance: "high" | "medium" | "low"

Output as JSON array. Be thorough - extract everything a student needs to know.
Do NOT summarize. Extract individual facts.

JSON OUTPUT:
```

### Implementation

```python
import json
import openai

def extract_facts(chunk_text, api_key):
    """Extract facts from text chunk using LLM."""
    
    prompt = f"""You are extracting key facts from electronics course material for flashcard creation.

TEXT CHUNK:
{chunk_text}

Extract ALL important facts, concepts, formulas, definitions, and common mistakes/traps.

For each fact, provide:
- type: "concept" | "formula" | "fact" | "definition" | "trap"
- content: Brief statement of the fact
- detail: Additional context or explanation (1-2 sentences)
- context: Where/how this is used
- importance: "high" | "medium" | "low"

Output as JSON array. Be thorough - extract everything a student needs to know.
Do NOT summarize. Extract individual facts.

JSON OUTPUT:"""
    
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        response_format={"type": "json_object"}
    )
    
    facts = json.loads(response.choices[0].message.content)
    return facts.get("facts", [])
```

### Batch Processing

```python
def process_all_chunks(chunks_file, api_key):
    """Process all chunks and extract facts."""
    
    with open(chunks_file) as f:
        data = json.load(f)
    
    all_facts = []
    
    for chunk in data["chunks"]:
        print(f"Processing chunk {chunk['chunk_index']}...")
        
        try:
            facts = extract_facts(chunk["text"], api_key)
            
            for fact in facts:
                fact["source"] = {
                    "section_id": data.get("section_id"),
                    "lecture_num": data.get("lecture_num"),
                    "chunk_index": chunk["chunk_index"]
                }
                all_facts.append(fact)
        
        except Exception as e:
            print(f"Error processing chunk {chunk['chunk_index']}: {e}")
            continue
    
    return all_facts
```

---

## Step B: Card Writing

### Goal
Convert each extracted fact into atomic Anki-style question/answer pair.

### Input
Single fact from Step A.

### Output
Tab-separated card:

```
What is Ohm's Law formula?	V = IR (Voltage = Current × Resistance)	Section_02,Ohm's_Law,Basic_Circuits
```

### Prompt Template (Step B)

```
Convert this fact into an atomic Anki flashcard.

FACT:
Type: {fact["type"]}
Content: {fact["content"]}
Detail: {fact["detail"]}
Context: {fact["context"]}

Create:
- Question: Specific, testable question (1 line)
- Answer: Concise answer (1-2 lines max)
- Tags: 3-5 relevant tags (comma-separated)

Output as tab-separated line:
Question\tAnswer\tTags

Rules:
- Question should test recall, not recognition
- Answer should be atomic (one fact)
- Use Ukrainian language for Q&A
- Tags should include section, topic, and subtopic
```

### Implementation

```python
def write_card(fact, api_key):
    """Convert fact to Anki card using LLM."""
    
    prompt = f"""Convert this fact into an atomic Anki flashcard.

FACT:
Type: {fact["type"]}
Content: {fact["content"]}
Detail: {fact["detail"]}
Context: {fact["context"]}

Create:
- Question: Specific, testable question (1 line)
- Answer: Concise answer (1-2 lines max)
- Tags: 3-5 relevant tags (comma-separated)

Output as tab-separated line:
Question\tAnswer\tTags

Rules:
- Question should test recall, not recognition
- Answer should be atomic (one fact)
- Use Ukrainian language for Q&A
- Tags should include section, topic, and subtopic"""
    
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    
    card_text = response.choices[0].message.content.strip()
    
    # Parse tab-separated output
    parts = card_text.split('\t')
    if len(parts) >= 3:
        return {
            "question": parts[0].strip(),
            "answer": parts[1].strip(),
            "tags": parts[2].strip()
        }
    
    return None
```

### Batch Processing

```python
def process_all_facts(facts, api_key):
    """Convert all facts to cards."""
    
    cards = []
    
    for fact in facts:
        try:
            card = write_card(fact, api_key)
            if card:
                card["source_fact"] = fact
                cards.append(card)
        except Exception as e:
            print(f"Error converting fact: {e}")
            continue
    
    return cards
```

---

## Complete Pipeline Script

```python
#!/usr/bin/env python3
"""
Two-step LLM extraction pipeline.
Step A: Extract facts from chunks
Step B: Convert facts to Anki cards
"""

import json
import openai
from pathlib import Path

API_KEY = "your-api-key-here"

def extract_facts(chunk_text):
    """Step A: Extract facts from text chunk."""
    # ... (see implementation above)
    pass

def write_card(fact):
    """Step B: Convert fact to Anki card."""
    # ... (see implementation above)
    pass

def main():
    # Load chunks
    chunks_file = "pipeline/output/subtitles/S02_L01.json"
    with open(chunks_file) as f:
        data = json.load(f)
    
    # Step A: Extract facts
    print("Step A: Extracting facts...")
    all_facts = []
    for chunk in data["chunks"]:
        facts = extract_facts(chunk["text"])
        all_facts.extend(facts)
    
    print(f"Extracted {len(all_facts)} facts")
    
    # Save intermediate results
    facts_file = "pipeline/output/facts/S02_L01_facts.json"
    Path(facts_file).parent.mkdir(parents=True, exist_ok=True)
    with open(facts_file, 'w') as f:
        json.dump(all_facts, f, indent=2, ensure_ascii=False)
    
    # Step B: Write cards
    print("Step B: Writing cards...")
    cards = []
    for fact in all_facts:
        card = write_card(fact)
        if card:
            cards.append(card)
    
    print(f"Generated {len(cards)} cards")
    
    # Save cards as tab-separated
    cards_file = "pipeline/output/cards/S02_L01_cards.txt"
    Path(cards_file).parent.mkdir(parents=True, exist_ok=True)
    with open(cards_file, 'w', encoding='utf-8') as f:
        for card in cards:
            f.write(f"{card['question']}\t{card['answer']}\t{card['tags']}\n")
    
    print(f"Saved to: {cards_file}")

if __name__ == "__main__":
    main()
```

---

## Error Handling

### Retry Logic
```python
import time

def llm_call_with_retry(prompt, max_retries=3):
    """Retry failed LLM calls."""
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(...)
            return response
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = 5 * (attempt + 1)
                print(f"Error: {e}. Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise
```

### Logging
```python
import logging

logging.basicConfig(
    filename='pipeline/logs/extraction.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info(f"Processed chunk {chunk_index}: {len(facts)} facts extracted")
```

---

## Verification

### Check Extracted Facts
```bash
cat pipeline/output/facts/S02_L01_facts.json | python -m json.tool | head -50
```

### Check Generated Cards
```bash
head -10 pipeline/output/cards/S02_L01_cards.txt
# Should show tab-separated: Question\tAnswer\tTags
```

### Quality Check
- Facts should be atomic (one concept per fact)
- Cards should be testable (question format)
- Tags should be consistent across section
