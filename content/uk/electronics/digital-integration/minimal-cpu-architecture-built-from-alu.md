---
id: emb-elinteg-0059
title: "Які функціональні вузли необхідно додати до АЛП для побудови мінімального повноцінного мікропроцесора?"
track: electronics
section: digital-integration
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
---

## Short answer

Для перетворення АЛП на процесор необхідні пам'ять команд і даних, лічильник команд (PC) для послідовної адресації та засувки для збереження операндів. Також потрібен автомат керування (FSM), який циклічно виконує вибірку команди, дешифрацію та запис результату назад у регістри чи пам'ять. На основі цих дискретних блоків логіки 74xx ентузіасти створюють повнофункціональні ретро-комп'ютери (наприклад, Magic-1).[^udemy-electronics-course]

## Detailed explanation

TODO
