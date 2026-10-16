---
id: emb-patterns-0018
title: "What does the return-code error handling pattern look like?"
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
typedef enum {
  ERR_OK = 0, ERR_TIMEOUT, ERR_CRC, ERR_BUSY, ERR_PARAM
} err_t;

err_t sensor_read(uint8_t a, uint16_t *out);
```

## Short answer

**The function returns `err_t` and passes data through an output pointer.**

When the API defines `ERR_OK = 0`, `if (result) { /* error */ }` tests for a non-zero result. Each error branch can return a specific code.[^iso-c-n1570]

Return codes make status explicit, but the caller must still check the result.[^iso-c-n1570]

## Detailed explanation

TODO
