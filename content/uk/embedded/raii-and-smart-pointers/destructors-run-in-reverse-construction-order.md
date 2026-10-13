---
id: emb-raii-0021
title: "Чому вкладені ресурси звільняються у зворотному порядку автоматично?"
description: "Деструктори локальних об’єктів викликаються у порядку, ЗВОРОТНОМУ до конструювання."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
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
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements ([stmt.jump])"
    url: https://eel.is/c++draft/stmt.jump
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "У примітці: при виході зі scope, яким би способом він не був досягнутий, автоматичні об’єкти, сконструйовані в ньому, знищуються у зворотному порядку конструювання. Про exit(), abort() і longjmp тут нічого не сказано."
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що бази й нестатичні члени знищуються у зворотному порядку завершення їх конструкторів. Локальні змінні тут не розглядаються."
  - source_id: cpp-draft-support-start-term
    title: "C++ working draft: Start and termination ([support.start.term])"
    url: https://eel.is/c++draft/support.start.term
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що std::abort завершує програму без виконання деструкторів для об’єктів automatic, thread і static storage duration; у зноски сказано, що exit() не знищує автоматичні об’єкти. Про embedded-рантайми нічого не говорить."
  - source_id: cpp-draft-support-runtime
    title: "C++ working draft: Other runtime support ([support.runtime])"
    url: https://eel.is/c++draft/support.runtime
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що пара setjmp/longjmp має невизначену поведінку, якщо заміна її на catch і throw викликала б нетривіальні деструктори автоматичних об’єктів. Конкретних MCU-рантаймів не описує."
---

## Short answer

**Деструктори локальних об’єктів викликаються у порядку, ЗВОРОТНОМУ до конструювання.**

Якщо взяв clock, потім SPI, потім CS – звільнення піде CS -> SPI -> clock, що зазвичай і є правильним порядком teardown.[^cpp-draft-stmt-jump] Вручну це легко переплутати.

Правило: оголошуй RAII-guard’и у порядку залежностей; reverse destruction спрацьовує при виході зі scope, але не при `exit()` чи `abort()`, які не знищують автоматичні об’єкти.[^cpp-draft-support-start-term]

## Detailed explanation

Порядок знищення локальних об’єктів не треба записувати вручну: компілятор сам викликає деструктори при виході з блоку. Стандарт формулює це так: при виході зі scope, яким би способом він не був досягнутий, автоматичні об’єкти, сконструйовані в ньому, знищуються у зворотному порядку конструювання.[^cpp-draft-stmt-jump] Саме тому RAII-обгортка прив’язує звільнення ресурсу до часу життя змінної: вимкнення периферії, зняття CS чи закриття хендла відбувається при виході з функції, і через `return`, і через виняток.

Вкладені ресурси працюють так само: бази й нестатичні члени класу знищуються у зворотному порядку завершення їх конструкторів, тому член, оголошений пізніше, звільняється раніше.[^cpp-draft-class-dtor]

Приклад показує порядок залежностей: SPI тактується від clock, а CS працює через SPI. Оголошення в такому порядку дає правильне звільнення: спочатку CS, потім SPI, потім clock.

```cpp
// Illustrative: Clock, SpiBus and CsLine are driver RAII types.
void transfer(const uint8_t* data, size_t n) {
    Clock clk;        // 1st constructed: clock on
    SpiBus spi(clk);  // 2nd: uses clk, so it must go before clk
    CsLine cs(spi);   // 3rd: pulls CS low through spi
    spi.write(data, n);
}   // ~CsLine (CS high), ~SpiBus, ~Clock - reverse order
```

Межі правила: `exit()` не знищує автоматичні об’єкти, а `abort()` завершує програму без деструкторів.[^cpp-draft-support-start-term] `longjmp`, що минає автоматичні об’єкти з нетривіальними деструкторами, дає undefined behavior.[^cpp-draft-support-runtime] Якщо `main()` ніколи не повертається, як у типовому firmware, деструктори його локальних об’єктів не спрацюють, тож вимикати периферію треба явним кодом, а не сподіватися на RAII. Якщо ж залежні ресурси оголошено у зворотному порядку, clock вимкнеться раніше, ніж SPI перестане ним користуватися.

**Типові помилки:**

- Вважати, що RAII-guard спрацює при `exit()` або при `longjmp` з обробника помилки.
- Оголошувати залежні ресурси без урахування залежностей: reverse destruction іде за порядком оголошення, а не за змістом.
- Очікувати, що деструктори спрацюють при reset MCU: після скидання апаратури звільнення не виконується.

## Sources

<!-- generated from frontmatter -->
