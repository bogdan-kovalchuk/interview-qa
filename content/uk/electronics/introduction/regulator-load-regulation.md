---
id: emb-elintro-0188
title: "Що таке load regulation стабілізатора?"
description: "Що таке load regulation стабілізатора?"
track: electronics
section: introduction
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання: лекція 18, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: ti-regulator-regulation
    title: "TI: Identify the Most Accurate Linear Voltage Regulator"
    url: https://www.ti.com/document-viewer/lit/html/SSZTCA7/GUID-C15E9A5E-C4B2-4C77-98A3-C375536EE8EF
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Визначення load regulation; конкретні відсотки залежать від регулятора й умов вимірювання."
  - source_id: aac-zener-regulator
    title: "All About Circuits: What Are Zener Diodes?"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/zener-diodes/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Механізм і межа стабілізації за струмом навантаження для кола зі стабілітроном."
---

## Short answer

Load regulation описує зміну `V_out` при зміні струму навантаження за фіксованого входу; числове значення залежить від регулятора та умов вимірювання.[^ti-regulator-regulation] У простому Зенерівському колі збільшення `I_load` зменшує `I_Z`; коли `I_Z` падає нижче потрібного мінімуму, вихідна напруга просідає, а не перемикається миттєво.[^aac-zener-regulator]

## Detailed explanation

Load regulation показує, наскільки змінюється `V_out`, коли змінюють навантаження, утримуючи вхідну напругу сталою. Для лінійного стабілізатора її зазвичай подають як відносну зміну між заданими межами струму навантаження або як зміну напруги; порівнювати значення можна лише разом з умовами вимірювання.[^ti-regulator-regulation]

У shunt-регуляторі зі стабілітроном струм через `R_s` приблизно задається різницею `V_in` і `V_Z`. Цей струм розподіляється між навантаженням та стабілітроном. Коли навантаження збільшує споживання, `I_Z` зменшується, і регулювання зберігається лише доки лишається достатній запас струму для області стабілізації. Тому критерій для найбільшого навантаження та найменшого входу має враховувати мінімальний струм стабілітрона з його datasheet, а не просто віднімати довільну постійну величину від можливостей `R_s`.[^aac-zener-regulator]

Приклад: нехай джерело та резистор разом забезпечують `24 mA`, а за вибраною робочою точкою стабілітрону потрібно залишити щонайменше `5 mA`. Тоді в цій спрощеній точці навантаженню доступно не більш як `19 mA`. Якщо навантаження вимагає більше, стабілітрон не «вимикається» як ідеальний перемикач: струм його гілки спадає, і напруга на спільному вузлі відхиляється від номінальної. Числа тут ілюструють баланс струмів, а не параметри певного діода.

**Типові помилки:**

- Вважати 5–10% універсальною характеристикою всіх Зенерівських регуляторів; потрібні межі навантаження і критерій вимірювання.
- Розраховувати лише максимальний струм навантаження й не перевіряти, що при мінімальному вході стабілітрон зберігає потрібний струм.[^aac-zener-regulator]

## Sources

<!-- generated from frontmatter -->
