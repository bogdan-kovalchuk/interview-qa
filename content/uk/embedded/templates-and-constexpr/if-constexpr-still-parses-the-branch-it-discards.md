---
id: emb-tmplcx-0019
title: "Trap: чим `if constexpr` безпечніший за `#ifdef` щодо помилок?"
description: "#ifdef пропускає невибрану гілку без перевірки C++-синтаксису, тож опечатки в ній не видно до її ввімкнення."
track: embedded
section: templates-and-constexpr
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; це джерело не є доказом тверджень."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
  - source_id: cpp-draft-stmt-if
    title: "C++ working draft: The if statement ([stmt.if])"
    url: https://eel.is/c++draft/stmt.if
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Для if constexpr: у шаблоні відкинута substatement не інстанціюється, якщо після інстанціації умова вже не залежить від значень; умова має бути константним виразом. Не каже, який код видає конкретний компілятор."
  - source_id: cpp-draft-cpp-cond
    title: "C++ working draft: Conditional inclusion ([cpp.cond])"
    url: https://eel.is/c++draft/cpp.cond
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Обробляється лише перша група з істинною умовою; у пропущеній групі решта препроцесорних токенів ігнорується. Не описує конкретний препроцесор."
  - source_id: cpp-draft-temp-res
    title: "C++ working draft: Name resolution ([temp.res])"
    url: https://eel.is/c++draft/temp.res
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що програма некоректна (NDR), якщо для шаблону чи substatement if constexpr усередині шаблону не може бути жодної коректної специалізації, а шаблон не інстанційовано. Конкретні діагностики компіляторів не описує."
---

## Short answer

<span class="warn">`#ifdef` пропускає невибрану гілку без перевірки C++-синтаксису – опечатки в ній не видно, доки гілку не ввімкнено.</span>[^cpp-draft-cpp-cond]

`if constexpr` змушує компілятор перевірити синтаксис обох гілок, тож синтаксична помилка в «неактивній» платформі виявиться одразу.[^cpp-draft-stmt-if]

Але помилки типів, що залежать від template-параметра, у відкинутій гілці не проявляються: вона не інстанціюється.[^cpp-draft-stmt-if]

Захист: для платформо-перемикань надавай перевагу `if constexpr` і збирай кожну платформу, бо залежні частини перевіряються лише при інстанціації.

## Detailed explanation

`#ifdef` і `#if` обробляє препроцесор, до того як компілятор бачить C++. Якщо умова хибна, група пропускається: з директив обробляється лише ім’я, щоб відстежувати вкладеність, а решта токенів ігнорується.[^cpp-draft-cpp-cond] Тому помилка в невибраному блоці – наприклад, пропущена крапка з комою в `#else`-гілці для іншої плати – не дає жодного повідомлення, поки збірка не вибере цю гілку.

`if constexpr` змінює це для коду в шаблоні. Відкинутий оператор лишається частиною програми, тож його синтаксична помилка – помилка компіляції. Неоголошене ім’я у відкинутій гілці теж дає помилку, бо для шаблону немає жодної коректної специалізації, тож програма некоректна (NDR).[^cpp-draft-temp-res] Залежна від template-параметра частина не інстанціюється, тож її помилка типу не проявляється: `p.nope()` у гілці `if constexpr (sizeof(P) > 100)` не дає помилки для `int`, бо гілка для нього відкинута.[^cpp-draft-stmt-if]

Практичний висновок: `if constexpr` безпечніший за `#ifdef` для синтаксису й неоголошених імен, але не для залежних від шаблону частин. Для них потрібна збірка з типом, який реально активує гілку; див. qid:emb-tmplcx-0018.

**Типові помилки:**

- Збирати лише поточну платформу: помилки в інших гілках не видно ні в `#ifdef`, ні в залежному від шаблону `if constexpr`.
- Тимчасово відключати код через `#if 0`, вважаючи, що компілятор його перевіряє: препроцесор його пропускає, тож синтаксичні помилки лишаються.
- Вважати, що `if constexpr` перевіряє типи всіх гілок: залежні від шаблону вирази перевіряються лише для активної інстанціації.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
