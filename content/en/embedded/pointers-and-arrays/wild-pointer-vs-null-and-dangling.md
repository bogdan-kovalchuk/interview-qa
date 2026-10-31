---
id: emb-cppfound-0038
title: "What is a wild pointer and how does it differ from a NULL or dangling pointer?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Wild pointer** – an uninitialized pointer with a garbage value (a random address from the stack).

Comparison:
- **NULL pointer**: explicitly invalid address 0, can be checked;
- **Dangling pointer**: pointed to a valid object that has been destroyed;
- **Wild pointer**: never pointed to a valid object.

All three lead to undefined behavior when dereferenced. A wild pointer is the most dangerous: its address is non-zero and random, so it passes the `if(p != NULL)` check.[^embeddedinterviewlab]

## Detailed explanation

TODO
