---
id: emb-fnptr-0053
title: "Trap: чому weak hooks гірші за explicit callback для кількох інстансів driver-а?"
description: "Weak function має одне глобальне ім’я і не несе per-instance context."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
  - source_id: gcc-weak-attribute
    title: "GCC: Common Function Attributes – weak"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
    accessed: 2026-10-04
    kind: official
    version: "GCC current documentation"
    applicability: "Описує GNU weak attribute і можливість override для підтримуваних ELF/a.out toolchain; це розширення компілятора, не гарантія ISO C."
---

## Short answer

<span class="warn">Weak hook сам по собі не передає per-instance context.</span>[^gcc-weak-attribute]

Якщо є два UART-и або два timer-и, функція з одним глобальним ім’ям не визначає, до якого екземпляра належить подія. Weak override також обирається на етапі link, а не реєструється окремо для кожного пристрою.[^gcc-weak-attribute]

Для reusable drivers передавай callback і context окремо; weak hooks залишай для глобальних startup defaults або board-level extension points.

## Detailed explanation

Weak hook має одне ім’я зовнішнього символу, яке linker розв’язує для всієї програми. Weak definition дає fallback-реалізацію, а сильний override підміняє її відповідно до правил toolchain. У такому механізмі немає автоматичного аргументу, що повідомив би функції, який із кількох однакових driver-ів викликав її; аргументи функції задаються її сигнатурою, а не атрибутом `weak`.[^gcc-weak-attribute]

Це відрізняє hook від callback table або API реєстрації. Реєстрація може зберегти пару `callback + context` у структурі кожного UART. Коли надходить подія, driver викликає callback саме цього екземпляра й передає його context. Для weak hook зазвичай потрібна інша схема: окремі функції з різними символами або глобальна таблиця, яку хтось має підтримувати самостійно.

Проблема проявляється, коли копіюють reusable driver для другого пристрою, але обидва обробники зводяться до одного символу на кшталт `uart_rx_hook`. Тоді override не може самостійно розрізнити джерело події. Додавання глобальної змінної «поточний UART» не розв’язує проблему надійно, якщо два пристрої можуть генерувати події поруч у часі або з різних контекстів.

Приклад: структури `uart1` і `uart2` можуть кожна містити власний callback та `context` на буфер стану. Одна загальна функція обробки приймає `context` і тому працює з правильним екземпляром; у варіанті лише з weak symbol довелося б розрізняти пристрої через окремі глобальні hook-и або іншу явну маршрутизацію.

**Типові помилки:**

- Вважати, що weak symbol автоматично передає адресу периферії, яка породила подію.
- Вирішувати проблему через один змінний global pointer без захисту від конкурентних подій.
- Застосовувати linker override там, де потрібна runtime-конфігурація кількох інстансів.

Для повторно використовуваного driver-а визначай, хто володіє callback і як довго живе його context. Weak hooks залишай для єдиної глобальної точки розширення, а інстанс-специфічну поведінку моделюй явними даними та реєстрацією.[^gcc-weak-attribute]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
