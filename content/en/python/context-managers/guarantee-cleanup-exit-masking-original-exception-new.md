---
id: py-ctxmgr-0003
title: "How do you guarantee cleanup in `__exit__` without masking the original exception with a new error from the cleanup code?"
description: "How do you guarantee cleanup in `__exit__` without masking the original exception with a new error from the cleanup code?"
track: python
section: context-managers
level: senior
type: practical
tags: [exit]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel-with-statement-context-managers
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#with-statement-context-managers
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-contextlib
    title: "Python 3.14: Library/contextlib"
    url: https://docs.python.org/3.14/library/contextlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-asyncio-task-task-cancellation
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html#task-cancellation
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**Cleanup code in `__exit__` must be wrapped in its own `try/except` block so that an exception during cleanup does not mask the original one.**[^py314-reference-datamodel-with-statement-context-managers] If `__exit__` is called with exception arguments and cleanup raises a new unhandled error, Python replaces the original exception with the cleanup failure. A safe pattern is to wrap `self.resource.close()` in `try/except Exception`, log the cleanup error, and return `False`. If there was no original exception, the cleanup error should be allowed to propagate freely.

## Detailed explanation

When the interpreter invokes `__exit__(exc_type, exc_val, exc_tb)` following an exception inside a `with` block, any new unhandled exception raised within `__exit__` itself immediately aborts the method and propagates up the stack, displacing the original failure.[^py314-reference-datamodel-with-statement-context-managers]

Although Python implicit exception chaining attaches the preceding error to the new one via the `__context__` attribute, in production environments this frequently distorts monitoring and triage: alerting systems trigger on secondary `OSError` or `ConnectionResetError` during socket teardown rather than the underlying domain exception or syntax defect. Furthermore, if `__exit__` is responsible for releasing multiple resources, an unhandled crash during the first cleanup step leaves all subsequent resources orphaned.

A resilient engineering pattern separates normal exit (`exc_type is None`) from exceptional exit (`exc_type is not None`). When no exception occurred inside the `with` block, a failure during cleanup represents the sole catastrophic event and must be allowed to propagate (for example, if flushing a dirty buffer to disk fails and data is lost). Conversely, if an exception is already in flight, cleanup errors should be caught, recorded to diagnostics via structured logging, and suppressed within cleanup while returning `False` so the original root-cause exception continues propagating.[^py314-library-contextlib]

Pattern for resilient resource cleanup in `__exit__` protecting the original exception:

```python
import logging

logger = logging.getLogger(__name__)


class ResilientResource:
    def __init__(self, resource):
        self.resource = resource

    def __enter__(self):
        return self.resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.resource.close()
        except Exception as cleanup_err:
            if exc_type is not None:
                # An exception already occurred in the with-block:
                # Log cleanup failure so original exc_val continues propagating
                logger.error(
                    "Cleanup failed during exception handling: %s",
                    cleanup_err,
                    exc_info=True,
                )
                return False  # Propagate the original exception from with-block
            # Normal exit had no errors, so let the cleanup exception surface
            raise
        return False  # Normal clean exit or propagation
```

**Engineering trade-offs and best practices:**
- logging cleanup errors instead of silencing them: `logger.error(..., exc_info=True)` preserves full traceback diagnostics without aborting propagation of the root cause;
- isolating multiple cleanup actions: if releasing multiple resources, each teardown operation must reside in its own protective block or be orchestrated via `contextlib.ExitStack`;
- never swallowing errors on clean exits: a failure during `close()` or `flush()` without an active error in the `with` body indicates real data loss and must raise;
- avoiding catching `BaseException` during cleanup: system interrupts (`KeyboardInterrupt`, `SystemExit`) must never be trapped by routine resource cleanup handlers.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
