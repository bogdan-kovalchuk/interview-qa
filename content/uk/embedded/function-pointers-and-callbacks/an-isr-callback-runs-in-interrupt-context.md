---
id: emb-fnptr-0026
title: "Чому callback з ISR має бути коротким?"
description: "ISR callback виконується в interrupt context, де не можна довго блокувати систему."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: concept
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
  - source_id: arm-interrupt-latency
    title: "Arm: A Beginner’s Guide on Interrupt Latency"
    url: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/beginner-guide-on-interrupt-latency-and-interrupt-latency-of-the-arm-cortex-m-processors
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює interrupt latency та обробку переривань на Cortex-M; деталі пріоритетів і вкладеності залежать від конкретного ядра та MCU."
  - source_id: freertos-isr-api
    title: "FreeRTOS Reference Manual V10.0.0: API Usage Restrictions"
    url: https://en.freertos.org/media/2018/FreeRTOS_Reference_Manual_V10.0.0.pdf
    accessed: 2026-10-04
    kind: official
    version: "V10.0.0"
    applicability: "Підтверджує обмеження FreeRTOS API для ISR та FromISR-виклики; не визначає правила інших RTOS чи MCU."
---

## Short answer

**ISR callback виконується в interrupt context**, тому його робота має бути короткою й обмеженою правилами ISR конкретної платформи.

Довга обробка затримує повернення до перерваного коду та може збільшити час очікування інших переривань. Наприклад, FreeRTOS забороняє з ISR API-функції без суфікса `FromISR`; callback-контракт має вказувати контекст виклику.

Правило: ISR callback швидко фіксує подію або сповіщає task дозволеним ISR-safe способом, а тривалу роботу переносить у thread/main context.[^embeddedinterviewlab] [^arm-interrupt-latency] [^freertos-isr-api]

## Detailed explanation

ISR callback – це callback, який виконується як частина обробки переривання, а не як звичайна функція в main loop чи task. Тому її тривалість впливає на час, протягом якого процесор залишається в обробнику, і на затримку повернення до звичайного коду. У системі з пріоритетами конкретний вплив на інші переривання залежить від контролера, пріоритетів і правил вкладеності, але зайву роботу в цьому контексті варто уникати.[^arm-interrupt-latency]

Callback може бути викликаний драйвером усередині ISR навіть тоді, коли його зареєстрував application code. Тож контракт API має явно повідомляти про цей контекст: звичайний callback-код часто очікує, що може чекати, блокуватися або використовувати task-level API, тоді як ISR зазвичай цього не дозволяє. Наприклад, FreeRTOS вимагає використовувати з ISR відповідні API-функції із суфіксом `FromISR` і має додаткові обмеження для пріоритетів переривань.[^freertos-isr-api]

Типовий шаблон – зчитати мінімальний статус периферії, зберегти потрібні дані в короткий буфер, очистити interrupt condition згідно з документацією MCU, а потім повідомити task або виставити flag. Конкретний порядок очищення та синхронізації залежить від периферії; пропуск очищення може спричинити повторний виклик ISR, а передчасне очищення – втрату події. Важке опрацювання пакета, форматування рядків і довге очікування належать до звичайного контексту.[^freertos-isr-api]

**Типова помилка:** написати у callback повний шлях обробки, бо він виглядає як звичайна функція. Це може створити jitter чи порушити дедлайн, а блокувальний API може зависнути або бути заборонений. Перевіряй документацію драйвера й RTOS, що саме безпечно викликати з ISR, та залишай у callback лише мінімальні дії.[^arm-interrupt-latency] [^freertos-isr-api]

Приклад: callback UART може зчитати байт і покласти його в кільцевий буфер, після чого розбудити task через ISR-специфічне сповіщення. Task уже збирає повне повідомлення, перевіряє його формат і виконує повільну команду. Якщо буфер переповнений, callback має застосувати явно визначену політику, а не чекати звільнення місця в ISR.[^freertos-isr-api]

## Sources

<!-- generated from frontmatter -->
