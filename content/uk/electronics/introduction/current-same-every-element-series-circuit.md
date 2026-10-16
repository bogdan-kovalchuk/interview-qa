---
id: emb-elintro-0103
title: "Чому струм однаковий у всіх елементах послідовного кола?"
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
  - source_id: aac-series-circuits
    title: "All About Circuits: Series Circuits and the Application of Ohm’s Law"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-5/simple-series-circuits/
---

## Short answer

У послідовному колі струм однаковий у кожному елементі, бо між ними є лише один шлях для руху заряду. За законом збереження заряду заряд не накопичується в проміжних вузлах у сталому режимі, тому за однаковий час через кожен елемент проходить однакова кількість заряду.[^aac-series-circuits]

## Detailed explanation

Послідовним називають з’єднання, у якому елементи утворюють один неперервний шлях без розгалужень. Струм показує, скільки заряду проходить через переріз провідника за одиницю часу. Якби через один елемент надходило більше заряду, ніж виходило до наступного, заряд накопичувався б на з’єднанні; у сталому режимі цього не відбувається. Тому струм перед і після кожного елемента однаковий, хоча напруга на елементах може відрізнятися.[^aac-series-circuits]

Це також видно із закону Кірхгофа для струмів: у вузлі алгебраїчна сума струмів дорівнює нулю. Для вузла послідовного кола, до якого входить один елемент і виходить інший, струм, що входить, мусить дорівнювати струму, що виходить. Повторивши це для кожного з’єднання, отримуємо однаковий струм у всьому колі. Правило стосується будь-яких компонентів, з’єднаних послідовно, а не лише резисторів.[^aac-series-circuits]

**Типові помилки:**
- Однаковий струм не означає однакову напругу. На резисторах із різними опорами падіння відрізняються відповідно до закону Ома.
- Якщо в колі є вузол, де струм може розділитися на гілки, усе коло вже не є одним послідовним шляхом. Струми гілок можуть відрізнятися, а їхня сума дорівнює струму до розгалуження.
- Перевіряйте з’єднання за схемою, а не лише за розташуванням компонентів на макетній платі: внутрішні контакти можуть створити паралельні гілки або коротке замикання.[^aac-series-circuits]
