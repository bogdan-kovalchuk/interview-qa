---
id: emb-cppoop-0018
title: "Як virtual dispatch шкодить детермінізму на простих ядрах?"
description: "Virtual call – це indirect branch через vptr/vtable, тому ціль виклику не видно напряму з інструкції."
track: embedded
section: cpp-classes-and-oop
level: junior
type: concept
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; це джерело не є доказом тверджень."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
  - source_id: cpp-draft-expr-call
    title: "C++ working draft: Function call ([expr.call])"
    url: https://eel.is/c++draft/expr.call
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що виклик virtual-функції виконує її final overrider у dynamic type об’єкта, а виклик через qualified-id викликає саме названу функцію; сам механізм (vptr/vtable) стандарт не задає."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Описує vtable як таблицю для dispatch virtual-функцій, vptr в об’єкті dynamic class і те, що запис vtable на більшості платформ еквівалентний вказівнику на функцію. Це ABI, а не стандарт мови: ABI конкретного тулчейну може відрізнятися, а про вартість у тактах документ нічого не каже."
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Документує -fdevirtualize (спроба перетворити виклики virtual-функцій на прямі; вмикається на -O2, -O3 і -Os); не гарантує, що конкретний виклик буде devirtualized."
  - source_id: absint-ait-wcet
    title: "Worst-Case Execution Time Prediction by Static Program Analysis (AbsInt)"
    url: https://www.absint.com/aiT_WCET.pdf
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Каже, що computed calls і branches, яких декодер не може розпізнати, потребують анотацій користувача з переліком можливих цілей. Йдеться про computed calls загалом (таблиці вказівників на функції, switch), а не саме про C++ virtual; це опис одного інструмента (aiT)."
  - source_id: arm-cortex-m7-trm
    title: "Arm Cortex-M7 Processor Technical Reference Manual (r0p2, DDI 0489B)"
    url: https://documentation-service.arm.com/static/5e906b038259fe2368e2a7bb
    accessed: 2026-10-06
    kind: official
    version: "r0p2"
    applicability: "Підтверджує, що Cortex-M7 має dynamic branch prediction з Branch Target Address Cache (або static predictor, якщо BTAC не задано); про інші ядра Cortex-M нічого не каже й вартості непрямого виклику не наводить."
---

## Short answer

**Virtual call – це indirect branch через vptr/vtable, тому ціль виклику не видно напряму з інструкції.**[^itanium-cxx-abi] На простих ядрах це кілька зайвих інструкцій, а головна проблема для real-time – аналіз: ціль залежить від dynamic type,[^cpp-draft-expr-call] а для worst-case execution time інструмент має знати можливі цілі.[^absint-ait-wcet] На ядрах із dynamic branch prediction, як Cortex-M7,[^arm-cortex-m7-trm] час виклику залежить ще й від передбачення.

Правило: у hot path і коді з WCET-вимогами надавай перевагу викликам із відомою на етапі компіляції ціллю (templates, CRTP).

## Detailed explanation

Для не-`virtual` методу ціль виклику відома з типу виразу ще на етапі компіляції. Для `virtual` стандарт вимагає викликати final overrider у dynamic type об’єкта,[^cpp-draft-expr-call] а тип об’єкта за вказівником на base у загальному випадку відомий лише під час виконання. Як це реалізовано, визначає ABI: в Itanium C++ ABI кожен об’єкт dynamic class містить vptr, що вказує на vtable, а запис vtable на більшості платформ еквівалентний вказівнику на функцію.[^itanium-cxx-abi] Тому `s->read()` перетворюється на читання vptr з об’єкта, читання запису з vtable і непрямий перехід; прямий виклик цього не потребує.

Через це virtual call шкодить передусім аналізованості, а не обов’язково швидкості. «Детермінізм» тут – питання доказовості: навіть коли виконання стабільне, треба показати, які функції можуть бути викликані. Інструмент статичного аналізу часу відновлює граф викликів з бінарника, а computed calls, яких він не розпізнав, потребують анотацій з переліком можливих цілей;[^absint-ait-wcet] без інформації про тип доводиться вважати можливою ціллю кожен override цієї функції. Компілятор теж не може підставити тіло, поки не знає dynamic type. GCC намагається devirtualize виклики на `-O2`, `-O3` і `-Os`, але це спроба, а не гарантія.[^gcc-optimize-options]

На ядрах із branch prediction картина складніша: Cortex-M7 має dynamic branch prediction з Branch Target Address Cache,[^arm-cortex-m7-trm] тож час непрямого переходу залежить від стану предиктора, а не лише від коду, і оцінка worst case для такого виклику обережніша, ніж для прямого.

Невеликий приклад (ілюстративний): перший виклик – virtual, у другому `qualified-id` забороняє virtual dispatch, і викликається саме названа функція.[^cpp-draft-expr-call]

```cpp
#include <cstdint>

struct Sensor { virtual std::int16_t read() = 0; };
struct Temp final : Sensor { std::int16_t read() override; };

std::int16_t via_base(Sensor& s) { return s.read(); }        // virtual call
std::int16_t via_temp(Temp& t)   { return t.Temp::read(); }  // qualified-id: direct call
```

**Типові помилки:**

- Вважати, що virtual завжди «повільний» або «недетермінований»: сам перехід не випадковий, проблема в доказі цілі та втраченому інлайнінгу.
- Розраховувати на devirtualization як на гарантію: вона залежить від рівня оптимізації й від того, чи видно dynamic type.[^gcc-optimize-options]
- Посилатися на AUTOSAR чи MISRA як на загальну заборону virtual у hot path: це залежить від редакції й конкретних правил проєкту, тож читай текст правила.

## Sources

<!-- generated from frontmatter -->
