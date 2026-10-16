---
id: emb-elintro-0256
title: "Що означає корпус SOT-6 з кількома drain-виводами?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: onsemi-fds4685
    title: "onsemi FDS4685 datasheet"
    url: https://www.onsemi.com/download/data-sheet/pdf/fds4685-d.pdf
  - source_id: infineon-mosfet-layout
    title: "Infineon: Designing with power MOSFETs"
    url: https://www.infineon.com/assets/row/public/documents/24/42/infineon-designing-with-power-mosfets-applicationnotes-en.pdf?fileId=8ac78c8c7ddc01d7017e6c619a490f47
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Кілька виводів drain у конкретному MOSFET можуть бути з’єднані з одним drain вузлом і забезпечувати паралельні електричні та теплові шляхи; pinout треба підтвердити за datasheet саме цієї деталі.[^onsemi-fds4685] Їх не можна автоматично вважати кількома транзисторами або гарантією більшого допустимого струму: його обмежують кристал, корпус, плата й температура.[^infineon-mosfet-layout]

## Detailed explanation

Кілька drain-виводів на корпусі MOSFET зазвичай є зовнішніми контактами одного drain-вузла, але це потрібно перевіряти за pinout та еквівалентною схемою в datasheet конкретної деталі. Наприклад, datasheet FDS4685 показує чотири контакти D для одного P-channel MOSFET у SO-8; цей приклад підтверджує спосіб читання документації, а не універсальний pinout для всіх SOT-6 деталей.[^onsemi-fds4685]

Поділ одного електрода на кілька ніжок дає змогу з’єднати його з більшою площею міді та зменшити обмеження, пов’язані з окремим контактом. У силовому корпусі drain може бути також пов’язаний із металевою тепловою площадкою, а відведення тепла залежить від корпусу, припою, міді плати й теплових переходів. Тому сам факт кількох ніжок не задає ні опір шляху, ні струмовий рейтинг, ні температуру кристала: їх визначає datasheet за конкретних умов монтажу й охолодження.[^infineon-mosfet-layout]

Перед трасуванням знайдіть таблицю виводів та малюнок корпусу, перевірте орієнтацію pin 1 і встановіть, чи контакти справді об’єднані всередині. Якщо datasheet позначає їх однаковою функцією, у footprint кожен фізичний pin треба прив’язати до відповідного електричного net. Перевірте і тепловий layout, бо паспортний струм може передбачати велику мідну площу або задану температуру корпусу.[^onsemi-fds4685] [^infineon-mosfet-layout]

**Типові помилки:**

- Вважати назву корпусу достатньою для висновку про pinout. Pin numbering і внутрішні з’єднання залежать від конкретної деталі.
- Думати, що паралельні виводи автоматично дозволяють подвоїти струм. Межі кристала й тепловідведення залишаються чинними.
- Підключити контакт за схожим footprint, не перевіривши pin 1 та вид зверху у datasheet.
