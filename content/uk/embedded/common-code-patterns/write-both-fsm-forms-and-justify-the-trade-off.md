---
id: emb-patterns-0042
title: "Що має вміти кандидат у питаннях про embedded code patterns?"
description: "Писати FSM (finite state machine) у обох формах: switch і table; пояснювати trade-off-и; будувати ring buffer на степені двійки без спільного count (він дає race); робити bit operations через unsigned mask-and-shift."
track: embedded
section: common-code-patterns
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Підтверджує правила зсувів і беззнакової арифметики (6.5.7, 6.2.5 п. 9), семантику `volatile` (6.7.3 п. 7), data race як undefined behavior (5.1.2.4 п. 25) і те, що `malloc` може повернути null (7.22.3); конкретні пристрої й тулчейни можуть відрізнятися."
  - source_id: holzmann-power-of-ten
    title: "The Power of Ten – Rules for Developing Safety Critical Code (G. J. Holzmann, NASA/JPL)"
    url: https://spinroot.com/gerard/pdf/P10.pdf
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Стаття автора з NASA/JPL, розміщена на його сайті: правило 3 забороняє динамічне виділення пам’яті після ініціалізації, бо алокатори на кшталт malloc і garbage collectors часто мають непередбачувану поведінку, що помітно впливає на продуктивність. Це настанова, а не вимога конкретного safety-стандарту; про фрагментацію heap стаття прямо не говорить."
  - source_id: linux-circular-buffers
    title: "Circular Buffers (Linux kernel documentation)"
    url: https://www.kernel.org/doc/html/latest/core-api/circular-buffers.html
    accessed: 2026-10-06
    kind: official
    version: "7.3.0-rc6"
    applicability: "Підтверджує, що для буфера розміром у степінь двійки обгортання індексу робиться побітовим AND замість ділення, і що схема з одним producer і одним consumer не потребує спільного локу. Це документація ядра Linux (SMP), а не bare-metal MCU."
---

## Short answer

**Писати FSM (finite state machine) у обох формах: switch і table; пояснювати trade-off-и; будувати ring buffer розміром у степінь двійки й знати, чому спільний `count` дає race; робити bit operations через unsigned mask-and-shift.**

Плюс: консистентні return codes із перевіркою всіх результатів, `volatile` для регістрів (але не як синхронізація з ISR), guard clauses для null/діапазону.[^iso-c-n1570]

Правило: до кожного патерну май відповідь «коли застосовувати», «чи ISR-safe (interrupt service routine safe)» і «чому без heap».

## Detailed explanation

Це питання – не про один факт, а про набір базових патернів, які перевіряють на короткій задачі «напиши ціле». Для кожного важливо назвати не лише код, а й межі, у яких він працює.

**FSM у двох формах.** Версія з `switch` по `enum` читається найпростіше, а компілятор може попередити про пропущений case. Таблиця handler-ів зручніша, коли станів і подій багато, але вимагає перевірки індексу перед викликом (див. qid:emb-patterns-0040), а вибір між формами робиться за читабельністю й вимірюваннями, а не за фіксованою кількістю станів (qid:emb-patterns-0029).

**Ring buffer.** Якщо розмір буфера – степінь двійки, обгортання індексу виконується як `idx & (SIZE - 1)` без ділення.[^linux-circular-buffers] Спільний `count`, який збільшує producer і зменшує consumer, – це два read-modify-write над однією змінною, тобто race між main і ISR; безпечніше, коли кожен індекс має одного writer-а (див. qid:emb-patterns-0041).[^linux-circular-buffers]

**Bit operations.** Роботу з бітами роблять на беззнакових типах: беззнакова арифметика ніколи не переповнюється, а лише береться за модулем.[^iso-c-n1570] Зсув на кількість бітів, не меншу за ширину операнда, або від’ємну – undefined behavior; те саме для лівого зсуву знакового значення, результат якого не вміщується в тип.[^iso-c-n1570] Тому `1 << 31` на 32-бітному `int` – помилка, а `uint8_t` у виразі `b << 24` спершу стає `int`, і значення від `0x80` ламає зсув. Приклад (ілюстративний):

```c
#define BIT(n)  (UINT32_C(1) << (n))            /* n у діапазоні 0..31 */

static inline uint32_t reg_set_field(uint32_t reg, uint32_t mask,
                                     unsigned shift, uint32_t value)
{
    return (reg & ~mask) | ((value << shift) & mask);
}

ctrl = reg_set_field(ctrl, 0xF0u, 4u, 0x5u);    /* біти 7..4 стають 0x5 */
```

**Решта.** Доступ до `volatile` об’єкта – side effect, який компілятор не має права прибрати чи злити, тому `volatile` потрібен для регістрів; але він не робить доступ атомарним і не синхронізує main з ISR.[^iso-c-n1570] Код повернення треба перевіряти, а guard clauses на початку функції відсікають null і значення поза діапазоном. «Без heap» має кілька причин: `malloc` може повернути null,[^iso-c-n1570] час виконання алокатора не є детермінованим, а після тривалої роботи heap може фрагментуватися. Настанова Holzmann для safety-critical коду прямо забороняє динамічне виділення пам’яті після ініціалізації, бо алокатори на кшталт `malloc` мають непередбачувану поведінку, яка помітно впливає на продуктивність.[^holzmann-power-of-ten] Тому прошивка з жорсткими обмеженнями розподіляє пам’ять статично, і її обсяг видно з map file ще до запуску.

**Типові помилки:**

- Відповідати «беру `switch`» без trade-off, перевірки індексу й відповіді про ISR-safety.
- Писати `1 << 31` або зсув знакового значення замість `1u` чи `UINT32_C(1)`.
- Вважати `volatile` синхронізацією між ISR і main.
- Ігнорувати код повернення або не перевіряти результат `malloc`.

## Sources

<!-- generated from frontmatter -->
