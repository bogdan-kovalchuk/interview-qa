---
id: emb-cemb-0039
title: "Чим важливі C99 і C11 для embedded C, і які можливості C11 не завжди доступні на MCU toolchains?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

C99 приніс `stdint.h`, `stdbool.h`, designated initializers, mixed declarations і `inline`, що дуже корисно для embedded. C11 додав atomics, threads, alignment features і static assertions. <span class="warn">На MCU toolchains C11 threads/atomics можуть бути неповними або залежати від runtime/libc</span>, тому треба перевіряти конкретний compiler і flags.[^dou-embedded-interview]

## Detailed explanation

TODO
