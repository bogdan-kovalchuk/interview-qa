---
id: py-excpt-0014
title: "When is EAFP preferable to LBYL, and how can a race between the check and the action make LBYL incorrect?"
track: python
section: exceptions
sources:
  - source_id: py314-tutorial-errors
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html
  - source_id: py314-library-exceptions
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html
  - source_id: py314-reference-compound-stmts-the-try-statement
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
  - source_id: py314-glossary-term-lbyl
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-LBYL
  - source_id: py314-glossary-term-eafp
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-EAFP
  - source_id: py314-library-os-os-access
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.access
---

## Short answer

**EAFP is preferable when the state can change between the check and the action.** LBYL checks a condition first and then acts, so another thread, process or network request can change the state in between (a TOCTOU race, time-of-check to time-of-use). EAFP performs the action at once and handles the exception if it fails, so there is no separate window. The `os.access()` documentation warns about exactly this case and recommends EAFP.[^py314-library-os-os-access]

## Detailed explanation

LBYL (look before you leap) explicitly tests preconditions before a call or lookup, while EAFP (easier to ask forgiveness than permission) assumes the operation will succeed and catches the exception if that assumption proves false.[^py314-glossary-term-lbyl][^py314-glossary-term-eafp] Both approaches can be correct. The difference is where the guarantee lives: in EAFP it is the operation itself, while in LBYL it is the check, which may already be false by the time the action runs.

A race happens when there is a gap between the check and the action in which the state can change. The `os.access()` documentation describes exactly this case: checking access and then calling `open()` gives an attacker a window to replace the file, so EAFP is recommended.[^py314-library-os-os-access] The simulation below shows the same mechanism on a dictionary: `remove_key` behaves like another thread that deletes the key in the gap between the check and the action. It is a deterministic simulation, not real concurrent code.

```python
def lbyl(d, key, other_thread):
    if key in d:             # check
        other_thread(d)      # another thread runs here and removes the key
        return d[key]        # action: KeyError, the check is already stale
    return None

def eafp(d, key, other_thread):
    other_thread(d)          # the removal happens here too, but there is no check to go stale
    try:
        return d[key]        # action; the exception is handled where it occurs
    except KeyError:
        return None

def remove_key(d):
    d.pop('k', None)

try:
    print(lbyl({'k': 1}, 'k', remove_key))
except KeyError as exc:
    print('LBYL failed:', exc)     # LBYL failed: 'k'
print(eafp({'k': 1}, 'k', remove_key))  # None
```

EAFP is the better fit when the failure is a normal outcome (the key is missing, the file is missing, the network returned an error) that the code must handle; when the state is shared and may change; and when the `try` block is narrow, so the exception caught is the expected one from the intended operation. LBYL remains the better choice when a partial action is unsafe or cannot be undone: it is better to validate all inputs before the first write than to leave a half-finished write behind.

EAFP does not make a sequence atomic. If the second step fails after the first one has succeeded, the first step has already happened; a transaction, a lock or another synchronization mechanism is needed for that.

**Common mistakes:**
- catching a broad `Exception` around a large block, so an error from a neighbouring operation looks like "the key is missing";
- assuming a `try` makes several steps atomic: after the first successful step, the second may fail;
- keeping `if os.path.exists(p)` before `open(p)` "for safety", which reproduces the same window that EAFP removes.
