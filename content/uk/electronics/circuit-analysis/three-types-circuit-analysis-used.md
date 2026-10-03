---
id: emb-elcirc-0001
title: "Які три типи аналізу кіл існують і де кожен застосовується?"
description: "Які три типи аналізу кіл існують і де кожен застосовується?"
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
    applicability: "Походження питання: лекція 27, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-spice-analysis-types
    title: "All About Circuits: DC Analysis in SPICE"
    url: https://www.allaboutcircuits.com/textbook/designing-analog-chips/simulation/dc-analysis-in-spice/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює значення DC-аналізу та його приклади; висновки стосуються аналізу схеми в SPICE."
  - source_id: aac-spice-ac-analysis
    title: "All About Circuits: AC Analysis in SPICE"
    url: https://www.allaboutcircuits.com/textbook/designing-analog-chips/simulation/ac-analysis-in-spice/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтверджує частотний малосигнальний аналіз навколо заданої робочої точки; нелінійна поведінка за великих сигналів може відрізнятися."
  - source_id: aac-spice-transient
    title: "All About Circuits: Transient Analysis in SPICE"
    url: https://www.allaboutcircuits.com/textbook/designing-analog-chips/simulation/transient-analysis-in-spice/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює часовий аналіз реакції схеми на заданий сигнал у SPICE."
---

## Short answer

DC-аналіз визначає робочий стан або залежність від постійного параметра, AC-аналіз оцінює малосигнальну частотну характеристику навколо робочої точки, а transient-аналіз показує напруги й струми в часі після зміни сигналу.[^aac-spice-analysis-types][^aac-spice-ac-analysis][^aac-spice-transient] DC підходить для перевірки зміщення транзистора, AC – для підсилення та фази за частотою, transient – для перехідного процесу після перемикання або імпульсу.[^aac-spice-analysis-types][^aac-spice-ac-analysis][^aac-spice-transient]

## Detailed explanation

Три назви описують різні зрізи поведінки однієї схеми. У DC-аналізі джерела задають постійні значення або їх послідовно змінюють, а результатом є робоча точка: напруги вузлів і струми гілок. Це допомагає перевірити, чи транзистор має потрібне зміщення, чи не насичений вихід і який струм споживає схема. У симуляторах також є DC sweep, де змінюють параметр джерела й спостерігають усталену відповідь; це не те саме, що спостерігати сигнал у часі.[^aac-spice-analysis-types]

AC-аналіз зазвичай є малосигнальним: спочатку визначається DC робоча точка, потім нелінійні елементи лінеаризуються поблизу неї, а вхід задається як мала синусоїдна зміна. Частотний sweep показує відношення амплітуд і фазу для різних частот. Так аналізують смугу пропускання фільтра або підсилювача, але він не прогнозує великосигнальне обмеження чи перехід через нелінійну область.[^aac-spice-ac-analysis]

Transient-аналіз розв’язує поведінку схеми в часі з урахуванням заданої форми джерела та початкових умов накопичувальних елементів. Він доречний для фронту цифрового сигналу, запуску живлення або заряджання конденсатора. Результат залежить від часового кроку, тривалості моделювання та початкової напруги конденсатора чи струму індуктора, тому ці параметри треба задавати так, щоб не пропустити швидку подію.[^aac-spice-transient]

Приклад вибору: для схеми підсилювача спершу перевіряють DC напруги та струми, далі AC підсилення в потрібному діапазоні частот, а transient-відповідь на реальний імпульс або ступінчасту зміну входу. Один тип аналізу не замінює інші: правильно обрана робоча точка сама по собі не доводить стабільності чи потрібної швидкодії.

**Типові помилки:**

- Називати AC-аналіз моделлю довільного великого сигналу: він зазвичай лінеаризований біля робочої точки.
- Очікувати від DC-аналізу часової форми: для фронтів і заряджання потрібен transient-аналіз.
- Вважати, що «цифрова» схема завжди потребує тільки DC: перемикання також має часові перехідні процеси.

## Sources

<!-- generated from frontmatter -->
