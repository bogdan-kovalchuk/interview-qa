---
id: emb-patterns-0026
title: "Як коректно чекати прапорець TXE перед записом у UART (universal asynchronous receiver-transmitter)?"
description: "Спін на бітовому тесті статус-регістра, потім запис у data-регістр."
track: embedded
section: common-code-patterns
level: junior
type: mechanism
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
  - source_id: stm32f1-rm0008
    title: "RM0008 Reference manual: STM32F101xx, STM32F102xx, STM32F103xx, STM32F105xx and STM32F107xx advanced Arm-based 32-bit MCUs"
    url: https://www.st.com/content/ccc/resource/technical/document/reference_manual/59/b9/ba/7f/11/af/43/d5/CD00171190.pdf/files/CD00171190.pdf/jcr:content/translations/en.CD00171190.pdf
    accessed: 2026-10-04
    kind: official
    version: "RM0008"
    applicability: "Описує TXE як готовність USART data register прийняти наступні дані та відрізняє його від TC; застосовність обмежена переліченими STM32F1."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Question code

```c
void usart1_send(uint8_t b) {
  while (!(USART1->SR & BIT(7))) // wait TXE
    ;
  USART1->DR = b;
}
```

## Short answer

**Спін на бітовому тесті статус-регістра, потім запис у data-регістр.**

Для прикладу STM32F1 `BIT(7)` – маска TXE: прапорець означає, що data register може прийняти наступний байт, а не те, що весь кадр уже передано.[^stm32f1-rm0008]

Оголошення регістрів має забезпечувати повторні volatile-доступи; для довгих очікувань додай timeout.[^iso-c-n1570]

## Detailed explanation

У прикладі цикл читає status register доти, доки маска `BIT(7)` не стане ненульовою, і лише тоді записує байт у data register. Це polling: CPU активно перевіряє умову, тому між ітераціями не виконує іншу роботу. Для STM32F1 TXE означає, що data register доступний для наступного байта; назви `SR`, `DR` та номер біта не є універсальними для всіх UART.[^stm32f1-rm0008]

Зазвичай TXE означає, що передавальний data register готовий прийняти наступний байт. Це не обов’язково означає, що останній stop bit уже вийшов на лінію: для очікування повного завершення передавання периферія може мати окремий прапорець transmission complete. Це розрізнення важливе перед вимкненням UART або зміною режиму лінії.

Апаратні регістри мають бути оголошені способом, передбаченим toolchain і платформою, зазвичай як `volatile`; інакше оптимізатор може не перечитувати status field. Але `volatile` саме по собі не дає timeout і не вирішує конкуренцію, якщо кілька контекстів одночасно пишуть у той самий UART. Для довгих затримок interrupt або DMA часто дають змогу не витрачати CPU на активне очікування.

Приклад використовує API конкретного MCU, а не переносимий код для кожного UART:

```c
while ((USART1->SR & TXE_MASK) == 0u) {
    /* wait until the device permits the next write */
}
USART1->DR = byte;
```

**Типові помилки:**

- Вважати TXE ознакою завершення всього кадру.
- Копіювати бітову маску між різними сімействами MCU без перевірки reference manual.
- Залишати нескінченне очікування без timeout у системі, де зависання неприпустиме.

## Sources

<!-- generated from frontmatter -->
