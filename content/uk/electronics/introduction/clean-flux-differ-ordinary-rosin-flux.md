---
id: emb-elintro-0290
title: "Чим `no-clean flux` відрізняється від звичайного rosin flux?"
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
  - source_id: nordson-flux-classifications
    title: "FluxPlus Paste Flux"
    url: https://www.nordson.com/en/products/efd-products/fluxplus-paste-flux
  - source_id: fda-flux-cleaning
    title: "Evaluation of Production Cleaning Processes for Electronic Medical Devices – Part 1, Contaminants"
    url: https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/inspection-technical-guides/evaluation-production-cleaning-processes-electronic-medical-devices-part-1-contaminants
---

## Short answer

No-clean flux має резидуальний флюс, розрахований так, щоб його залишки за звичайних умов можна було не змивати. «Rosin» описує хімію флюсу, тож це не протилежні категорії: існують rosin-based no-clean продукти, а рішення про очищення залежить від специфікації конкретного флюсу.[^nordson-flux-classifications]

Тому «no-clean» не означає, що залишки ніколи не очищують, а «rosin» саме по собі не визначає вимогу до очищення.[^nordson-flux-classifications]

## Detailed explanation

Flux – це речовина, яка допомагає припою змочувати металеві поверхні під час нагрівання. «Rosin» називає хімічну основу флюсу, а «no-clean» – призначення залишку після пайки: його склад і кількість мають дозволяти залишити плату без очищення в умовах, передбачених виробником. Отже, no-clean і rosin не є взаємовиключними назвами: бувають no-clean флюси на основі rosin.[^nordson-flux-classifications]

Залишок no-clean часто є малим за обсягом і після охолодження твердне, але зовнішній вигляд не доводить сумісність із будь-яким пристроєм або середовищем. Виробник Nordson окремо описує no-clean, rosin, RMA й активований rosin flux як різні формуляції з різною активністю та типовими залишками. Зокрема, для активованих форм без тестування не можна автоматично вважати залишок безпечним від корозії; потрібна специфікація саме вибраного матеріалу.[^nordson-flux-classifications]

Очищення може бути потрібним через вимоги до надійності, подальшого покриття, електричного опору ізоляції, зовнішнього вигляду або ремонтопридатності. Для медичних та інших критичних виробів процес очищення встановлюють і перевіряють окремо; не можна замінювати кваліфікований процес припущенням, що будь-який залишок rosin нешкідливий.[^fda-flux-cleaning]

Приклад: якщо технічний опис пасти прямо класифікує її як no-clean і виріб працює у звичайному сухому середовищі, залишок може бути допустимим за вказаних виробником умов. Якщо потрібен конформний лак або специфікація вимагає чистої поверхні, перевіряють сумісність залишку й рекомендований виробником спосіб очищення перед нанесенням покриття.[^nordson-flux-classifications]

**Типова помилка:** вважати, що весь rosin flux обов’язково треба змивати або, навпаки, що позначка no-clean гарантує безпеку в усіх застосуваннях. Вирішальними є точна марка флюсу, документація виробника та вимоги готового виробу.
