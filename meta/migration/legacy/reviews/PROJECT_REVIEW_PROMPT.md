# Prompt: exhaustive independent review of the Python interview deck project

## Role

Act as a strict independent reviewer with four simultaneous perspectives:

1. a senior Python interviewer who regularly evaluates Middle and Senior candidates;
2. a Python curriculum auditor who can detect missing concepts and artificial card padding;
3. an Anki editor who understands atomic retrieval practice, ambiguity, and semantic duplication;
4. a source-verification engineer who distinguishes Python language guarantees from CPython
   implementation details and checks every material claim against authoritative evidence.

Do not defend the existing project. Assume that its taxonomy, coverage plan, sources, questions,
levels, tags, and validators may all contain mistakes. Your job is to find them and document them
precisely.

## Repository and deliverable

Review the complete repository at:

```text
C:\Users\bogdan\Desktop\python_interview_questions
```

Write the complete review to:

```text
tracking/reviews/EXHAUSTIVE_PROJECT_REVIEW.md
```

Create `tracking/reviews/` if it does not exist. The report must be written in English and saved
as UTF-8. Do not edit cards, specifications, source registers, scripts, templates, or tracking
state during this task. The review report is the only permitted content change.

## Primary objective

The most important question is whether the deck is exhaustive for its declared scope without
being repetitive or padded.

Determine, with evidence:

1. whether all interview-relevant concepts within the declared scope are covered;
2. whether important concepts are covered deeply enough for Middle and Senior interviews;
3. whether any concepts, retrieval operations, or expected trade-offs are missing;
4. whether any cards are exact, near, functional, or cross-topic semantic duplicates;
5. whether each question is genuinely representative of a Python interview rather than merely
   technically true, easy to look up, obscure, academic, or invented for quota completion;
6. whether the number of cards follows concept coverage instead of arbitrary target counts.

"Exhaustive" does not mean covering every Python API or trivia item. It means covering the
complete set of durable, interview-relevant learning objectives appropriate to the repository's
scope and Middle+ audience. A smaller complete set is better than a large padded set.

Allocate most of the review effort to completeness, duplicates, and interview relevance. Review
technical correctness and repository mechanics as required supporting gates, not as substitutes
for the content audit.

## Non-negotiable boundaries

- Read and follow the repository `AGENTS.md` before doing any work.
- Also read the shared reference library instructions at
  `C:\Users\bogdan\Documents\Projects\agents-library\AGENTS.md`, followed by
  `rules/known-issues.md`, `rules/decisions.md`, and `rules/conventions.md`.
- Treat stable Python 3.14 as the baseline. Mark behavior from other versions explicitly.
- Separate Python language guarantees from CPython implementation details.
- Separate ordinary GIL-enabled CPython from the supported free-threaded build.
- Keep Python as the primary subject. Algorithms/data structures, SQL, and Git/CI/CD/SDLC must
  remain deliberately brief.
- Treat web frameworks, APIs, frontend, cloud platforms, and detailed system design as out of
  scope.
- Do not recommend cards merely to increase a count.
- Do not accept a topic as complete because its planned and actual counts match.
- Do not accept a card as interview-relevant merely because it appears in this repository or one
  community question bank.
- Do not invent citations, interview-frequency claims, source coverage, or Python behavior.
- Do not copy substantial source wording into the report.
- Do not write missing Back content. Review the existing pilot Back content only.
- Do not edit card TSV files or change accepted-card counts.
- Preserve unrelated working-tree changes. If the repository is dirty before the review, record
  the exact pre-existing state and do not include those changes in any commit.

## Required reading order

Read these artifacts completely before judging cards:

