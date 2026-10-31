---
id: emb-cppfound-0076
title: "What is wrong with this code?"
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

## Question code

```c
char buf[4]="abc";
buf[4]='\0';
```

## Short answer

<span class="warn">Buffer overflow!</span> `char buf[4] = "abc"` -> `buf = {'a','b','c','\0'}` – the array has 4 elements, indices 0..3, so `buf[4]` is the fifth element, outside the array. Another issue: `"abc"` already has '\0' at position 3 – the null-terminator is already there, so the string is valid. If `char buf[3] = "abc"` – the compiler warns or stores 'a','b','c' without '\0' (truncation); always ensure buffer size >= string length + 1.[^embeddedinterviewlab]

## Detailed explanation

TODO
