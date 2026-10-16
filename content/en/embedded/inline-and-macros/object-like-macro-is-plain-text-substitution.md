---
id: emb-macros-0002
title: "How does an object-like macro differ from an ordinary constant?"
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
#define BUFFER_SIZE 256
```

## Short answer

**An object-like macro is plain text substitution**: wherever `BUFFER_SIZE` appears, the preprocessor inserts `256`.

Unlike a `const` variable, a macro <span class="warn">has no type and no scope</span> – it is visible from the `#define` site to the end of the file (or `#undef`) and ignores blocks and functions.[^iso-c-n1570]

Rule: for an ordinary typed value, use a language declaration and reserve macros for preprocessor substitution.[^iso-c-n1570]

## Detailed explanation

TODO
