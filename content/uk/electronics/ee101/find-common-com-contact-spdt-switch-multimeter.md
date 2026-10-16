---
id: emb-elee-0008
title: "Як мультиметром знайти спільний контакт (COM) перемикача SPDT?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: aratas-switch-basics
    title: "ARATAS (formerly Omron): What is an Electrical Switch?"
    url: https://www.aratas.com/sg-en/products/basic-knowledge/switches/basics
  - source_id: fluke-continuity
    title: "Fluke: A Guide to Continuity Testing with a Multimeter"
    url: https://www.fluke.com/en-gb/learn/blog/digital-multimeters/how-to-test-for-continuity
---

## Short answer

Знеструмте й від’єднайте перемикач від решти кола, потім перевірте кожну пару контактів у двох положеннях: COM – єдиний контакт, який по черзі замикається з кожним із двох інших. У замкненій парі мультиметр показує малий опір або подає сигнал, а в розімкненій – OL чи відсутність сигналу; точні покази залежать від приладу й контактів.[^fluke-continuity]

## Detailed explanation

COM у SPDT – рухомий спільний контакт: перемикач з’єднує його з одним із двох альтернативних контактів, а в іншому положенні – з другим. На нерухомому корпусі клеми можуть бути розташовані по-різному, тож форму корпуса чи середній ряд контактів не можна вважати надійним маркуванням COM. Визначайте клему за схемою виробника або вимірюванням.[^aratas-switch-basics]

Перед перевіркою від’єднайте живлення та ізолюйте перемикач від паралельних шляхів у схемі. Режим continuity подає власний малий вимірювальний струм; вимірювати ним активне коло не можна. Виберіть continuity або опір, торкніться щупами двох клем і перевірте обидва механічні положення. У парі COM–throw стан має змінитися з провідного на розімкнений або навпаки. Сигнал зумера лише означає, що опір нижчий за поріг конкретного приладу, а не обов’язково рівно нуль Ом.[^fluke-continuity]

Для трьох клем протестуйте всі три пари в обох положеннях. Для справного звичайного SPDT одна клема матиме провідність до першої з решти двох в одному положенні та до другої – в іншому; саме вона є COM. Між двома throw зазвичай немає прямого шляху. Якщо перемикач має кілька полюсів, індикатор або іншу спеціальну схему, кількість фізичних виводів буде більшою, і потрібно спершу розібратися зі схемою конкретного виробу.[^aratas-switch-basics] [^fluke-continuity]

Приклад: позначте клеми A, B і C. Якщо A–B замкнена в першому положенні, а A–C у другому, A є COM, B та C – два throw. Немає підстав називати B «NO», доки не визначено нормальний стан і конкретну конструкцію: NC/NO залежать від неактивованого стану привода.[^aratas-switch-basics]

**Типові помилки:** проводити прозвонку на живій платі або визначати COM за її фізичним місцем. Знеструмлення та перевірка всіх пар у кожному положенні відрізняють справжні контакти перемикача від шляхів навколишньої схеми.[^fluke-continuity]
