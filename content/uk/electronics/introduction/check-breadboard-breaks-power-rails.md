---
id: emb-elintro-0111
title: "Чому на breadboard треба перевіряти розриви в рейках живлення?"
description: "Чому на breadboard треба перевіряти розриви в рейках живлення?"
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
    applicability: "Походження питання: лекція 11, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: adafruit-breadboard-split-rails
    title: "Adafruit: Breadboards for Beginners"
    url: https://learn.adafruit.com/breadboards-for-beginners?view=all
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює, що рейки живлення деяких breadboard розірвані, та радить перевіряти неперервність мультиметром або маркуванням."
---

## Short answer

На деяких breadboard рейки живлення розділені на ізольовані відрізки, тому напруга, подана на один відрізок, не обов’язково з’явиться на іншому. Перевірте з’єднання за схемою плати або мультиметром і, якщо потрібна неперервна шина, з’єднайте сегменти перемичкою.[^adafruit-breadboard-split-rails]

## Detailed explanation

Рейки живлення на breadboard – це групи контактів, з’єднаних усередині плати, щоб розвести `VCC` і `GND` без окремого дроту до кожного вузла. Але таке з’єднання не гарантовано проходить по всій довжині: деякі плати мають розрив посередині, а в окремих моделей дві сусідні рейки також електрично ізольовані. Тому кольорова смуга є лише підказкою, а не доказом електричного контакту.[^adafruit-breadboard-split-rails]

Якщо джерело під’єднане до верхньої частини розірваної рейки, нижня частина може залишитися без живлення або «плавати» – її потенціал не визначений цим джерелом. У такому разі мікросхема чи датчик може не запускатися, а сигнал із входу бути нестабільним. Це схоже на помилку в схемі, хоча фактично бракує лише електричного з’єднання між сегментами.

Перед подачею живлення простежте, які отвори з’єднані всередині саме вашої плати. За вимкненого живлення перевірте мультиметром режимом продзвонювання контакт між точками, які вважаєте однією рейкою. Якщо контакту немає, додайте перемичку від одного сегмента до іншого; для довгих шин варто перевірити також падіння напруги під навантаженням. Не з’єднуйте навмання рейки `VCC` і `GND`: це створить коротке замикання.

Приклад: джерело `5 V` під’єднане до верхньої половини червоної рейки, а резистор світлодіода – до нижньої. Якщо рейка розірвана, нижня половина не отримує ці `5 V`, доки її не з’єднати перемичкою з верхньою половиною або безпосередньо з джерелом.[^adafruit-breadboard-split-rails]

**Типові помилки:**
- Вважати, що червона смуга означає суцільний провід на всю довжину.
- З’єднувати рейки лише за кольором, не перевіривши їхню фактичну топологію.
- Перевіряти продзвонюванням плату, яка ще під’єднана до джерела живлення.

## Sources

<!-- generated from frontmatter -->
