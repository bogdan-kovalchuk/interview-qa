---
id: emb-cppfound-0048
title: "What does this return on 32-bit?"
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

## Question code

```c
char *p = "hello";
printf("%zu", sizeof(p));
```

## Short answer

**4** (on 64-bit – 8).

`p` is a pointer of type `char*`, so `sizeof(p) = sizeof(char*) = 4` on 32-bit. Not the string length, not 6 (with '\0'), but only the pointer size.

For the string length: `strlen(p) + 1` = 6 (with null terminator) or `strlen(p)` = 5.

Compare: `char arr[] = "hello"; sizeof(arr) = 6` – here it is an array, not a pointer.[^embeddedinterviewlab]

## Detailed explanation

TODO
