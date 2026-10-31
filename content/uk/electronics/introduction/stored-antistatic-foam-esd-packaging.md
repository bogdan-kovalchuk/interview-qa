---
id: emb-elintro-0028
title: "Навіщо `IC` зберігають в антистатичній піні або `ESD`-упаковці?"
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
  - source_id: ti-esd-packaging
    title: "Texas Instruments: Electrostatic Discharge (ESD) Protective Semiconductor Packing Materials and Configurations"
    url: https://www.ti.com/lit/an/szza027a/szza027a.pdf
---

## Short answer

ESD-упаковка обмежує накопичення заряду та захищає чутливі до електростатичного розряду компоненти під час зберігання й перенесення. Її матеріал і конструкція мають відповідати потрібному рівню захисту; не кожна антистатична піна екранує розряд.[^ti-esd-packaging]

## Detailed explanation

Виводи й внутрішні структури мікросхеми можуть пошкодитися від електростатичного розряду, навіть якщо компонент після цього ще частково працює. Тому захист потрібен не лише під час перевезення: поводьтеся з компонентами у відповідній ESD-зоні та використовуйте упаковку, призначену для чутливих до ESD виробів.[^ti-esd-packaging]

У пакування можуть бути різні функції. Матеріал із низьким зарядоутворенням зменшує заряд, що виникає під час тертя чи відокремлення; dissipative матеріал дає заряду контрольовано розсіюватися, а shielding-оболонка послаблює зовнішнє електричне поле або розряд. Конкретний пакет може поєднувати ці властивості, але слова «антистатичний» самі по собі не доводять, що він забезпечує повний захист від прямого розряду.[^ti-esd-packaging]

Піна для компонентів також буває різною за електричними властивостями; провідна піна може з’єднати між собою виводи, тому її застосовують лише коли це безпечно для конкретного компонента. Не торкайтеся виводів і не покладайтеся на пакувальний матеріал як на заміну заземленню робочого місця та належним процедурам ESD.[^ti-esd-packaging]

**Практичне правило:** залишайте мікросхему в упаковці, маркованій для ESD-захисту, до роботи з нею в підготовленій зоні. Не підмінюйте таку упаковку звичайною пінопластовою підкладкою чи пластиковим пакетом.[^ti-esd-packaging]
