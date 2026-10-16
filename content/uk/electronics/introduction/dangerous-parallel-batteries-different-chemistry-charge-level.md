---
id: emb-elintro-0060
title: "Чому небезпечно з'єднувати паралельно батареї різної хімії або з різним рівнем заряду?"
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
  - source_id: energizer-alkaline-faq
    title: "Energizer: Alkaline Batteries FAQ"
    url: https://data.energizer.com/pdfs/alkaline_faq.pdf
  - source_id: libretexts-battery-networks
    title: "Physics LibreTexts: Networks of Batteries and Resistors"
    url: https://phys.libretexts.org/Courses/University_of_California_Davis/UCD:_Physics_9C__Electricity_and_Magnetism/3:_Direct_Current_Circuits/3.3:_Networks_of_Batteries_and_Resistors
---

## Short answer

За прямого паралельного з’єднання батарей із різною напругою виникає струм між ними, величина якого залежить від різниці напруг і сумарного опору кола. Змішувати батареї різної хімії чи стану без спеціально спроєктованого керування небезпечно: можливі надмірний струм, нагрівання, пошкодження або витік.[^libretexts-battery-networks] [^energizer-alkaline-faq]

## Detailed explanation

Небезпека прямого паралельного з’єднання полягає в тому, що обидва джерела опиняються на спільних клемах. Якщо їхні напруги різні, різниця потенціалів створює струм між батареями. У простій моделі він визначається цією різницею та сумою внутрішніх опорів і опорів з’єднань; малий сумарний опір може дати великий струм навіть без зовнішнього навантаження.[^libretexts-battery-networks]

Рівень заряду впливає на напругу, але відповідність напруги в один момент не доводить сумісність: різні хімічні системи мають різні робочі межі та вимоги до заряджання. Надмірний струм може нагріти елементи й проводи. Для літієвих акумуляторів неправильний режим може спричинити небезпечний стан, тому потрібна конфігурація, захист і керування, визначені виробником; не можна вважати, що внутрішній опір сам по собі є достатнім захистом.[^libretexts-battery-networks]

Попередження виробників про змішування нових і використаних батарей чи різних хімічних типів стосуються також звичайних пристроїв із кількома елементами: слабший елемент може бути надмірно розряджений сильнішими, що підвищує ризик витоку. Це окремий механізм від вирівнювального струму при прямому паралельному з’єднанні, але висновок практичний той самий – використовуйте лише передбачені виробником сумісні елементи.[^energizer-alkaline-faq]

**Типова помилка:** вважати, що паралельні батареї безпечні, якщо на етикетках однакова номінальна напруга. Перед з’єднанням потрібні однакова сумісна хімія, близький стан і дозволена виробником схема з належним захистом.
