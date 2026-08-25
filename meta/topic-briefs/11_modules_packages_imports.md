# Topic brief: 11_modules_packages_imports

## Goal and scope

Test import resolution, module caching and initialization, package forms, circular imports,
reload behavior, and modern packaging boundaries. Exclude tool-specific dependency-manager trivia.

## Sources

- Official: https://docs.python.org/3.14/reference/import.html
- Official: https://docs.python.org/3.14/library/importlib.html
- Official: https://packaging.python.org/en/latest/tutorials/packaging-projects/
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/modules_and_packages.md
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/python_packages.md

## Coverage plan

| Cluster | Retrieval operation | Middle | Senior | Total |
|---|---|---:|---:|---:|
| Import process and `sys.modules` cache | trace and explain | 3 | 1 | 4 |
| Resolution paths and relative imports | diagnose and choose | 2 | 1 | 3 |
| Circular and partially initialized imports | diagnose and repair | 1 | 1 | 2 |
| Regular and namespace packages | contrast and design | 2 | 0 | 2 |
| Main guard and reload semantics | predict and constrain | 1 | 1 | 2 |
| Build metadata and distribution boundary | explain | 1 | 0 | 1 |

Planned total: 14 fronts, all Middle+.

## Sensitive boundaries

- Import cache behavior must be separated from name binding in the importing module.
- Packaging terms project distribution import package and module must not be conflated.
