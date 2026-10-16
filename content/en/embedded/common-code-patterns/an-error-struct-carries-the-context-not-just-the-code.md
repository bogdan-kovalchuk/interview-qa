---
id: emb-patterns-0020
title: "What is the error struct pattern and when is it better than a plain code?"
track: embedded
section: common-code-patterns
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
typedef struct {
  err_t    code;
  uint16_t line;      // __LINE__
  uint32_t timestamp; // tick
} err_info_t;
```

## Short answer

**An error structure can store a code together with diagnostic context.**

For example, `record_error(code, __LINE__)` can record where a fault was detected; a global `last_error` stores only the latest record and needs coordination when accessed concurrently.

Such context helps diagnosis when its fields, size, and access rules fit the target platform.[^iso-c-n1570]

## Detailed explanation

TODO
