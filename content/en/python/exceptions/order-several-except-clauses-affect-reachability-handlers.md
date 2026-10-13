---
id: py-excpt-0002
title: "How does the order of several `except` clauses affect the reachability of handlers for subclass exceptions?"
description: "How does the order of several `except` clauses affect the reachability of handlers for subclass exceptions?"
track: python
section: exceptions
level: middle
type: mechanism
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-tutorial-errors
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-exceptions
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-compound-stmts-the-try-statement
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**Python checks `except` clauses from top to bottom and runs the first match; if a parent class comes before its child, the child's handler is unreachable.**[^py314-reference-compound-stmts-the-try-statement] An `except` clause also catches subclasses of the class it names, so `except Exception` before `except ValueError` catches `ValueError` first and the second clause never runs.[^py314-library-exceptions] CPython 3.13 and 3.14 report no warning or error for this order. Put the narrowest (subclass) clauses first and the broadest (parent) last.

## Detailed explanation

When `try` raises an exception, the interpreter checks the `except` clauses in the order they are written and runs the first one that matches. The search stops there, so at most one handler runs per `try`.[^py314-reference-compound-stmts-the-try-statement][^py314-tutorial-errors]

A clause naming class `C` matches an exception if the exception's class is `C` or a subclass of `C`; the reverse does not hold. So `except ValueError` also catches `UnicodeDecodeError` (which inherits from `UnicodeError`, which inherits from `ValueError`), but `except UnicodeDecodeError` does not catch a plain `ValueError`.[^py314-library-exceptions] This is why order matters: a broad clause placed earlier absorbs exceptions that a narrower clause further down was meant to handle.

The trap looks like this:

```python
def parse(text):
    try:
        return int(text)
    except Exception:          # matches every Exception, including ValueError
        return "generic failure"
    except ValueError:         # never reached for int("x")
        return "bad number"

print(parse("x"))  # generic failure, not 'bad number'
```

If the two clauses are swapped, `int("x")` gives `bad number`, while an exception that is not a `ValueError` (for example the `TypeError` from `int(None)`) falls through to `generic failure`. The interpreter does not check this order: CPython 3.13 and 3.14 compile the code without any warning, so the mistake shows up only in a test that passes an input reaching that handler.

Order matters when one exception can match both clauses. That happens in two cases: the classes are related by subclassing, or the exception's class inherits from both. For example, `class E(ValueError, KeyError)` matches both `except ValueError` and `except KeyError`, so whichever clause comes first runs. Built-in pairs such as `OSError` and `ValueError` do not overlap: no built-in class inherits from both, so swapping them changes nothing. The rule is simple: narrowest classes first, parent classes after them, and `except Exception` last.

**Common mistakes:**
- putting `except Exception` before specific exceptions that need their own handling;
- expecting the interpreter to warn about an unreachable handler (CPython 3.13 and 3.14 do not);
- assuming order never matters for unrelated classes; it does when one exception class inherits from both.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
