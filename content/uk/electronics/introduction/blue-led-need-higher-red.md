---
id: emb-elintro-0166
title: "Чому синій `LED` потребує більшої `V_f`, ніж червоний?"
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
  - source_id: aac-leds
    title: "All About Circuits: Light Emitting Diodes"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-7/light-emitting-diodes-leds/
---

## Short answer

Енергія фотона пропорційна частоті: `E = h*f`. Синє світло має вищу частоту, тому відповідний напівпровідник має більшу band gap, ніж червоний; зазвичай це пов’язано з більшою `V_f`.[^aac-leds] Точне значення залежить від матеріалу, струму й температури.

## Detailed explanation

Пряма напруга `V_f` у LED пов’язана з енергією, яку вивільняють носії заряду під час рекомбінації в активній області. Різниця енергій між станами в зонній структурі матеріалу визначає характерну енергію фотона; частота світла пов’язана з нею співвідношенням `E = h*f`. Тому матеріали, що випромінюють синє світло, зазвичай мають більшу band gap, ніж матеріали червоних LED, і потребують більшої прямої напруги.[^aac-leds]

Це якісна залежність, а не спосіб точно визначити `V_f` лише за кольором. Напруга залежить також від складу напівпровідника, конструкції кристала, струму та температури; для розрахунку схеми слід користуватися графіком `I-V` або таблицею виробника для конкретного LED. Значення в даташиті зазвичай наведене для заданого тестового струму, а не є універсальною сталою.[^aac-leds]

У колі LED струм обмежують резистором або драйвером: джерело не повинно подавати необмежений струм лише тому, що діод має певний `V_f`. Для послідовного резистора оцінку роблять за `R = (V_supply - V_f)/I`; якщо `V_f` істотно зміниться, зміниться і струм. Це особливо важливо при зміні температури або використанні кількох LED послідовно.[^aac-leds]

Приклад: якщо для червоного LED в заданому режимі типовий `V_f` нижчий, ніж для синього, то за однакових джерела й резистора на синьому LED залишиться менша напруга на резисторі, отже струм буде меншим. Поширена помилка – сприймати колір як точну специфікацію напруги; колір лише підказує порядок величини, а проєктне значення беруть із даташиту конкретної деталі.[^aac-leds]
