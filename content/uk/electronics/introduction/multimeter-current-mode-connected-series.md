---
id: emb-elintro-0265
title: "Чому мультиметр у режимі струму треба підключати послідовно?"
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
  - source_id: fluke-current-measurement-fuses
    title: "Fluke: Choosing the correct fuse for your tester"
    url: https://www.fluke.com/en-us/learn/blog/digital-multimeters/choosing-the-correct-fuse-for-your-tester
---

## Short answer

У режимі струму мультиметр вмикають послідовно: коло розмикають, а струм навантаження пропускають через вимірювальний вхід приладу.[^fluke-current-measurement-fuses] Цей вхід має малий опір, тому паралельне підключення до джерела може спричинити надмірний струм і пошкодити прилад або запобіжник.

## Detailed explanation

Амперметр вимірює струм, пропускаючи його через внутрішній шунт із малим опором. Щоб виміряти струм навантаження, потрібно розімкнути відповідну гілку й вставити прилад у цей розрив; тоді через мультиметр і навантаження проходить той самий струм. Саме тому послідовне з’єднання є правильним способом вимірювання.[^fluke-current-measurement-fuses]

У режимі напруги мультиметр зазвичай має великий вхідний опір і під’єднується паралельно. Перенесення цього способу на струмовий режим небезпечне: низькоомний шунт опиниться майже безпосередньо між клемами джерела й пропустить струм, обмежений переважно джерелом, проводами та внутрішнім опором приладу. Такий струм може перевищити номінал запобіжника або пошкодити обладнання.[^fluke-current-measurement-fuses]

Приклад: щоб виміряти струм лампи, вимкніть живлення, роз’єднайте один провід між джерелом і лампою, а мультиметр вставте в розрив, вибравши правильне струмове гніздо та діапазон. Перевірте, що очікуваний струм нижчий за межу входу й запобіжника приладу; після вимірювання поверніть провід у гніздо напруги перед наступною перевіркою напруги. Для струму, більшого за допустимий для мультиметра, потрібен відповідний струмовий затискач або інший метод, а не паралельне підключення.[^fluke-current-measurement-fuses]

Типова помилка – виміряти напругу, а потім не переставити червоний провід із гнізда `A` або `mA` до гнізда `V` перед наступним вимірюванням. У такій конфігурації торкання щупами двох точок кола може створити короткий шлях через шунт. Тому перевіряйте і режим перемикача, і гніздо проводу до підключення, а не лише значок на дисплеї.[^fluke-current-measurement-fuses]
