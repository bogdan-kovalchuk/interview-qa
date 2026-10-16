---
id: emb-elee-0187
title: "Як позначаються виводи біполярного транзистора і як тече струм у NPN?"
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
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor
---

## Short answer

База B, колектор C, емітер E. У NPN в активному режимі струм входить у колектор і базу та виходить з емітера; у PNP полярності й напрямки протилежні. Стрілка на емітері: у NPN – назовні, у PNP – до бази.[^fiore-bjt-basics]

## Detailed explanation

Три виводи біполярного транзистора називають за шарами, з якими вони контактують. Емітер (E) інжектує носії в базу, база (B) – тонкий слабко легований середній шар, колектор (C) – найбільший шар, який збирає більшість носіїв. У NPN шари йдуть у порядку N–P–N: емітер і колектор є N-областями, база – P-областю. У PNP порядок P–N–P, тому полярності живлення й напрямки струмів протилежні. Емітер і колектор не взаємозамінні: колектор – найбільша область, база – тонка й слабко легована.[^fiore-bjt-basics] Транзистор, увімкнений навпаки, зазвичай усе ще працює, але з набагато меншим β, тому параметри з datasheet не виконуються.

У NPN при прямому зміщенні B–E електрони з емітера входять у базу. Оскільки база тонка й слабко легована, лише невеликий відсоток електронів рекомбінує з дірками бази; понад 95 % доходить до колектора й тече до плюса живлення колектора. Звичайний струм тече у протилежний бік: входить у колектор і базу та виходить з емітера. Закон Кірхгофа для вузла дає I_E = I_C + I_B, а через малий I_B маємо I_E ≈ I_C. Приклад: при I_B = 0,02 мА і I_C = 2 мА отримуємо I_E = 2,02 мА.[^fiore-bjt-basics]

Стрілка на символі показує напрямок звичайного струму через емітер: у NPN вона вказує назовні, у PNP – на базу. За символом одразу видно і тип транзистора, і напрямок струму через емітер: у NPN він виходить, у PNP входить.[^fiore-bjt-basics]

**Типові помилки:**
- Плутати звичайний струм із рухом електронів: вони течуть у протилежний бік, тож у NPN електрони надходять в емітер від його джерела живлення.[^fiore-bjt-basics]
- Вважати емітер і колектор взаємозамінними лише тому, що обидва – N-області: вони фізично не ідентичні.[^fiore-bjt-basics]
