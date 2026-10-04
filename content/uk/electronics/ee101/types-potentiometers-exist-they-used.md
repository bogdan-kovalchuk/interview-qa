---
id: emb-elee-0017
title: "Які типи потенціометрів бувають і де їх застосовують?"
description: "Які типи потенціометрів бувають і де їх застосовують?"
track: electronics
section: ee101
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
    applicability: "Походження питання: лекція 34, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-potentiometer-types
    title: "All About Circuits: Voltage Divider Circuits"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-6/voltage-divider-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Описує wiper і механічні rotary, linear та trimmer конструкції; не є повною класифікацією всіх промислових варіантів."
  - source_id: ad-max5481
    title: "Analog Devices: MAX5481 product page"
    url: https://www.analog.com/en/products/max5481.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Конкретне сімейство цифрових потенціометрів має SPI-compatible та up/down інтерфейс; це приклад, не універсальна властивість усіх цифрових потенціометрів."
  - source_id: microchip-mcp4018
    title: "Microchip: MCP4018 product page"
    url: https://www.microchip.com/en-us/product/mcp4018
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Підтверджує, що конкретна модель MCP4018 є цифровим потенціометром з I2C; інші моделі можуть мати інші інтерфейси."
---

## Short answer

Механічні потенціометри бувають роторні, повзункові та підлаштувальні (trimmer); цифровий потенціометр змінює положення електронно. Застосування й доступний інтерфейс залежать від конструкції та моделі: наприклад, конкретні цифрові мікросхеми використовують SPI або I²C.[^aac-potentiometer-types] [^ad-max5481] [^microchip-mcp4018]

## Detailed explanation

Потенціометр містить резистивну доріжку та рухомий контакт – wiper, тому може працювати як регульований дільник напруги. Назви «роторний» і «повзунковий» описують спосіб механічного руху: в першому wiper рухається обертанням вала, у другому – прямолінійним переміщенням повзунка. Роторний регулятор зручний для ручок гучності чи налаштування; повзунковий дає наочне лінійне керування, тому трапляється в мікшерах. Це приклади типового використання, а не обмеження призначення компонента.[^aac-potentiometer-types]

Trimmer – невеликий потенціометр для підлаштування параметра під час калібрування або обслуговування, часто за допомогою викрутки. Існують одно- й багатоколові варіанти: багатоколовий забезпечує точніше налаштування на малому діапазоні, але потребує більше обертів. Не плутайте тип механізму з законом зміни опору: «лінійний» також називає taper, тобто залежність опору від положення. Лінійний taper приблизно пропорційний ходу, а аудіо-регулятор може мати логарифмічний taper, щоб суб’єктивна гучність змінювалася зручніше.[^aac-potentiometer-types]

Цифровий потенціометр – інтегральна схема, яка задає еквівалентне положення wiper дискретними кроками за командою контролера. Вона корисна для автоматичного або дистанційного налаштування, збереження повторюваних параметрів і калібрування без механічного доступу. Інтерфейс не можна узагальнювати: MAX5481 має SPI-compatible та up/down режими, тоді як MCP4018 використовує I²C. Перед вибором перевіряйте число кроків, діапазон напруги на виводах, допустимий струм, опір wiper, енергонезалежність і протокол саме в документації моделі.[^ad-max5481] [^microchip-mcp4018]

Приклад вибору: для ручного рівня сигналу на панелі доречний роторний компонент із потрібним опором і taper; для налаштування коефіцієнта підсилення під час виробництва – trimmer; для повторюваного налаштування програмою – цифрова модель. У кожному випадку також перевіряють потужність, точність, ресурс контактів і граничні умови сигналу: цифрові мікросхеми часто не можна використовувати як силовий реостат або подавати на їхні виводи напругу поза межами живлення.[^aac-potentiometer-types] [^ad-max5481]

**Типова помилка:** вважати, що кожен потенціометр має поворот на фіксовані 270–300° або що будь-який цифровий варіант спілкується і через SPI, і через I²C. Геометрію механічної моделі та функції цифрової мікросхеми визначає її datasheet; обирайте деталь за конкретними вимогами, а не лише за загальною назвою типу.[^aac-potentiometer-types] [^ad-max5481] [^microchip-mcp4018]

## Sources

<!-- generated from frontmatter -->
