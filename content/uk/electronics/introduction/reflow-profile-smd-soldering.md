---
id: emb-elintro-0287
title: "Що таке reflow-профіль для SMD-пайки?"
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
  - source_id: indium-reflow-profile
    title: "Matching a Reflow Profile to a Solder Paste Spec"
    url: https://www.indium.com/blog/matching-a-reflow-profile-to-a-solder-paste-spec/
---

## Short answer

Reflow-профіль описує зміну температури плати й компонентів у часі під час оплавлення паяльної пасти. Його параметри – швидкість нагрівання, можливе вирівнювання температури, пікова температура, час вище liquidus та охолодження – мають відповідати специфікації конкретної пасти й компонентів.[^indium-reflow-profile]

Цільові межі беруть зі специфікацій виробника пасти й компонентів, а не переносять автоматично між процесами.[^indium-reflow-profile]

## Detailed explanation

Reflow-профіль – це температурний графік, якого дотримуються під час нагрівання зібраної SMD-плати, щоб паста розплавилася й утворила паяні з’єднання, а деталі не перегрілися. У типовому процесі плата поступово нагрівається, може мати ділянку soak для вирівнювання температури, проходить вище liquidus пасти, а потім контрольовано охолоджується. Не кожна паста потребує окремої ділянки soak: це визначає її виробник.[^indium-reflow-profile]

Профіль важливий, бо одна й та сама піч може нагрівати різні плати по-різному. Великі мідні площини, масивні компоненти й розміщення на конвеєрі змінюють фактичний час і температуру в місцях з’єднань. Тому специфікація зазвичай обмежує швидкість ramp-up, час вище температури liquidus (TAL), пікову температуру та швидкість охолодження. Профіль перевіряють термопарами, закріпленими на платі, а не лише за заданою температурою печі.[^indium-reflow-profile]

Приклад розрахунку з профілю Indium для пасти Indium8.9HF: перетин liquidus відбувається на 3.1 хвилині, а охолодження нижче liquidus – на 4.4 хвилині. Отже, TAL становить 4.4 – 3.1 = 1.3 хвилини, тобто 78 секунд; виробник порівнює це значення з вимогами саме цієї пасти. Це не універсальна ціль для кожного сплаву чи компонента.[^indium-reflow-profile]

**Типові помилки:** переносити один числовий профіль на всі пасти або орієнтуватися лише на температуру печі. Спочатку звіряють технічний опис пасти й допустимий нагрів компонентів, потім вимірюють профіль реальної плати. Занадто короткий або холодний цикл може лишити неповністю сформовані з’єднання, а надмірний час чи пік здатні пошкодити деталі або флюс.[^indium-reflow-profile]
