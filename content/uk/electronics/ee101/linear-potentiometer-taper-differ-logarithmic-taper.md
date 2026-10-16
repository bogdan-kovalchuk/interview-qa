---
id: emb-elee-0013
title: "Чим лінійний потенціометр відрізняється від логарифмічного?"
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
  - source_id: analog-devices-taper
    title: "Analog Devices: Taper"
    url: https://www.analog.com/en/resources/glossary/logarithmic_linear_taper.html
---

## Short answer

У лінійного потенціометра опір від wiper до кінця змінюється приблизно пропорційно переміщенню контакту; у логарифмічного ця залежність нелінійна. Точна крива, її напрямок і маркування A/B залежать від виробника та регіональної конвенції, тому їх перевіряють у даташиті конкретної моделі.[^analog-devices-taper]

## Detailed explanation

Taper описує залежність опору між wiper і кінцем резистивної доріжки від положення рухомого контакту. У лінійного потенціометра зміна опору приблизно пропорційна переміщенню: у середині механічного ходу буде близько половини повного опору. Це зручно, коли положення ручки має прямо відповідати частці керувального сигналу, наприклад у простому voltage divider.[^analog-devices-taper]

У логарифмічного потенціометра опір змінюється за нелінійною кривою. Для audio taper зміна на початку ходу зазвичай повільніша, а ближче до кінця – швидша, щоб регулювання гучності відчувалося плавніше. Реальна крива часто є наближенням, а не математично точним логарифмом; однакові позначки номіналу не гарантують однакового taper у різних виробників.[^analog-devices-taper]

Наприклад, для лінійного потенціометра 10 kΩ приблизно 50% ходу дає близько 5 kΩ від wiper до одного краю без навантаження. Для аудіо taper таке твердження неправильне: середнє положення не обов’язково відповідає половині опору чи половині напруги. Зовнішнє навантаження також змінює вихідну характеристику обох типів.[^analog-devices-taper]

Маркування не є універсальним для всіх ринків і серій: літера A або B може мати різне значення у різних виробників. Перед заміною компонента потрібно звірити опис taper у документації, а не покладатися лише на літеру або назву в магазині.[^analog-devices-taper]

**Типова помилка:** переносити правило «B – linear, A – log» на будь-який компонент та вважати, що log taper завжди має точну криву. Спершу визначають фактичну характеристику з даташита й перевіряють, чи відповідає вона функції схеми.
