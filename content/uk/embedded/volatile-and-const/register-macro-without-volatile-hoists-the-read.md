---
id: emb-volconst-0007
title: "Trap: що не так із таким polling-кодом?"
description: "Бракує volatile у доступі до hardware register."
track: embedded
section: volatile-and-const
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
---

## Question code

```c
#define UART_SR (*( uint32_t *)0x40011000)

while ((UART_SR & 0x20) == 0) { }
```

## Short answer

<span class="warn">Доступ до memory-mapped register не має `volatile`.</span>

`UART_SR` розіменовує звичайний `uint32_t *`, тому C-компілятор не зобов’язаний трактувати кожне звернення як volatile-доступ; оптимізація може прибрати повторні читання. У release build polling тоді може не помітити зміну status register.[^iso-c-n1570]

Використайте `#define UART_SR (*(volatile uint32_t *)0x40011000u)` та перевірте, що адреса й ширина доступу відповідають документації MCU. `volatile` не доводить, що адреса правильна або що периферія підтримує такий доступ.[^iso-c-n1570]

## Detailed explanation

Проблема фрагмента в тому, що `UART_SR` розіменовує вказівник на звичайний `uint32_t`. Для компілятора це звичайний об’єкт: у тілі `while` немає запису до нього, тому він може зчитати значення один раз і використовувати його знову. Якщо апаратура встановить біт `0x20` після першого читання, програма може не побачити зміни й залишитися в циклі.[^iso-c-n1570]

Кваліфікатор ставлять на тип об’єкта, на який вказує макрос: `volatile uint32_t *`. Тоді розіменування створює volatile lvalue, а повторне обчислення умови циклу виконує volatile-доступ за правилами конкретної реалізації C. Важливо, що стандарт лишає визначення «доступу» реалізації, тому embedded-компілятор має документувати поведінку для memory-mapped I/O.[^iso-c-n1570]

**Приклад виправлення:**

```c
#define UART_SR (*(volatile uint32_t *)0x40011000u)

while ((UART_SR & 0x20u) == 0u) { }
```

Це виправляє лише кваліфікацію. Адресу, ширину й допустимий спосіб читання треба звірити з reference manual конкретного MCU: деякі регістри мають спеціальні правила читання, side effect або іншу ширину. Не кожен бітовий вираз придатний для регістра з read-to-clear семантикою.[^iso-c-n1570]

Для практичного polling варто додати timeout чи умову скасування, аби помилка периферії не зависила main loop. Якщо доступ відбувається з ISR чи паралельно з DMA, потрібні також гарантії атомарності й когерентності, визначені платформою; сам `volatile` їх не створює.[^iso-c-n1570]

**Типові помилки:**

- кваліфікувати вказівник (`uint32_t * volatile`), а не дані за адресою;
- копіювати адресу з прикладу без перевірки мапи регістрів;
- вважати `volatile` бар’єром синхронізації для всіх типів пам’яті.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
