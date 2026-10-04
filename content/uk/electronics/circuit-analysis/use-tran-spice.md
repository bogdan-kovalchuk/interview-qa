---
id: emb-elcirc-0045
title: "Коли використовувати `.op`, `.tran` і `.ac` у SPICE?"
description: "Коли використовувати `.op`, `.tran` і `.ac` у SPICE?"
track: electronics
section: circuit-analysis
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
    applicability: "Походження питання: лекція 31, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: ngspice-analysis-types
    title: "ngspice User's Manual: OP, TRAN, and AC Analyses"
    url: https://ngspice.sourceforge.io/docs/ngspice-manual.pdf
    accessed: 2026-10-04
    kind: official
    version: "current manual"
    applicability: "Визначення operating point, transient і small-signal AC аналізів у ngspice; деталі синтаксису можуть відрізнятися між SPICE-сумісними програмами."
---

## Short answer

`.op` знаходить DC operating point; `.tran` показує часову реакцію на задані стимули; `.ac` обчислює малосигнальну частотну характеристику навколо робочої точки. Для `.ac` потрібне AC-збудження джерела, а нелінійна поведінка за великим сигналом зазвичай досліджується через `.tran`.[^ngspice-analysis-types]

## Detailed explanation

Команда аналізу відповідає на конкретне запитання про модель кола. `.op` розв’язує DC operating point: сталі вузлові напруги та струми за DC умов. Ця точка важлива для нелінійних елементів, адже транзистор або діод працюватиме по-різному залежно від зміщення. У багатьох сценаріях симулятор також знаходить таку точку перед іншими аналізами, щоб отримати початкові умови чи лінеаризовану модель.[^ngspice-analysis-types]

`.tran` обчислює часову реакцію. Він підходить для запуску, перемикання, імпульсного збудження та нелінійної поведінки за великих сигналів. Треба задати тривалість і достатньо дрібний максимальний крок часу: надто грубий крок може пропустити швидкий фронт чи короткий імпульс. Початкові умови також впливають на перші моменти перехідного процесу.[^ngspice-analysis-types]

`.ac` аналізує малосигнальну поведінку в частотній області навколо DC operating point. Він дає змогу побачити підсилення та фазу як функцію частоти, але не є звичайним прогоном великого синусоїдального сигналу: нелінійні моделі лінеаризуються, а незалежне джерело повинно мати AC значення.[^ngspice-analysis-types]

Приклад: для RC-фільтра `.op` покаже сталі DC-рівні, `.tran` покаже заряджання конденсатора після стрибка входу, а `.ac` – зміну підсилення й фази зі частотою. Якщо шукають форму перемикання діода, `.ac` не замінить часовий аналіз.

**Типові помилки:**

- Вибирати `.ac` для великосигнального або нелінійного transient режиму; використовуйте `.tran`.
- Забувати задати AC amplitude джерела й отримати неінформативний частотний результат.
- Задавати часовий крок без огляду на найшвидшу подію в колі.

## Sources

<!-- generated from frontmatter -->
