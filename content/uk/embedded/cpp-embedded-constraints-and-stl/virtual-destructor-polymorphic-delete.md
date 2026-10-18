---
id: emb-cppemb-0001
title: "Для чого потрібен virtual destructor у C++ і коли це актуально для embedded C++?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

Virtual destructor потрібен, якщо об'єкт видаляють через pointer/reference на base class: тоді викликається destructor derived class. Без нього `delete basePtr` для polymorphic object має undefined behavior. В embedded C++ це актуально для driver interfaces, HAL abstractions або state machines, але dynamic allocation часто замінюють static lifetime чи placement new.[^dou-embedded-interview]

## Detailed explanation

TODO
