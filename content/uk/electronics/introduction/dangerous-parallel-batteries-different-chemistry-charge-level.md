---
id: emb-elintro-0060
title: "Чому небезпечно з'єднувати паралельно батареї різної хімії або з різним рівнем заряду?"
description: "Чому небезпечно з'єднувати паралельно батареї різної хімії або з різним рівнем заряду?"
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
    applicability: "Походження питання: лекція 7, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: energizer-alkaline-faq
    title: "Energizer: Alkaline Batteries FAQ"
    url: https://data.energizer.com/pdfs/alkaline_faq.pdf
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Наслідки змішування батарей різної хімії, віку або стану в пристрої з послідовним живленням; не є інструкцією для проєктування паралельних акумуляторних збірок."
  - source_id: libretexts-battery-networks
    title: "Physics LibreTexts: Networks of Batteries and Resistors"
    url: "https://phys.libretexts.org/Courses/University_of_California_Davis/UCD:_Physics_9C__Electricity_and_Magnetism/3:_Direct_Current_Circuits/3.3:_Networks_of_Batteries_and_Resistors"
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Модель джерела з внутрішнім опором і струму в колі; ілюструє, чому різниця напруги разом з опорами задає струм."
---

## Short answer

За прямого паралельного з’єднання батарей із різною напругою виникає струм між ними, величина якого залежить від різниці напруг і сумарного опору кола. Змішувати батареї різної хімії чи стану без спеціально спроєктованого керування небезпечно: можливі надмірний струм, нагрівання, пошкодження або витік.[^libretexts-battery-networks] [^energizer-alkaline-faq]

## Detailed explanation

Небезпека прямого паралельного з’єднання полягає в тому, що обидва джерела опиняються на спільних клемах. Якщо їхні напруги різні, різниця потенціалів створює струм між батареями. У простій моделі він визначається цією різницею та сумою внутрішніх опорів і опорів з’єднань; малий сумарний опір може дати великий струм навіть без зовнішнього навантаження.[^libretexts-battery-networks]

Рівень заряду впливає на напругу, але відповідність напруги в один момент не доводить сумісність: різні хімічні системи мають різні робочі межі та вимоги до заряджання. Надмірний струм може нагріти елементи й проводи. Для літієвих акумуляторів неправильний режим може спричинити небезпечний стан, тому потрібна конфігурація, захист і керування, визначені виробником; не можна вважати, що внутрішній опір сам по собі є достатнім захистом.[^libretexts-battery-networks]

Попередження виробників про змішування нових і використаних батарей чи різних хімічних типів стосуються також звичайних пристроїв із кількома елементами: слабший елемент може бути надмірно розряджений сильнішими, що підвищує ризик витоку. Це окремий механізм від вирівнювального струму при прямому паралельному з’єднанні, але висновок практичний той самий – використовуйте лише передбачені виробником сумісні елементи.[^energizer-alkaline-faq]

**Типова помилка:** вважати, що паралельні батареї безпечні, якщо на етикетках однакова номінальна напруга. Перед з’єднанням потрібні однакова сумісна хімія, близький стан і дозволена виробником схема з належним захистом.

## Sources

<!-- generated from frontmatter -->
