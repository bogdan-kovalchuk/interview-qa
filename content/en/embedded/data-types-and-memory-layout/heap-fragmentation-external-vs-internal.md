---
id: emb-dtypes-0034
title: "What is heap fragmentation, and why is it critical for embedded systems?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: freertos-heap
    title: "FreeRTOS heap_4 implementation"
    url: https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/main/portable/MemMang/heap_4.c
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Heap fragmentation occurs after multiple `malloc`/`free` calls: total free memory may be sufficient, but the largest contiguous block may be too small for a request, so `malloc` can return `NULL`.

**External**: many small free blocks. **Internal**: allocated block is larger than requested (alignment/metadata).

The absence of an MMU does not prevent an allocator from coalescing adjacent free blocks: for example, FreeRTOS `heap_4` does this. Moving live objects to compact memory is a separate allocator feature, and ordinary C pointers make such relocation difficult.[^freertos-heap]

## Detailed explanation

TODO
