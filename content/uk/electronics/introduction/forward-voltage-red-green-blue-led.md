---
id: emb-elintro-0114
title: "Яка пряма напруга `V_f` у червоного, зеленого й синього `LED`?"
description: "Яка пряма напруга V_f у червоного, зеленого й синього LED?"
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
    applicability: "Походження питання: лекція 12, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: digikey-rgb-led-forward-voltage
    title: "DigiKey: RGB LEDs Provide Multicolor Display Solutions"
    url: https://www.digikey.com/en/articles/how-to-drive-multicolor-leds
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Наводить типові прямі напруги RGB-світлодіода Adafruit 2739 за конкретного струму; значення не є універсальними для всіх кольорів і моделей."
---

## Short answer

Типове `V_f` залежить від моделі та струму. Наприклад, для RGB LED Adafruit 2739 при `20 mA` наведено приблизно `2.0 V` для червоного та `3.2 V` для зеленого й синього каналів; це значення конкретного виробу, а не універсальна таблиця кольорів.[^digikey-rgb-led-forward-voltage]

## Detailed explanation

Пряма напруга `V_f` – це напруга на світлодіоді за заданого прямого струму. У червоних LED вона часто нижча, ніж у синіх, бо напівпровідникові матеріали для різних довжин хвиль мають різну ширину забороненої зони. Однак колір сам по собі не задає точне значення: важливі матеріал, конструкція, струм і температура, тому для конкретного компонента потрібно дивитися його datasheet.[^digikey-rgb-led-forward-voltage]

Таблиці з приблизними діапазонами корисні лише для оцінки. Навіть значення з однієї специфікації прив’язане до певного тестового струму: у прикладі RGB LED Adafruit 2739 стаття наводить для червоного каналу `2.0 V` при `20 mA`, а для зеленого й синього – `3.2 V`; при `15 mA` для цих каналів вказані вже `1.9 V` і `3.1 V`. Не слід сприймати це як гарантовані межі для будь-якого світлодіода такого кольору.[^digikey-rgb-led-forward-voltage]

`V_f` потрібна, зокрема, для оцінки опору послідовного резистора: джерело живлення має забезпечити падіння напруги і на LED, і на резисторі. Якщо в багатоколірному компоненті є окремі кристали, для кожного каналу використовують його власну характеристику. Заміна червоного LED на синій без повторного розрахунку може змінити струм і яскравість.[^digikey-rgb-led-forward-voltage]

Приклад: якщо datasheet конкретного червоного LED задає типове `V_f = 2.0 V` при `20 mA`, саме це значення можна використати як початкову оцінку для цього струму; для гарантованого розрахунку перевіряють межі у специфікації.

**Типові помилки:**
- Вважати наведені для кольору діапазони точними гарантованими межами.
- Ігнорувати тестовий струм, за якого виробник виміряв `V_f`.
- Вважати, що всі зелені LED мають однакову пряму напругу.

## Sources

<!-- generated from frontmatter -->
