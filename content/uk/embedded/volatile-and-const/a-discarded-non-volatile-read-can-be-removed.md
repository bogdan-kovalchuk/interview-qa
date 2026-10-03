---
id: emb-volconst-0036
title: "Trap: що не так із читанням register без використання результату?"
description: "Якщо macro не volatile, компілятор може прибрати це читання."
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
  - source_id: gcc-volatile
    title: "GCC documentation: Volatiles"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Описує поведінку volatile-доступів і discarded scalar expressions саме в GCC; це не універсальна гарантія для кожного компілятора."
---

## Question code

```c
#define ADC_DR (*( uint32_t *)0x4001204C)

ADC_DR;
```

## Short answer

<span class="warn">Якщо lvalue register не має кваліфікатора `volatile`, компілятор може прибрати читання.</span>

Читання data register може очищати апаратний flag або витягувати sample з FIFO; звичайний `uint32_t` expression statement не має такого видимого для C ефекту, тому компілятор може видалити його. Для скалярного volatile-об’єкта GCC трактує навіть discarded expression як читання, хоча визначення volatile access залежить від реалізації.

Захист: оголошуй MMIO register як volatile, наприклад `(*(volatile uint32_t *)address)`. Cast `(void)` лише пояснює намір і сам по собі не надає звичайному об’єкту volatile-семантики.[^gcc-volatile]

## Detailed explanation

`volatile` у типі MMIO-доступу повідомляє компілятору, що цей доступ має значення поза звичайною моделлю змінних програми. Умова задачі важлива: якщо `ADC_DR` має тип звичайного `uint32_t`, вираз `ADC_DR;` обчислює значення і відкидає його, а жоден подальший код це значення не використовує. З погляду абстрактної машини C результат не змінює програму, тож оптимізатор може викинути завантаження з адреси.[^iso-c-n1570]

Для периферії таке завантаження може бути операцією: читання очищає прапорець, підтверджує переривання або знімає елемент FIFO. GCC документує, що скалярний volatile-об’єкт, використаний у void-контексті, читається; водночас стандарт залишає конкретне визначення volatile access реалізації. Тому регістри описують через volatile-qualified тип у заголовку конкретного MCU, а не покладаються на побічний ефект звичайного читання.[^gcc-volatile]

Показаний cast `(void)ADC_DR` не є заміною `volatile`: він лише явно відкидає значення. Якщо вираз уже volatile, cast залишає сам volatile-доступ; якщо ні – оптимізатор може прибрати завантаження. Також `volatile` не визначає адресу, ширину транзакції чи дозвіл читання регістра. Це треба перевірити в reference manual MCU.

**Типові помилки:**

- Вважати, що будь-який доступ за фіксованою адресою автоматично є апаратним доступом для компілятора.
- Додавати `(void)` і вважати це еквівалентом volatile.
- Вважати volatile достатнім для порядку між різними звичайними об’єктами пам’яті.

Для такого register macro потрібні коректна адреса, тип і volatile-кваліфікація; для конкретного периферійного register слід наслідувати визначення з vendor header.[^gcc-volatile]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
