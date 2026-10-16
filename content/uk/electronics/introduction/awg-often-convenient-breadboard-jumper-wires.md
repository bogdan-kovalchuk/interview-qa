---
id: emb-elintro-0289
title: "Який AWG часто зручний для breadboard jumper wires?"
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
  - source_id: busboard-breadboard-wire-gauge
    title: "What wire gauge should I use with a solderless breadboard?"
    url: https://busboard.com/faq/breadboard-wire-gauge
  - source_id: adafruit-breadboard-jumpers
    title: "Jumper Wires | Breadboards for Beginners"
    url: https://learn.adafruit.com/breadboards-for-beginners/diy-jumper-wires
---

## Short answer

Для безпаяних макетних плат часто зручний одножильний 22 AWG; виробник BusBoard також рекомендує суцільний провід у діапазоні 22–26 AWG. Вибір залежить від конкретних пружинних контактів: надто товстий провід може їх пошкодити, а надто тонкий – давати ненадійний контакт.[^busboard-breadboard-wire-gauge]

Точний припустимий калібр залежить від геометрії та стану контактів конкретної плати.[^busboard-breadboard-wire-gauge]

## Detailed explanation

AWG – це система, у якій менше число означає товстіший провід. Для багатьох безпаяних макетних плат практичний вибір – суцільний 22 AWG, бо він достатньо жорсткий для вставляння в пружинні контакти; виробник BusBoard вказує придатний діапазон 22–26 AWG.[^busboard-breadboard-wire-gauge]

Ключове слово тут – «суцільний». Гнучкий багатожильний провід без підготовленого штиря розпушується на кінці, тому окремі тонкі жили можуть не зайти в контактний затискач або торкнутися сусіднього ряду. Суцільний провід зберігає форму після згинання, що допомагає прокласти коротку перемичку акуратно й повторювано. Ізоляція має бути достатньо тонкою біля кінця, щоб оголена ділянка входила в контакт повністю, але не настільки довгою, щоб оголений провід створював ризик короткого замикання.[^adafruit-breadboard-jumpers]

Провід не варто силоміць утискати в отвори. Надто товстий сердечник може розтягнути або пошкодити пружинні контакти; надто тонкий може погано утримуватися й давати переривчасте з’єднання. Навіть одна макетна плата може мати контакти, що відрізняються за станом і силою затиску, тому рекомендація щодо калібру не замінює перевірку сумісності.[^busboard-breadboard-wire-gauge]

Приклад: якщо на платі контактні отвори приймають 22 AWG, відрізають шматок такого ізольованого суцільного дроту, знімають коротку ділянку ізоляції з обох кінців і вставляють металеві кінці в потрібні ряди. Для іншої плати, що допускає 24 або 26 AWG, тонший провід також буде доречним; універсального калібру для всіх макетних плат немає.[^busboard-breadboard-wire-gauge]

**Типова помилка:** сприймати 22 AWG як обов’язковий стандарт для кожної плати або брати багатожильний провід лише тому, що він зручний у прокладанні. Перевіряють рекомендований діапазон для контактів і використовують суцільний провід відповідної товщини.
