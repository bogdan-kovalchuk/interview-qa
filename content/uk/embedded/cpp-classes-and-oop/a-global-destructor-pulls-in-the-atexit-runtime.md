---
id: emb-cppoop-0009
title: "Trap: чому просте оголошення деструктора може «роздути» ROM?"
description: "Деструктор глобального об'єкта може змусити лінкер підтягнути atexit()/__cxa_atexit runtime cleanup інфраструктуру – зайві байти ROM."
track: embedded
section: cpp-classes-and-oop
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
---

## Short answer

<span class="warn">Деструктор глобального об'єкта може змусити лінкер підтягнути `atexit()`/`__cxa_atexit` runtime cleanup інфраструктуру</span> – зайві байти ROM.

Для глобальних об'єктів компілятор має зареєструвати dtor, щоб викликати його при завершенні програми. У bare-metal firmware завершення часто не буває, тому ця інфраструктура непотрібна.

Захист: уникай non-trivial destructors у глобальних об'єктів; за потреби налаштуй toolchain (`-fno-use-cxa-atexit`) або тримай об'єкти «вічними».[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
