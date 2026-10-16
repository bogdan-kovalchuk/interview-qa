---
id: emb-fnptr-0028
title: "What is the callback lifetime problem?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**The driver may keep a callback or context longer than the object they point to lives.**

For example, `ctx = &local_config` is registered in an init function; the function returns, the stack frame is gone, and an interrupt later invokes the callback with a dangling context. This is use-after-scope.

Rule: a context pointer for an async callback must point to an object with sufficient lifetime: static storage, a heap object with ownership, or a driver instance that is guaranteed to live until unregister.[^embeddedinterviewlab] [^iso-c-n1570]

## Detailed explanation

TODO
