---
id: emb-macros-0012
title: "What does the stringification operator `#` do in a macro?"
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
#define STR(x) #x
printf("%s", STR(hello));
```

## Short answer

**`#x` turns the spelling of a macro argument into a string literal**: here `"hello"` is substituted.

It works only for a function-like macro parameter, without expanding macros inside the argument first. Whitespace is normalized, and quotes and backslashes are escaped.

For example, `STR(hello)` produces `"hello"`; expanding a nested macro first requires an extra level.[^iso-c-n1570]

## Detailed explanation

TODO
