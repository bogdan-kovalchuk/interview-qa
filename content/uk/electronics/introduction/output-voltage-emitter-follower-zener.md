---
id: emb-elintro-0195
title: "Яка вихідна напруга emitter follower після Зенера?"
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
  - source_id: aac-common-collector
    title: "All About Circuits: The Common-collector Amplifier"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/common-collector-amplifier/
---

## Short answer

Для `NPN` emitter follower вихід на емітері приблизно дорівнює напрузі бази мінус `V_BE`: `V_out ≈ V_Z - V_BE`. Якщо база має `5.1 V`, груба оцінка за `V_BE ≈ 0.7 V` дає `4.4 V`; фактичне значення залежить від струму, температури й режиму транзистора.[^aac-common-collector]

## Detailed explanation

У схемі `NPN` emitter follower база під’єднана до вузла стабілітрона, а навантаження – до емітера. Коли транзистор проводить, перехід база–емітер має пряме падіння напруги, тому емітерна напруга нижча за базову приблизно на `V_BE`. Звідси для простої оцінки `V_out ≈ V_Z - V_BE`; це не точна стала різниця для всіх струмів і температур.[^aac-common-collector]

Наприклад, якщо `V_Z = 5.1 V` і для грубої оцінки взяти `V_BE ≈ 0.7 V`, отримаємо `V_out ≈ 4.4 V`. Значення `0.7 V` є наближенням для кремнієвого транзистора, а не заданою напругою незалежно від режиму. Коли струм навантаження змінюється, змінюються струм емітера і потрібний струм бази; відповідно можуть змінитися і `V_BE`, і напруга базового вузла через ненульовий вихідний опір стабілізатора.[^aac-common-collector] [^aac-semiconductors]

Вихід також не може перевищити межі, дозволені живленням і робочою областю транзистора. За недостатнього запасу між напругою колектора та емітера транзистор входить у насичення і вже не підтримує звичайне співвідношення emitter follower. Для реального проєкту слід перевірити мінімальне живлення, максимальний струм, потужність транзистора та умову, що Зенер зберігає потрібний струм за найбільшого навантаження.[^aac-common-collector] [^aac-semiconductors]

**Типова помилка:** вважати `V_BE` завжди рівним рівно `0.7 V` і обіцяти точні `4.4 V` на виході. Це лише прикладна оцінка; вимоги до точності потребують урахування характеристики транзистора та струмової залежності вузла Зенера.[^aac-common-collector]
