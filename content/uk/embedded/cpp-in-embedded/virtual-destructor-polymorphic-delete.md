---
id: emb-cppemb-0001
title: "Для чого потрібен virtual destructor у C++ і коли це актуально для embedded C++?"
description: "Virtual destructor потрібен для коректного видалення polymorphic object через base pointer; у embedded це стосується driver і HAL interfaces."
track: embedded
section: cpp-in-embedded
level: middle
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? cpp-in-embedded; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Virtual destructor потрібен, якщо об'єкт видаляють через pointer/reference на base class: тоді викликається destructor derived class. Без нього <code>delete basePtr</code> для polymorphic object має undefined behavior. В embedded C++ це актуально для driver interfaces, HAL abstractions або state machines, але dynamic allocation часто замінюють static lifetime чи placement new.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
