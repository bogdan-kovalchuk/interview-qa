---
id: emb-cemb-0040
title: "Які storage classes є у C і як вони пов'язані з linkage та storage duration?"
track: embedded
section: c-in-embedded
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Основні specifiers: `auto`, `register`, `static`, `extern`, `_Thread_local`. `static` у block scope дає static storage duration, а на file scope дає internal linkage. `extern` зазвичай оголошує object/function з external linkage, але lifetime визначається самим об'єктом, не словом `extern`.[^dou-embedded-interview]

## Detailed explanation

TODO
