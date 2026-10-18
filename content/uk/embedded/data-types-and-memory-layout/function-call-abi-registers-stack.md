---
id: emb-cemb-0042
title: "Як працює function call на рівні ABI: stack frame, registers, return address і calling convention?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

ABI задає, які аргументи й return value ідуть у registers, що кладеться на stack і які registers має зберігати caller/callee. Під час call зберігається return address, створюється stack frame для locals/spills, потім callee повертає результат і відновлює потрібний стан. Для debug HardFault корисно дивитися SP, LR, PC і stack frame.[^dou-embedded-interview]

## Detailed explanation

TODO
