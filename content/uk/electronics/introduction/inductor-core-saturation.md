---
id: emb-elintro-0147
title: "Що таке насичення осердя індуктора?"
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
  - source_id: aac-core-saturation
    title: "All About Circuits: Controlling and Preventing Core Saturation in Inductors"
    url: https://www.allaboutcircuits.com/technical-articles/controlling-and-preventing-core-saturation-in-inductors/
---

## Short answer

Насичення осердя – це область, де подальше збільшення магнітного поля дає лише малий приріст магнітного потоку, а індуктивність осердного індуктора зменшується. За заданої напруги струм тоді може зростати значно швидше; нагрівання залежить від опору, джерела та тривалості режиму.[^aac-core-saturation]

## Detailed explanation

Насичення виникає у феромагнітному осерді, коли більшість його магнітних доменів уже зорієнтована полем. До цієї області матеріал підсилює магнітний потік: відносно невелике збільшення напруженості поля дає помітний приріст магнітної індукції. Поблизу «коліна» кривої намагнічування цей приріст стає набагато меншим, тож ефективна проникність і індуктивність котушки падають.[^aac-core-saturation]

Наслідок залежить від того, що саме задає коло. Якщо індуктор живиться від приблизно сталої напруги, співвідношення `v = L*di/dt` означає, що менше `L` дає більшу швидкість наростання струму. Це може збільшити втрати в обмотці, ключі та джерелі, спричинити перегрів і порушити роботу перетворювача. Але насичення саме по собі не гарантує пошкодження: струм і температура залежать також від імпедансу кола, обмеження струму та часу роботи.[^aac-core-saturation]

**Приклад:** якщо драйвер прикладає ту саму напругу до котушки, а її диференційна індуктивність після входу в насичення стала вдвічі меншою, `di/dt` у цій спрощеній моделі подвоїться. Це не означає, що струм миттєво подвоюється; він наростає швидше, поки не зміняться напруга, режим ключа або обмеження струму. Виробник часто задає saturation current за визначеним спадом індуктивності, тому це значення треба трактувати за його критерієм, а не як універсальну межу руйнування.[^aac-core-saturation]

**Типова помилка:** вважати, що будь-який індуктор має осердя, яке насичується. Повітряне осердя не має такого насичення, хоча створює інший рівень індуктивності за тих самих витків і струму. У конструкції з осердям перевіряють робочий піковий струм, температуру, частоту та умови вимірювання паспортної індуктивності.[^aac-core-saturation]
