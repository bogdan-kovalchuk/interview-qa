---
id: emb-elintro-0211
title: "Чому `V_CE` насиченого транзистора не дорівнює нулю?"
track: electronics
section: introduction
sources:
  - source_id: aac-bjt-saturation
    title: "All About Circuits: Transistor Ratings and Packages (BJT)"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/transistor-ratings-packages-bjt/
  - source_id: aac-bjt-active-mode
    title: "All About Circuits: Active-mode Operation (BJT)"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/active-mode-operation-bjt/
  - source_id: aac-bjt-beta-terms
    title: "All About Circuits: What Is BJT Beta? Understanding the Current Gain of a Bipolar Junction Transistor"
    url: https://www.allaboutcircuits.com/technical-articles/all-about-bjt-beta-understanding-terminology/
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

**Насичення не означає нульовий спад напруги.** Реальний BJT має ненульове `V_CE(sat)`, значення якого залежить від компонента, `I_C` і базового струму; діапазон 0.1–0.2 V не є універсальною гарантією. Більший базовий струм зазвичай зменшує спад у межах режиму й безпечних значень з документації.[^aac-bjt-saturation]

## Detailed explanation

Насичений біполярний транзистор проводить струм із ненульовим падінням напруги між колектором і емітером.

Модель ідеального ключа замикає контакти без опору, але BJT є напівпровідниковим приладом із внутрішніми переходами. Тому навіть коли транзистор відкритий настільки, що навантаження обмежує колекторний струм, `V_CE` залишається додатним. У документації його подають як `V_CE(sat)` для вказаних струмів колектора й бази; число залежить від типу транзистора та умов вимірювання.[^aac-bjt-saturation]

Значення 0.1–0.2 V часто використовують як приблизну модель для нескладних розрахунків, але це не універсальний фізичний поріг. Для іншого компонента, струму або температури падіння може бути іншим. Збільшення базового струму часто зменшує `V_CE(sat)`, проте обмежене допустимими струмами бази та розсіюваною потужністю.[^aac-bjt-saturation]

**Приклад:** якщо в розрахунку прийнято `V_CC` = 5 V, `R_C` = 1 kΩ та `V_CE(sat)` = 0.2 V, то струм колектора оцінюють як `I_C = (V_CC - V_CE(sat))/R_C = 4.8 mA`. Це значення є наслідком прийнятої моделі, а не характеристикою кожного транзистора.

**Типова помилка:** вважати «насичений» синонімом «ідеально замкнений». У практичному ключі треба врахувати спад на транзисторі, його потужність і відповідний рядок datasheet.[^aac-bjt-saturation]
