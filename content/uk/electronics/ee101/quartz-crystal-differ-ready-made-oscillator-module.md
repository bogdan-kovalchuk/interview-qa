---
id: emb-elee-0245
title: "Чим кварцовий резонатор відрізняється від готового генераторного модуля (oscillator)?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: ti-sn74lvc1gx04-oscillator
    title: "Texas Instruments: datasheet SN74LVC1GX04 (SCES581D), розділ 9 Application and Implementation"
    url: https://www.ti.com/lit/ds/symlink/sn74lvc1gx04.pdf
  - source_id: abracon-quartz-glossary
    title: "Abracon: Quartz Crystal Oscillators Glossary of Terms (глосарій кварцових генераторів)"
    url: https://abracon.com/Support/qtzcryoscil_glossary.pdf
---

## Short answer

Кварцовий резонатор задає частоту, але для коливань потрібен підсилювач із зворотним зв’язком, наприклад інвертор у схемі Пірса.[^ti-sn74lvc1gx04-oscillator] Готовий генераторний модуль (oscillator) зазвичай видає тактовий сигнал логічного рівня (наприклад TTL або HCMOS); є й синусові виходи.[^abracon-quartz-glossary] Вивід enable, якщо він є, задає стан виходу: заземлений вхід переводить його у стан високого імпедансу.[^abracon-quartz-glossary]

## Detailed explanation

Кварцовий резонатор – це частотозадавальний елемент: він визначає, на якій частоті може відбуватися коливання, але сам по собі не дає логічного тактового сигналу. Коливання створює схема навколо резонатора, а не сам резонатор. У прикладі TI для генератора Пірса інвертор підсилює сигнал, резистор R_F зміщує інвертор у лінійну область роботи, а значення C1 і C2 обирають так, щоб із них обчислити навантаження кварца C_L.[^ti-sn74lvc1gx04-oscillator]

Готовий генераторний модуль (oscillator) є закритим блоком: кварц і схема генератора вже з’єднані в корпусі, а назовні виведено живлення, землю, вихід і, у багатьох модулях, вивід enable. Вихід виробник описує як такий, що відповідає заявленим логічним станам, наприклад TTL або HCMOS; є й синусові виходи.[^abracon-quartz-glossary] Тому розробник не підбирає C1, C2 і R_F, а частоту, рівень і вихідну логіку бере з специфікації модуля.

Вивід enable належить до параметрів, які треба перевіряти в datasheet, бо його наявність і полярність залежать від конкретного виробу. В описі Abracon заземлений вхід переводить вихід у стан високого імпедансу, а вхід, залишений відкритим або з логічною одиницею, дає нормальну генерацію.[^abracon-quartz-glossary] Це визначення одного виробника, тому його не можна переносити на інші модулі без перевірки.

Вибір між окремим кварцом і модулем зводиться до того, хто відповідає за схему генератора. З окремим кварцом це розробник: він вибирає інвертор, навантаження і зворотний зв’язок та перевіряє запуск на найнижчій напрузі живлення.[^ti-sn74lvc1gx04-oscillator] У модулі ці рішення закладає виробник, а розробник отримує готовий тактовий вихід.

**Типові помилки:**

- Вважати, що кварцовий резонатор сам видає логічний тактовий сигнал без схеми з інвертором.
- Підключати enable модуля без перевірки його полярності: у Abracon заземлений вхід переводить вихід у стан високого імпедансу.[^abracon-quartz-glossary]
- Переносити логіку enable з одного модуля на інший, навіть коли назва виводу однакова.
