---
id: emb-tmplcx-0018
title: "Як працює `if constexpr` і чим він кращий за `#ifdef`?"
description: "Умова обчислюється на етапі компіляції; відкинута гілка не породжує коду, а в шаблоні ще й не інстанціюється."
track: embedded
section: templates-and-constexpr
level: junior
type: mechanism
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

## Question code

```cpp
template<typename P>
void init_uart() {
  if constexpr (std::is_same_v<P, STM32F4>) {
    USART1->BRR = compute_brr(115200);
  } else {
    static_assert(always_false<P>, "unsupported");
  }
}
```

## Short answer

**Умова обчислюється на етапі компіляції; відкинута гілка в шаблоні не інстанціюється, тож для неї не генерується код.**[^cpp-draft-stmt-if] Препроцесор `#ifdef` пропускає токени невибраної гілки.[^cpp-draft-cpp-cond] Компілятор же перевіряє синтаксис відкинутої гілки `if constexpr`.[^cpp-draft-stmt-if] Залежні від template-параметра частини відкинутої гілки не інстанціюються, тож їхні помилки типів не проявляються.[^cpp-draft-stmt-if] Правило: `if constexpr` – типобезпечна заміна `#ifdef` для платформо-залежного коду.

## Detailed explanation

`if constexpr` вибирає гілку під час компіляції, і умова має бути константним виразом.[^cpp-draft-stmt-if] Коли умова залежить від template-параметра `P`, відкинута гілка після інстанціації не створюється. Для `P = STM32F4` гілка `else` не інстанціюється, тож `static_assert` навіть не обчислюється; для будь-якого іншого `P` активною стає саме `else`, і `static_assert(always_false<P>, ...)` відхиляє збірку.

Препроцесорний `#ifdef` працює інакше. У пропущеній групі препроцесор обробляє лише ім’я директиви, щоб відстежувати вкладеність, а решту токенів ігнорує, тому синтаксично зламаний текст у ній компілятор не бачить.[^cpp-draft-cpp-cond] Наприклад, `#if 0` з рядком `int broken = ;` збирається без помилок.

`if constexpr` не скасовує перевірок повністю. Відкинутий оператор лишається частиною програми, тож його синтаксис перевіряється. Якщо для шаблону чи substatement `if constexpr` усередині шаблону немає жодної коректної специалізації, програма некоректна (NDR), і компілятори це діагностують: неоголошена функція у відкинутій гілці дає помилку і в GCC, і в Clang.[^cpp-draft-temp-res] Але залежна від `P` частина перевіряється лише тоді, коли гілка стає активною: `p.nope()` у `if constexpr (sizeof(P) > 100)` не дає помилки для `int`, а помилка проявиться лише тоді, коли шаблон інстанціюють із типом, для якого гілка активна.

Отже, `if constexpr` краще за `#ifdef` для синтаксису й неоголошених імен, але не для залежних від шаблону частин. Для них потрібна збірка з типом, який реально активує гілку (див. qid:emb-tmplcx-0019).

**Типові помилки:**

- Використовувати в `if constexpr` умову, яка не є константним виразом (наприклад, звичайну змінну): це помилка компіляції, а не вибір гілки під час виконання.[^cpp-draft-stmt-if]
- Вважати, що `if constexpr` перевіряє типи в усіх гілках: синтаксис і неоголошені імена перевіряються, а залежні від шаблону вирази – лише при інстанціації.
- Збирати тільки одну платформу: помилки в залежній гілці `if constexpr` не з’являються, доки її не використано з відповідним типом.

## Sources

<!-- generated from frontmatter -->
