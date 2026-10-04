---
id: emb-patterns-0025
title: "Trap: чому без `volatile` цей polling-цикл стає нескінченним?"
description: "Компілятор читає SR один раз, бачить, що прапорець не виставлений, і більше не перечитує – у C abstract machine ніщо не змінює SR."
track: embedded
section: common-code-patterns
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
while (!(REG->SR & FLAG))
    ;
```

## Short answer

<span class="warn">Компілятор читає `SR` один раз, бачить, що прапорець не виставлений, і більше не перечитує</span> – у C abstract machine ніщо не змінює `SR`.

Результат: цикл крутиться на закешованому значенні вічно, навіть коли апаратура вже виставила прапорець.

Захист: оголоси регістр `volatile` – тоді доступ до нього лишається спостережуваним для C abstract machine; це не замінює синхронізацію між потоками чи ISR.[^iso-c-n1570]

## Detailed explanation

`volatile` у типі регістра повідомляє компілятору, що значення може змінитися поза звичайним потоком виконання програми. За правилами C вирази, які звертаються до такого об’єкта, обчислюються відповідно до abstract machine, а доступи не можна просто прибрати як зайві; саме тому polling-код повторно читає апаратне поле.[^iso-c-n1570]

Якщо поле не `volatile`, тіло циклу не змінює його, тож оптимізатор може зчитати значення перед циклом і повторно використовувати його. Це допустима оптимізація, коли програма не описує зовнішню зміну. Результатом може стати зациклення навіть після того, як периферія встановила прапорець.

Оголошення `volatile` не є повним засобом синхронізації. Воно не забезпечує атомарність складеної операції, взаємне виключення між потоком та ISR, memory barrier для всіх архітектур чи правильну послідовність записів у конкретну периферію. Типи й макроси CMSIS або vendor HAL можуть задавати потрібний спосіб доступу; регістри з read-to-clear або write-one-to-clear семантикою потребують окремої обережності.

Приклад: якщо `STATUS` у memory map має правильний volatile-qualified тип, повторне читання у циклі може побачити зміну hardware:

```c
while ((STATUS & READY) == 0u) {
    /* hardware may set READY */
}
```

**Типові помилки:**

- Вважати `volatile` синонімом atomic або mutex.
- Застосувати `volatile` до локальної копії, а не до доступу за адресою регістра.
- Припускати однакову семантику для всіх регістрів і платформ.

Для довгого очікування додайте timeout або перейдіть на interrupt, щоб несправність периферії не зависила систему назавжди.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
