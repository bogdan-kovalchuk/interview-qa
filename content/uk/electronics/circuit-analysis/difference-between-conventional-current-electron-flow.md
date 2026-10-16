---
id: emb-elcirc-0007
title: "У чому різниця між умовним струмом і рухом електронів?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-conventional-electron-flow
    title: "All About Circuits: Conventional Versus Electron Flow"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-1/conventional-versus-electron-flow/
---

## Short answer

**Conventional current** задають як напрям руху додатного заряду; у металевому провіднику він протилежний середньому дрейфу електронів. Обидва напрями можна використовувати в розрахунках, але схемна домовленість зазвичай використовує conventional current.[^aac-conventional-electron-flow]

## Detailed explanation

Електричний струм визначають як напрям перенесення додатного заряду. Ця домовленість виникла до відкриття електрона й залишилася стандартною в схемах, символах компонентів та більшості інженерних розрахунків. Тому стрілка струму на схемі не обов’язково показує рух конкретних частинок; вона задає знак і напрям величини, з якою працює аналіз.[^aac-conventional-electron-flow]

У металах рухомими носіями заряду є електрони з від’ємним зарядом. Під дією електричного поля їхній дрейф спрямований проти conventional current. Наприклад, у простому колі з батареєю conventional current у зовнішньому колі умовно йде від плюсової клеми до мінусової, тоді як електрони рухаються від мінусової до плюсової. Це опис напрямку дрейфу; тепловий рух електронів хаотичний і значно швидший, але його середнє значення не створює сталого струму.[^aac-conventional-electron-flow]

Для схемного аналізу знак важливіший за фізичний рух носіїв. Якщо розрахунок дає від’ємний струм відносно обраної стрілки, фактичний conventional current спрямований протилежно цій стрілці. Не потрібно міняти всі формули на «електронний» напрям: достатньо послідовно зберігати прийняту систему знаків. У напівпровідниках ситуація ще ширша, бо струм можуть переносити як електрони, так і дірки; твердження про рух електронів від мінуса до плюса стосується металевого провідника, а не кожного носія в кожному матеріалі.[^aac-conventional-electron-flow]

**Типові помилки:**
- Називати напрям умовного струму напрямом руху електронів у металевому дроті.
- Вважати від’ємний результат помилкою замість індикації протилежного напряму відносно обраної стрілки.
- Переносити модель електронного провідника на напівпровідники без згадки про дірки.[^aac-conventional-electron-flow]
