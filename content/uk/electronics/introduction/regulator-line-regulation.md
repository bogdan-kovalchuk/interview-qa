---
id: emb-elintro-0187
title: "Що таке line regulation стабілізатора?"
description: "Що таке line regulation стабілізатора?"
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
    applicability: "Визначення line regulation та її вимірювання; не задає універсальний відсоток для простого Зенерівського кола."
  - source_id: aac-zener-regulator
    title: "All About Circuits: What Are Zener Diodes?"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/zener-diodes/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Межа стабілізації за доступним струмом у колі зі стабілітроном."
---

## Short answer

Line regulation описує зміну вихідної напруги регулятора при зміні `V_in` за фіксованого навантаження і часто задається як `ΔV_out/ΔV_in` або у відсотках на вольт.[^ti-regulator-regulation] Для простого стабілізатора на Зенері її не можна узагальнити до фіксованих 5% чи умови `V_in ≥ V_Z + 3 V`: межа залежить від `R_s`, струму навантаження та мінімального струму стабілітрона.[^aac-zener-regulator]

## Detailed explanation

Line regulation – це показник того, наскільки вихідна напруга змінюється, коли змінюють вхідну напругу, залишаючи навантаження незмінним. Його вимірюють у заданому діапазоні входу та за вказаних умов; для лінійних стабілізаторів виробник може вказати `ΔV_out/ΔV_in` або відносну зміну на вольт. Менше значення означає, що зміна входу слабше передається на вихід у цьому режимі.[^ti-regulator-regulation]

У простому колі зі стабілітроном вхідна напруга визначає струм через `R_s`. За приблизно сталого виходу збільшення `V_in` збільшує цей струм, і за сталого навантаження додаткова частина переважно проходить через стабілітрон. Зміни його струму трохи змінюють напругу через ненульовий динамічний опір, тому вихід не є математично незмінним. Якщо вхід знизиться так, що струму вже не вистачить навантаженню й мінімальному струму стабілітрона, регулятор залишає режим стабілізації; це межа headroom, а не відсоткова характеристика line regulation.[^aac-zener-regulator]

Приклад: якщо за незмінного навантаження виміряно `V_out = 5.08 V` при `V_in = 9 V` і `V_out = 5.12 V` при `V_in = 12 V`, то зміна виходу становить `40 mV` при зміні входу `3 V`. Відношення `ΔV_out/ΔV_in` дорівнює приблизно `13.3 mV/V` на цьому інтервалі. Це лише результат конкретного вимірювання, а не типовий норматив для всіх стабілізаторів.

**Типові помилки:**

- Плутати line regulation із load regulation: тут змінюється вхід, а навантаження фіксоване.
- Називати «5%» універсальною межею або вважати `V_Z + 3 V` точною умовою: необхідний запас залежить від струмів, резистора й параметрів компонента.[^aac-zener-regulator]

## Sources

<!-- generated from frontmatter -->