1. `AGENTS.md`
2. `README.md`
3. `authoring/CARD_SPEC.md`
4. `authoring/TAXONOMY.md`
5. `authoring/SOURCE_POLICY.md`
6. `authoring/FRONT_PROVENANCE.md`
7. `authoring/QUALITY_GATES.md`
8. `authoring/DECISIONS.md`
9. `authoring/NOTE_TYPE_TEMPLATE.md`
10. `authoring/manifest.json`
11. every topic brief under `sources/notes/`
12. source inventories under `sources/official/` and `sources/community/`
13. `tracking/coverage.csv`
14. `tracking/front_coverage_plan.csv`
15. `tracking/front_sources.csv`
16. `tracking/code_checks.csv`
17. `tracking/anki_smoke.csv`
18. every TSV directly under `cards/`
19. all files under `authoring/examples/`, including the pilot Back preview;
20. all validators and tests under `scripts/`.

Follow every source named by each topic brief. Check the pinned community permalinks recorded in
`tracking/front_sources.csv`, but treat the community repository only as an interview concept map
unless its licensing and factual authority justify more. Validate technical facts with current
primary sources.

## Evidence policy

### Technical correctness

Prefer evidence in this order:

1. Python 3.14 Language Reference, Standard Library documentation, HOWTOs, and official FAQs;
2. accepted PEPs and official CPython documentation;
3. CPython source code and tests for explicitly implementation-specific behavior;
4. official documentation for non-Python overview topics;
5. reputable community sources only for discovery or corroboration.

Browse the live source when a fact may have changed, when a precise citation is required, or when
the repository contains only a URL rather than the relevant text. Record direct links in the
report. A broken or inaccessible source is an unresolved verification problem, not a pass.

### Interview relevance

Interview relevance requires separate evidence from technical correctness. Use the pinned
candidate Q&A source plus independent, reputable Python interview-question collections or hiring
materials. When possible, use at least two independent signals before calling a question common
or typical.

Use this evidence scale:

- `R3 common`: recurring across multiple independent interview-oriented sources and appropriate
  for the stated level;
- `R2 representative`: a canonical mechanism or trade-off that strongly predicts practical
  Python competence, even if public frequency evidence is limited;
- `R1 marginal`: technically valid but weakly evidenced, overly niche, mostly lookup-oriented, or
  poorly matched to the claimed level;
- `R0 unsuitable`: trivia, out of scope, misleading, below Middle level, unassessable, or not a
  credible interview question.

Do not present public question-bank frequency as statistical hiring data. If evidence is weak,
say so explicitly and lower confidence.

## Required workflow

### Stage 0: establish the immutable baseline

Before reviewing content:

1. record `git status --short` and the current commit;
2. inventory all tracked and relevant untracked files;
3. count topics, package-source TSV files, Fronts, non-empty Backs, placeholders, card IDs, levels,
   card types, and scopes mechanically;
4. record whether observed counts match `authoring/manifest.json`, topic briefs, and tracking files;
5. run the existing validation suite and capture the exact results.

At minimum, run:

```powershell
python scripts/verify_cards.py cards
python scripts/verify_front_sources.py
python scripts/verify_project.py
python -m unittest discover -s scripts/tests -v
python scripts/verify_cards.py authoring/examples/01_python_fundamentals_preview.txt
```

Do not treat zero validator errors as evidence of semantic completeness or interview quality.

### Stage 1: construct an independent concept inventory

For each of the 23 declared topics, derive a source-grounded inventory of interview-relevant
learning objectives before mapping existing cards. Do not reverse-engineer objectives from the
cards themselves.

Each objective must have:

- a stable review ID such as `OBJ-01-001`;
- a concise concept or decision boundary;
- the retrieval operation expected from a candidate, such as explain, predict, diagnose,
  contrast, design, or choose with a trade-off;
- intended level: Middle, Senior, or both;
- importance: critical, important, optional, or out of scope;
- authoritative technical source;
- interview-relevance evidence and relevance score;
- any required Python version, implementation, GIL, or platform qualification.

