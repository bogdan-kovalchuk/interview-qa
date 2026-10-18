---
id: emb-cppfound-0094
title: "What is the efficient way to iterate through an array with a pointer versus an index?"
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

Pointer iteration: `for(int *p=arr; p!=arr+n; p++) use(*p);` Index iteration: `for(int i=0; i<n; i++) use(arr[i]);`

With modern optimizing compilers (`-O2`): **the code is usually identical** – the compiler converts between forms on its own.

However: pointer iteration avoids recomputing the base address (`arr + i` each time). Without optimization, pointer iteration can be faster. In embedded (no optimization): pointer iteration is more efficient for Cortex-M0.[^embeddedinterviewlab]

## Detailed explanation

TODO
