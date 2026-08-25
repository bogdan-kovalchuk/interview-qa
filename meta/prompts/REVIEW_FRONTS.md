# Prompt: strict independent review of interview fronts

The reviewer receives `authoring/CARD_SPEC.md`, all topic briefs, the coverage plan, source records,
and all front-only TSV files. The reviewer must not infer that a question is good because it
already exists in the repository.

## Review gates

For every front, assess:

1. `Current`: the premise is valid for stable Python 3.14 and configuration assumptions are explicit.
2. `Level`: the question genuinely tests Middle or Senior understanding, not Junior recall.
3. `Atomic`: one primary retrieval operation and one assessable answer boundary.
4. `Unambiguous`: a competent candidate can tell what a complete answer must address.
5. `Interview value`: the concept and form are typical or strongly representative of Python interviews.
6. `Coverage`: the bank covers all planned objectives without quota padding.
7. `No duplicate`: no semantic duplicate across topic files.
8. `Scope`: Python remains primary and overview topics stay deliberately small.
9. `Language/runtime`: Python guarantees, CPython details, versions, GIL-enabled, and free-threaded
   behavior are not conflated.
10. `Format`: UTF-8, one physical line, exactly two TABs, empty Back, valid HTML, required tags,
    and `stage::FrontOnly`.
11. `Provenance`: the stable card ID has exactly one register row, the front hash matches, the
    community answer permalink resolves to the intended Q&A section, and official validation
    sources are sufficient for the future Back.

For every problem, assign one action: `FIX`, `SPLIT`, `MERGE`, `REJECT`, or `NEEDS_SOURCE`.
The report must include per-topic PASS/problem counts, coverage gaps, cross-topic duplicates,
and exact file/line references. Do not write any Back content.