The inventory must distinguish a concept from the ways it should be tested. For example, knowing
a definition does not automatically cover mechanism, code prediction, failure diagnosis, and
design trade-offs. Conversely, do not demand multiple cards when one well-designed scenario
reliably tests the complete objective.

For Overview topics 21-23, respect the repository's hard cap and general-awareness purpose. A
missing specialist detail is not a gap if it is intentionally out of scope.

### Stage 2: map every card to the independent inventory

Audit every physical card row. Sampling is not allowed.

For each card, record:

- stable card ID;
- file and physical line number;
- topic, type, level, and scope tags;
- one primary objective ID;
- optional secondary objective IDs;
- expected answer boundary in one concise sentence;
- relevance score `R0-R3` and confidence;
- content status;
- required action if defective.

Every observed card ID must appear exactly once in the review ledger. Report missing, duplicated,
malformed, or reused IDs immediately.

Use these content statuses:

- `PASS`
- `THIN`
- `AMBIGUOUS`
- `DUPLICATE`
- `OUT_OF_SCOPE`
- `BELOW_LEVEL`
- `NEEDS_SOURCE`
- `FACTUAL_RISK`
- `REJECT`

Use these remediation actions:

- `KEEP`
- `FIX`
- `SPLIT`
- `MERGE`
- `MOVE`
- `RELEVEL`
- `REJECT`
- `ADD_CARD`
- `ADD_SOURCE`

### Stage 3: audit completeness topic by topic

For every topic, compare the independent objective inventory with the mapped cards and classify
each objective as:

- `covered`: the candidate must actually retrieve or apply the objective;
- `thin`: the concept is mentioned but an important mechanism, boundary, or trade-off is absent;
- `missing`: no card tests it;
- `duplicated`: multiple cards test materially the same retrieval operation without added value;
- `overcovered`: card density is disproportionate to interview importance;
- `out_of_scope`: deliberately excluded and should remain excluded;
- `unsupported`: potentially valuable but not adequately sourced.

For every `thin` or `missing` objective, explain:

1. why it matters at Middle or Senior level;
2. what evidence makes it interview-relevant;
3. whether an existing card can be fixed or whether a new card is justified;
4. the smallest sufficient retrieval operation for remediation;
5. whether adding it would require removing or merging a weaker card.

Do not write the final wording of a new card unless a short example is necessary to make the
finding understandable. The report is an audit, not a silent expansion of the deck.

### Stage 4: perform exhaustive duplicate analysis

Run both mechanical and semantic duplicate detection across all topic files.

Check for:

- exact normalized Front duplicates;
- near-verbatim rephrasings;
- same expected answer under different wording;
- definition-versus-mechanism pairs that are actually redundant;
- scenario cards whose scenario decoration does not change the tested decision;
- cross-topic overlap caused by weak taxonomy boundaries;
- cards that repeat a parent concept while pretending to test a narrower child concept;
- multiple cards that differ only by an example value, API spelling, or implementation detail.

For each duplicate cluster, provide:

- cluster ID such as `DUP-001`;
- all card IDs and exact file/line references;
- normalized expected answer for the cluster;
- duplicate type: exact, near, functional, or cross-topic;
- whether any card contributes a genuinely distinct retrieval operation;
- the recommended canonical card and action for every other member;
- confidence and reasoning.

Do not mark legitimate reinforcement as duplication when cards independently test definition,
mechanism, prediction, diagnosis, or trade-off. Explain the distinction for borderline clusters.

### Stage 5: audit interview realism and level calibration

Evaluate every card as an interviewer would:

- Can the question be asked naturally without repository context?
- Does it have a bounded, assessable expected answer?
- Would a strong Middle or Senior candidate reasonably be expected to answer it?
- Does it reveal understanding, or only memorized trivia?
- Is the claimed level accurate?
- Is a Senior label justified by deeper reasoning rather than longer wording?
- Does a scenario resemble an engineering decision, debugging case, code review, or trade-off that
  occurs in real interviews?
