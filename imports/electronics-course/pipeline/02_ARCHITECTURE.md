# Architecture: Two-Step LLM Extraction

## Core Principle
Split LLM work into two distinct phases to maximize quality and minimize context issues:

### Step A: Fact Extraction
**Goal:** Extract raw knowledge from source material
**Input:** Text chunk (subtitle segment or PDF section)
**Output:** Structured JSON array of facts

```json
[
  {
    "type": "concept|formula|fact|trap",
    "content": "Ohm's Law: V = IR",
    "context": "Basic circuit analysis",
    "importance": "high|medium|low"
  }
]
```

**Prompt Strategy:**
- Ask LLM to identify ALL facts, not summarize
- Categorize by type (concept, formula, fact, trap)
- Include context for each fact
- Rate importance level

### Step B: Card Writing
**Goal:** Convert each fact into atomic Anki card
**Input:** Single fact from Step A
**Output:** Question/Answer pair + tags

```
Q: What is Ohm's Law formula?
A: V = IR (Voltage = Current × Resistance)
Tags: Section_02, Ohm's_Law, Basic_Circuits
```

**Prompt Strategy:**
- One fact = one card (atomic)
- Question should be specific and testable
- Answer should be concise
- Include relevant tags

## Why Two Steps?

### Problems with Single-Step Approach
1. **Context overload:** LLM tries to process entire document at once
2. **Quality degradation:** Summarization loses details
3. **Inconsistent formatting:** Mixed extraction and formatting logic
4. **Hard to debug:** Can't isolate extraction vs formatting issues

### Benefits of Two-Step Approach
1. **Focused prompts:** Each step has clear, narrow goal
2. **Better quality:** Facts extracted first, then optimized for Anki format
3. **Debuggable:** Can inspect extracted facts before card generation
4. **Reusable:** Same facts can generate different card types
5. **Scalable:** Process chunks independently

## Data Flow

```
Source Material
    ↓
[Chunker] → Text chunks (500-1000 words each)
    ↓
[Step A: Extract Facts] → JSON facts array
    ↓
[Step B: Write Cards] → Tab-separated cards
    ↓
[Anki Generator] → .apkg file
```

## Chunking Strategy

### Subtitles
- Split by lecture (each `.txt` file = one lecture)
- Further split if > 1000 words
- Preserve lecture boundaries

### PDF
- Split by chapter/section headings
- Each chunk = 500-1000 words
- Maintain section context in metadata

## Error Handling
- Retry failed LLM calls (3 attempts)
- Log failed chunks for manual review
- Continue processing remaining chunks
- Generate partial `.apkg` with successful cards

## File Naming Convention
- Extracted facts: `facts_S{section_num}_L{lecture_num}.json`
- Generated cards: `cards_S{section_num}_L{lecture_num}.txt`
- Final deck: `S{section_num}_{section_name}.apkg`
