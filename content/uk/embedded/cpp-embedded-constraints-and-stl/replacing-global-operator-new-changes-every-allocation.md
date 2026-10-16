---
id: emb-cppstl-0008
title: "Trap: чому небезпечно перевизначати глобальний `operator new` на pool-аллокатор?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

<span class="warn">Це тихо змінює семантику КОЖНОЇ алокації, включно зі сторонніми бібліотеками.</span>

Будь-який код, що десь усередині кличе `new` (навіть бібліотечний), раптом піде через твій пул – з непередбачуваними наслідками для розміру/часу.

Захист: безпечніше взагалі `= delete` глобальний `operator new`, щоб випадкова heap-алокація стала compile error.[^embeddedinterviewlab]

## Detailed explanation

TODO