- Would a code question test prediction plus explanation rather than syntax recall?
- Is the wording overly academic, artificial, leading, or optimized for a curriculum rather than
  a conversation?

Report all `R0` and `R1` cards individually. For `R2` and `R3`, provide per-topic counts and list
borderline cases. Identify important interview patterns that are absent from the deck even if the
underlying technical noun appears somewhere.

### Stage 6: audit factual, version, runtime, and provenance integrity

For every card, inspect whether its premise can support a correct future Back. Pay special
attention to:

- Python versus CPython;
- Python 3.14 versus earlier behavior or 3.15 preview behavior;
- language guarantees versus observable results from one implementation;
- GIL-enabled versus free-threaded CPython;
- reference counting, GC, finalization, object identity, interning, bytecode, frames, and memory;
- iteration order, hashing, mutation, equality, and concurrency guarantees;
- performance claims without a defined workload or implementation;
- broad claims containing words such as always, never, atomic, thread-safe, faster, or guaranteed.

Mechanically verify `tracking/front_sources.csv`:

- exactly one row per stable card ID;
- matching Front hash;
- correct topic and draft file;
- resolvable pinned community permalink when present;
- official references that actually support the premise and expected answer;
- no generic source bundle used as a substitute for claim-specific evidence;
- no stale, redirected, broken, or unrelated source.

### Stage 7: review the pilot Back preview

Review `authoring/examples/01_python_fundamentals_preview.txt` separately from the Front-only bank.

For the first ten completed Backs, check:

- factual correctness and completeness;
- direct answer in the first sentence;
- one primary idea per card;
- Python/CPython qualification;
- concise but interview-sufficient explanation;
- safe and valid HTML;
- working source links that support every material claim;
- preservation of stable card IDs and intended learning objectives;
- consistency with `authoring/NOTE_TYPE_TEMPLATE.md` and `authoring/CARD_SPEC.md`.

Confirm that the remaining placeholder Backs are visibly marked and cannot be mistaken for
production-ready content. Do not interpret a structurally valid placeholder as a completed Back.
Do not treat the preview as a package-source TSV.

### Stage 8: review project mechanics and presentation

After the content audit, assess supporting project quality:

- taxonomy boundaries and naming;
- consistency among manifest, briefs, cards, and tracking CSV files;
- whether coverage plans encode real objectives or only quotas;
- whether validators enforce the documented rules and fail closed;
- missing regression tests for high-risk gates;
- dead, misleading, duplicated, or stale documentation;
- note-template readability in desktop, mobile, day, and night modes;
- whether the structure clearly separates Front-only drafts, examples, placeholders, and ready
  artifacts;
- whether any current status or filename overstates production readiness.

Keep these findings secondary to card completeness, duplicates, and interview relevance.

### Stage 9: adversarial recheck

After drafting findings, perform a separate skeptical pass:

1. challenge every topic marked complete by searching for omitted critical objectives;
2. challenge every proposed new card for quota padding or scope expansion;
3. challenge every duplicate cluster for genuinely different retrieval operations;
4. challenge every `R3 common` rating for adequate independent evidence;
5. challenge every Senior rating for actual depth;
6. re-run mechanical validators;
7. verify that every card and every topic is represented in the report ledger;
8. confirm that no repository file except the report changed.

If subagents are available, they may perform bounded independent topic or duplicate audits, but
the primary reviewer must reconcile disagreements, verify evidence directly, and remain
responsible for the complete final report.

## Finding format

Every actionable finding must use this schema:

```text
Finding ID:
Severity: Blocker | High | Medium | Low
Confidence: High | Medium | Low
Area: Coverage | Duplicate | Relevance | Level | Correctness | Provenance | Format | Architecture
Topic:
Card IDs:
Files and lines:
Observed evidence:
Why it matters:
Required action:
Acceptance test:
Sources:
```

Severity definitions:

