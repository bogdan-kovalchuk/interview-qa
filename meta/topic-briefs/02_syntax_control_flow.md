# Topic brief: 02_syntax_control_flow

## Goal and scope

Test evaluation and control-flow semantics that affect real code review. Exclude keyword lists,
style-guide recall, and comprehension internals owned by topic 13.

## Sources

- Official: https://docs.python.org/3.14/reference/expressions.html
- Official: https://docs.python.org/3.14/reference/simple_stmts.html
- Official: https://docs.python.org/3.14/reference/compound_stmts.html
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/syntax.md
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/loops.md

## Coverage plan

| Cluster | Retrieval operation | Middle | Senior | Total |
|---|---|---:|---:|---:|
| Truthiness and short-circuit values | predict and explain | 3 | 0 | 3 |
| Assignment unpacking and walrus | predict and constrain | 2 | 1 | 3 |
| Loop control and loop `else` | explain and debug | 2 | 0 | 2 |
| Structural pattern matching | select and diagnose | 2 | 1 | 3 |
| Evaluation order and precedence | predict and explain | 2 | 1 | 3 |

Planned total: 14 fronts, all Middle+.

## Sensitive boundaries

- Avoid code whose result depends on unspecified evaluation outside the language reference.
- Pattern matching questions must state the Python 3.14 baseline.
