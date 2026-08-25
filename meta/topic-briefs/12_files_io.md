# Topic brief: 12_files_io

## Goal and scope

Test text/binary boundaries, encoding, buffering, lifecycle, paths, serialization, and safe file
handling. Network protocol and framework I/O are excluded.

## Sources

- Official: https://docs.python.org/3.14/library/io.html
- Official: https://docs.python.org/3.14/library/pathlib.html
- Official: https://docs.python.org/3.14/library/json.html
- Official: https://docs.python.org/3.14/library/pickle.html
- Official: https://docs.python.org/3.14/library/os.html#os.fsync
- Official: https://docs.python.org/3.14/library/os.html#os.replace
- Official: https://docs.python.org/3.14/library/tempfile.html
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/files_and_io.md

## Coverage plan

| Cluster | Retrieval operation | Middle | Senior | Total |
|---|---|---:|---:|---:|
| Text binary encoding and newline handling | diagnose and choose | 2 | 1 | 3 |
| Buffering blocking and flushing | explain and assess | 1 | 1 | 2 |
| Resource lifecycle and atomic replacement | design and diagnose | 2 | 0 | 2 |
| `seek` `tell` and random access | apply | 1 | 0 | 1 |
| `pathlib` traversal and path safety | implement and choose | 2 | 0 | 2 |
| JSON customization and pickle risk | choose and secure | 1 | 2 | 3 |
| In-memory streams | select | 1 | 0 | 1 |

Planned total: 14 fronts, all Middle+.

## Sensitive boundaries

- Default encodings and newline translation are platform-sensitive.
- Never imply that untrusted pickle data is safe to load.
