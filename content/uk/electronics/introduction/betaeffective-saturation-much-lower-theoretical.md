---
id: emb-elintro-0214
title: "Чому forced beta насиченого транзистора нижча за beta в активному режимі?"
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

**У насиченні відношення `I_C/I_B` задає зовнішнє коло.** У активному режимі beta описує співвідношення струмів, поки транзистор має достатній `V_CE`; після досягнення межі навантаження колекторний струм майже не зростає від додаткового базового струму.[^aac-bjt-active-mode] Тому фактичне `I_C/I_B` у перемикачі називають forced beta: воно обране драйвером і навантаженням, а не є незмінним підсиленням приладу.[^aac-bjt-beta-terms] Значення «менше 10» не є загальним законом: його треба рахувати для конкретного режиму.

## Detailed explanation

Forced beta в насиченні є відношенням струмів, яке нав’язане навантаженням і базовим керуванням; це не те саме, що beta транзистора в активному режимі.

У прямому активному режимі база керує колекторним струмом, а `β` описує їхнє відношення за конкретних умов. Цей опис працює, поки джерело живлення та навантаження можуть надати запитаний струм і транзистор зберігає достатню напругу колектор–емітер.[^aac-bjt-beta-terms]

Коли навантаження вже обмежує струм, транзистор входить у насичення: базовий струм просить більше, ніж може пройти через колекторну гілку. Подальше збільшення `I_B` мало змінює `I_C`, але змінює відношення `I_C/I_B`. Це відношення називають forced beta, бо його встановили схема та умови, а не лише фізичне підсилення приладу.[^aac-bjt-active-mode] Для проектування ключа таке відношення вибирають достатньо консервативним, аби забезпечити насичення за найгірших умов, звіряючись із документацією.

**Приклад:** якщо навантаження пропускає `I_C` = 20 mA, а керування подає `I_B` = 2 mA, то forced beta дорівнює 10. Якщо збільшити `I_B` до 4 mA, а навантаження й напруга лишилися незмінними, `I_C` залишиться приблизно біля 20 mA, а відношення зменшиться приблизно до 5. Це не означає, що внутрішній активний beta транзистора змінився.

**Типова помилка:** називати мале `I_C/I_B` «поганим beta». У насиченні це наслідок режиму перемикача; значення менше 10 часто трапляється як вибір дизайнера, але не є правилом для всіх моделей.[^aac-bjt-beta-terms]
