---
id: emb-elintro-0038
title: "Атомний номер і атомна маса – чим вони відрізняються?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: openstax-atomic-structure
    title: "OpenStax Chemistry 2e, 2.3 Atomic Structure and Symbolism"
    url: https://openstax.org/books/chemistry/pages/2-3-atomic-structure-and-symbolism
---

## Short answer

Атомний номер `Z` дорівнює кількості протонів у ядрі й визначає хімічний елемент; масове число `A` дорівнює сумі протонів і нейтронів.[^openstax-atomic-structure] Для нейтрального атома число електронів також дорівнює `Z`, але іон може мати іншу кількість електронів. У кремнію `Z = 14`, а найпоширеніший ізотоп має `A = 28`.[^openstax-atomic-structure]

## Detailed explanation

Атомний номер `Z` – це кількість протонів у ядрі; саме вона визначає, до якого хімічного елемента належить атом.[^openstax-atomic-structure] Масове число `A` – ціле число нуклонів у ядрі: протонів плюс нейтронів. Отже, кількість нейтронів можна знайти як `A - Z`.[^openstax-atomic-structure]

Не слід плутати масове число із середньою атомною масою елемента в періодичній таблиці. Масове число описує конкретний ізотоп, тоді як атомна маса природного елемента є зваженим середнім мас ізотопів; ізотопи одного елемента мають однакове `Z`, але різні числа нейтронів.[^openstax-atomic-structure]

Приклад: у найпоширенішого ізотопу кремнію-28 `Z = 14` і `A = 28`, отже, ядро містить 14 протонів і 14 нейтронів. Нейтральний атом цього ізотопу також має 14 електронів; для йона це останнє твердження вже не обов’язково правильне.

Отже, щоб знайти число нейтронів конкретного ізотопу, від масового числа віднімають атомний номер: `N = A - Z`. Наприклад, ізотопи кремнію-29 і кремнію-30 мають ті самі 14 протонів, але відповідно 15 і 16 нейтронів. Вони залишаються атомами того самого елемента, бо його хімічну тотожність задає саме заряд ядра, тобто число протонів.[^openstax-atomic-structure]
