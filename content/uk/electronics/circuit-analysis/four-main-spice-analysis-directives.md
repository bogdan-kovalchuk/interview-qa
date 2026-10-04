---
id: emb-elcirc-0038
title: "Які чотири основні директиви SPICE-аналізу?"
description: "Які чотири основні директиви SPICE-аналізу?"
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
  - source_id: ngspice-analysis-manual
    title: "ngspice User's Manual"
    url: https://ngspice.sourceforge.io/docs/ngspice-manual.pdf
    accessed: 2026-10-04
    kind: official
    version: "current manual"
    applicability: "Описує значення .op, .tran, .ac і .dc саме в ngspice; параметри директив можуть мати відмінності між симуляторами."
---

## Short answer

`.op` знаходить DC operating point, `.tran` обчислює часовий перехідний процес, `.ac` – малосигнальну частотну відповідь, а `.dc` змінює DC-параметр або джерело й обчислює робочу точку для кожного значення.[^ngspice-analysis-manual] Ці назви та директиви відповідають ngspice; підтримку і синтаксис конкретного симулятора перевіряють у його документації.[^ngspice-analysis-manual]

## Detailed explanation

У ngspice чотири поширені аналізи відповідають на різні запитання про ту саму схему: робоча точка, поведінка в часі, малосигнальна відповідь за частотою або реакція на зміну DC-значення.[^ngspice-analysis-manual]

`.op` обчислює DC operating point: напруги вузлів і струми гілок у сталому режимі. Це корисно для перевірки bias у транзисторному каскаді; конденсатори трактуються як розімкнені, а індуктивності як коротке замикання у стандартному розрахунку робочої точки.[^ngspice-analysis-manual]

`.tran` розв’язує схему в послідовних часових точках, щоб показати, як вихід змінюється після імпульсу, вмикання або іншого часового збудження. Потрібні часовий інтервал і параметри кроку; надто великий крок може приховати швидкі зміни, а нелінійності та складна схема можуть збільшити час обчислення.[^ngspice-analysis-manual]

`.ac` виконує малосигнальний аналіз у частотній області. Симулятор спершу знаходить DC operating point, лінеаризує нелінійні моделі поблизу нього, а потім обчислює комплексну відповідь на AC-збудження для заданих частот. Це дає амплітуду й фазу, але не є часовою симуляцією великого сигналу.[^ngspice-analysis-manual]

`.dc` змінює вибране джерело чи параметр у заданому діапазоні та повторно обчислює DC-стан. Так можна побудувати передавальну характеристику, наприклад вихідну напругу залежно від вхідного DC-рівня. На відміну від `.tran`, послідовність значень тут не означає перебіг часу.[^ngspice-analysis-manual]

**Типова помилка:** називати будь-який графік виходу «AC-аналізом». Вибір залежить від питання: сталий режим – `.op`, часова форма – `.tran`, малосигнальна залежність від частоти – `.ac`, статичне sweep-залежність – `.dc`.[^ngspice-analysis-manual]

## Sources

<!-- generated from frontmatter -->