- `Blocker`: makes a card materially wrong, unsafe to learn, falsely production-ready, or breaks
  the integrity of the bank;
- `High`: critical coverage gap, strong duplicate cluster, unsupported premise, or clearly
  non-interview card;
- `Medium`: meaningful ambiguity, thin coverage, incorrect level, weak source, or maintainability
  problem;
- `Low`: wording, organization, minor consistency, or non-blocking presentation improvement.

## Required report structure

The report must contain all of these sections:

1. `Executive verdict`
2. `Scope, evidence, and limitations`
3. `Repository baseline and validation results`
4. `Deck-wide quantitative summary`
5. `Independent learning-objective inventory`
6. `Topic-by-topic completeness review`
7. `Cross-topic coverage and taxonomy gaps`
8. `Duplicate clusters`
9. `Interview relevance and level calibration`
10. `Factual, version, runtime, and provenance findings`
11. `Pilot Back preview review`
12. `Project mechanics, validators, and card presentation`
13. `Prioritized remediation backlog`
14. `Production-readiness verdict`
15. `Appendix A: complete card ledger`
16. `Appendix B: source and interview-evidence ledger`
17. `Appendix C: commands and mechanical results`

The topic summary table must include at least:

```text
Topic | Objectives | Covered | Thin | Missing | Cards | Duplicate cards | R0/R1 cards | Source issues | Verdict
```

The deck-wide summary must include:

- observed topics and files;
- total unique card IDs;
- cards by topic, level, type, and scope;
- covered, thin, missing, duplicated, overcovered, and unsupported objectives;
- exact, near, functional, and cross-topic duplicate counts;
- `R0-R3` relevance distribution;
- Blocker, High, Medium, and Low finding counts;
- completed Backs, placeholders, ready cards, and deferred gates.

The complete card ledger must account for every card, even when the card passes. Do not hide pass
cards behind a sample or aggregate count.

## Prioritized remediation backlog

Order remediation by learning risk, not by file order. Use these phases:

1. remove or correct false and misleading cards;
2. merge semantic duplicates and repair taxonomy boundaries;
3. fill critical Middle+ coverage gaps;
4. replace marginal or artificial questions with evidenced interview-relevant retrieval tasks;
5. repair source and provenance gaps;
6. improve wording, levels, tags, validators, and presentation;
7. write and validate Backs only after the Front bank is stable.

For each backlog item, state dependencies, affected card IDs, expected outcome, and a mechanical or
semantic acceptance test. Do not estimate work with vague labels such as easy or hard.

## Completion gates

Do not claim the review is complete until all of the following are true:

- every observed topic has an independent objective inventory;
- every observed card ID appears exactly once in the complete card ledger;
- every objective has a coverage classification;
- every `thin`, `missing`, `duplicated`, `overcovered`, or `unsupported` objective has a concrete
  recommendation;
- every exact and semantic duplicate cluster names all affected cards;
- every card has an interview-relevance rating;
- every `R0` and `R1` card has an individual explanation;
- all source and provenance failures are reported as unresolved rather than silently passed;
- the pilot Backs and placeholders are distinguished from production-ready cards;
- all required validators have been rerun and their actual output summarized;
- limitations of public interview evidence are explicit;
- the only repository content change is
  `tracking/reviews/EXHAUSTIVE_PROJECT_REVIEW.md`.

Before finishing, run `git diff --check` and inspect `git status --short`. If the working tree was
clean at the start, commit only the report with this one-line commit message:

```text
add exhaustive project review
```

If unrelated or pre-existing changes exist, do not include them in the commit. Report the exact
commit status honestly.

## Final response

Return a concise summary containing:

- the overall verdict;
- the most important completeness, duplicate, and interview-relevance conclusions;
- counts of findings by severity;
- the exact report path;
- validator results;
- commit hash or an explicit explanation of why no commit was made.

Do not substitute the chat response for the full saved report.
