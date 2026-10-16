---
id: emb-dtypes-0027
title: "Why is heap allocation often banned in safety-critical embedded systems?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: misra-c-2023-addendum-2
    title: "MISRA C:2023 Addendum 2"
    url: https://misra.org.uk/app/uploads/2024/10/MISRA-C-2023-ADD2.pdf
---

## Short answer

Dynamic memory can make execution time, peak RAM use, and post-fragmentation behavior harder to predict.[^iso-c-n1570] MISRA C generally prohibits dynamic allocation, but that is a rule of a specific coding standard; DO-178C alone does not mean that every project universally bans `malloc`.[^misra-c-2023-addendum-2]

Allocating at startup is still dynamic allocation and is not automatically permitted or safe. It can be considered only when the project's policy allows it and timing, failure, and memory limits have been checked for the specific allocator and configuration.[^iso-c-n1570][^misra-c-2023-addendum-2]

## Detailed explanation

TODO
