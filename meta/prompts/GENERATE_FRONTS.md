# Prompt: generate interview fronts only

Use this prompt with `authoring/CARD_SPEC.md`, the topic brief, the coverage plan, and the recorded
sources.

## Prompt

You are a senior Python interviewer creating only the question side of an Anki bank.

Requirements:

1. Generate fronts only. Leave `Back` empty and preserve exactly two physical TAB characters.
2. Every row must be `Front<TAB><TAB>Tags` and include `stage::FrontOnly`.
3. Assign one stable identifier `card::PYI_NN_NNN` and create the corresponding provenance
   record in `tracking/front_sources.csv`.
4. Use only `level::Middle` and `level::Senior`.
5. Cover every planned learning objective once unless a second retrieval operation is explicitly
   justified by the brief.
   Overview topics are capped at 7 fronts; exceeding that cap requires an explicit user decision.
6. Prefer Mechanism, Contrast, Code, Trap, and Scenario. Use Definition only when a Middle-level
   candidate must give a precise boundary, invariant, or contract.
7. Make each front self-contained, atomic, answerable, and representative of real interviews.
8. State Python, CPython, version, and GIL-enabled/free-threaded configuration whenever the
   expected answer depends on them.
9. Do not copy community-source wording. Reformulate independently in Ukrainian.
10. Use English for Python code, identifiers, API names, and established technical terms.
11. Do not invent popularity, company attribution, or a factual premise not supported by the
    supplied sources.
12. Link every front to the exact existing Q&A answer section when one exists, using a permalink
    pinned to the audited source commit. Add official validation URLs separately. Do not copy the
    answer text into the TSV or provenance register.

Before writing the file, map each proposed front to one coverage objective and remove semantic
duplicates. After writing, run:

```powershell
python scripts/verify_cards.py --front-only cards/<topic>.txt
```

Return a short report separately from the TSV file. Never place the report inside the TSV.
