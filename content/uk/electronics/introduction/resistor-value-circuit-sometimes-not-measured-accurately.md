---
id: emb-elintro-0276
title: "Чому опір резистора в схемі іноді не можна точно виміряти мультиметром?"
description: "Чому опір резистора в схемі іноді не можна точно виміряти мультиметром?"
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
    applicability: "Походження питання: лекція 24, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: fluke-in-circuit-resistance
    title: "Fluke: How to Measure Resistance with a Digital Multimeter"
    url: https://www.fluke.com/en-us/learn/blog/digital-multimeters/how-to-measure-resistance
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює вимірювання опору, паралельні шляхи між щупами та потребу підняти вивід для ізольованого вимірювання; точність залежить від мультиметра й кола."
---

## Short answer

Паралельні шляхи на платі впливають на вимірювання, тому мультиметр може показати еквівалентний опір між щупами, а не номінал окремого резистора. Для точного вимірювання часто треба випаяти один вивід або ізолювати елемент від решти схеми.[^fluke-in-circuit-resistance]

## Detailed explanation

Опір резистора в зібраному колі не завжди можна визначити безпосередньо, бо омметр вимірює еквівалентний опір усіх шляхів між щупами.[^fluke-in-circuit-resistance]

У режимі вимірювання опору мультиметр подає невеликий тестовий струм і за виміряною напругою оцінює опір. Якщо паралельно резистору підключений інший резистор, вимірювальний струм ділиться між гілками. Наприклад, два резистори по `10 kΩ`, підключені паралельно, мають еквівалент `5 kΩ`; при вимірюванні на платі прилад побачить цей нижчий шлях замість `10 kΩ` одного компонента.[^fluke-in-circuit-resistance]

Складніша схема може містити діоди, транзистори, конденсатори та інші елементи. Тестова напруга мультиметра іноді відкриває напівпровідниковий перехід, тож показ може залежати від полярності щупів, діапазону та стану решти кола. Це не обов’язково означає несправність резистора. Перед вимірюванням вимкніть живлення та розрядіть конденсатори, інакше можна пошкодити прилад або отримати хибне значення.[^fluke-in-circuit-resistance]

Якщо треба перевірити саме резистор, звіртеся зі схемою та ізолюйте щонайменше один його вивід від плати. Після цього виміряйте опір і порівняйте з номіналом, зважаючи на допуск компонента. Не плутайте вимірювання опору в схемі з режимом continuity: звуковий сигнал повідомляє лише, що опір нижчий за поріг конкретного мультиметра, а не підтверджує заданий номінал.[^fluke-in-circuit-resistance]

## Sources

<!-- generated from frontmatter -->
