---
id: emb-elintro-0215
title: "Чому `I_B` не змінився, коли `R_C` зменшили з 1 kΩ до 330 Ω?"
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

**Базовий і колекторний струми проходять різними гілками.** Якщо `V_in`, `R_B` і перехід база–емітер не змінилися, то в простій схемі з окремими колами `I_B ≈ (V_in - V_BE)/R_B` лишається приблизно сталим. Зміна `R_C` змінює допустимий колекторний струм і робочу точку; менший опір дозволяє більший струм за тієї самої напруги живлення.[^aac-bjt-active-mode] Незалежність не абсолютна: транзистор може вийти з насичення, зміниться `V_BE`, нагрів або просідання джерела вплине на `I_B`.[^aac-bjt-saturation]

## Detailed explanation

У простій схемі базовий струм визначається базовим колом, тому зміна `R_C` сама по собі зазвичай не змінює `I_B`.

Для NPN-транзистора з емітером на землі, окремим резистором `R_B` від джерела керування до бази та фіксованими `V_in` і `V_BE`, базовий струм оцінюють як `I_B = (V_in - V_BE)/R_B`. `R_C` розташований у колекторному колі, тож його заміна не входить до цього наближеного рівняння. Такий поділ гілок пояснює, чому в навчальному досліді базовий струм залишився приблизно тим самим.

Колекторний струм натомість обмежений напругою живлення, `R_C` і транзистором. За того самого `V_CC`, менший `R_C` допускає більший струм навантаження, якщо джерело та транзистор його забезпечують. Заміна 1 kΩ на 330 Ω тому змінює навантажувальну пряму та може змінити робочу точку або вивести транзистор із насичення.[^aac-bjt-active-mode]

Незалежність струмів є наближенням, не абсолютним законом для будь-якої топології. У реальному колі `V_BE` залежить від струму й температури; спільний опір емітера, просідання джерела, обмеження драйвера або зміна режиму можуть опосередковано змінити `I_B`. Тому твердження стосується схеми з незалежним базовим живленням і незмінними умовами.[^aac-bjt-saturation]

**Приклад:** за `V_in` = 5 V, `R_B` = 3.3 kΩ та наближеного `V_BE` = 0.7 V отримуємо `I_B ≈ 1.30 mA` до й після заміни `R_C`, якщо ці величини не змінилися.

**Типова помилка:** казати, що колекторне й базове кола взагалі ніяк не впливають одне на одне. Їхні робочі точки пов’язані транзистором, хоча в цій простій оцінці `R_C` не задає безпосередньо базовий струм.
