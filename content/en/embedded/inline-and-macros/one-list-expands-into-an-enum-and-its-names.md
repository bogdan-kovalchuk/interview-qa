---
id: emb-macros-0022
title: "How does an X-macro keep an `enum` and a string array in sync?"
track: embedded
section: inline-and-macros
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
#define ERR_LIST(X) \
  X(ERR_NONE, "OK") \
  X(ERR_TIMEOUT, "Timeout")
```

## Short answer

The same list is expanded twice with different `X`:

```c
#define AS_ENUM(n, s) n,
typedef enum { ERR_LIST(AS_ENUM) } err_t;

#define AS_STR(n, s) [n] = s,
static const char *const names[] = { ERR_LIST(AS_STR) };
```

One list – two generated objects. A new error code is added in one place, and both `enum` and `names[]` are updated together.[^iso-c-n1570]

## Detailed explanation

TODO
