---
id: emb-cppfound-0100
title: "Trap: where is the error?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/e/
---

## Question code

```c
char *p = malloc(5);
strcpy(p, "hello");
p[5] = '\0';
```

## Short answer

<span class="warn">Buffer overflow.</span> `malloc(5)` – 5 bytes, but `"hello"` = `{'h','e','l','l','o','\0'}` – 6 bytes including the null terminator.

`strcpy(p, "hello")` already overflows the buffer (6 bytes into 5), and `p[5] = '\0'` is a sixth write past the end.

Correct: `malloc(strlen("hello") + 1)` = `malloc(6)`, or `strncpy(p, "hello", 5); p[4]='\0';` – truncate if needed.[^embeddedinterviewlab]

## Detailed explanation

TODO
