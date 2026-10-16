---
id: emb-cppfound-0087
title: "What is a one-past-the-end pointer and which operations are allowed?"
track: embedded
section: c-in-embedded
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**One-past-the-end** is a pointer to the element immediately after the array: `int *end = arr + N`. It is legal under the C standard.

Allowed:
- **Forming** it (the address is valid);
- **Comparing**: `p != end`, `p <= end`;
- **Subtracting** from another pointer within the array.

Forbidden:
- <span class="warn">Dereferencing</span>: `*end` -> UB;
- <span class="warn">Incrementing further</span>: `end+1` -> UB.

Standard idiom: `for(int *p=arr; p!=arr+N; p++)`[^embeddedinterviewlab]

## Detailed explanation

TODO
