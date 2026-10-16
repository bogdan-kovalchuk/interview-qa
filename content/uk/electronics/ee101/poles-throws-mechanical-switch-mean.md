---
id: emb-elee-0004
title: "Що означають полюси (poles) і напрямки (throws) механічного перемикача?"
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
  - source_id: te-switch-poles-throws
    title: "TE Connectivity: Understanding Switch Pole and Switch Throw"
    url: https://www.te.com/en/products/switches/intersection/global-switch-attributes.html
---

## Short answer

Полюс описує окреме коло або спільний контакт перемикача, а напрямок (throw) – кількість контактів, між якими цей полюс перемикає з’єднання. Наприклад, SPDT має один полюс і два вибрані вихідні контакти; позначення не задає саме по собі моментну поведінку чи схему контактів конкретної деталі.[^te-switch-poles-throws]

## Detailed explanation

Полюси й напрямки – це два параметри контактної конфігурації перемикача. Полюс (pole) відповідає кількості окремих кіл або спільних контактів, якими керує механізм. Напрямок (throw) означає, до скількох контактних шляхів може перемкнутися кожен полюс. Ця нотація допомагає зрозуміти базову топологію, але не описує всі електричні характеристики деталі.[^te-switch-poles-throws]

У SPST один полюс комутує один шлях: типовий приклад – просте вмикання або розмикання кола. У SPDT один спільний контакт переходить між двома іншими контактами, тож ним можна вибрати один із двох шляхів. У DPDT є два полюси, кожен із двома напрямками; одна дія перемикача керує обома полюсами одночасно. Тому «два полюси» не означає два незалежні органи керування: їх може з’єднувати спільний механічний привод.[^te-switch-poles-throws]

**Приклад читання позначення:**

Якщо на схемі вказано `SPDT`, визначте common контакт і два альтернативні контакти, а потім за символом з’ясуйте, який контакт замкнений у кожному положенні. Сам напис `SPDT` не встановлює, чи є третє центральне положення, чи перемикач momentary або latching, а також чи є перехід break-before-make чи make-before-break. Ці властивості потрібно перевірити за схемою контактів і datasheet конкретного виробу.[^te-switch-poles-throws]

Не плутайте кількість механічних положень руків’я з кількістю poles: це різні властивості. Так само pole не завжди означає окреме незалежно кероване навантаження; у багатополюсному перемикачі контакти часто перемикаються разом. Для підключення реального перемикача орієнтуйтеся на його розводку контактів, а не лише на загальне скорочення.[^te-switch-poles-throws]
