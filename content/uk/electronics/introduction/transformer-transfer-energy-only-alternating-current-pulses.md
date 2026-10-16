---
id: emb-elintro-0156
title: "Чому трансформатор передає енергію тільки при змінному струмі або імпульсах?"
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
  - source_id: electronics-tutorials-transformer-basics
    title: "Electronics Tutorials: Transformer Basics and Transformer Principles"
    url: https://www.electronics-tutorials.ws/transformer/transformer-basics.html
---

## Short answer

Вторинна напруга виникає, коли магнітний потік через обмотку змінюється; її створюють AC або імпульси, а не сталий DC після перехідного процесу.[^electronics-tutorials-transformer-basics] Подача DC на первинну обмотку може спричинити надмірний струм і перегрів, бо після перехідного процесу індуктивний опір не обмежує його так, як при AC.[^electronics-tutorials-transformer-basics]

## Detailed explanation

Трансформатор передає енергію між обмотками через змінний магнітний потік у спільному осерді. Струм первинної обмотки створює потік, а закон електромагнітної індукції пов’язує наведену напругу в кожній обмотці зі швидкістю зміни цього потоку та кількістю витків.[^electronics-tutorials-transformer-basics]

За синусоїдальної напруги потік періодично змінюється, тому у вторинній обмотці постійно наводиться напруга. Імпульсне живлення також працює: кожен фронт або спад змінює потік і створює короткочасну напругу, а схема перемикання задає повторення імпульсів і шлях для енергії.[^electronics-tutorials-transformer-basics] Отже, вислів «тільки AC» був би надто вузьким: важлива зміна потоку, а не саме синусоїдальна форма сигналу.

Після завершення перехідного процесу від постійного струму магнітний потік стає сталим. Тоді `dΦ/dt = 0`, тож вторинна напруга не індукується; короткий імпульс напруги можливий під час підключення або відключення джерела, поки потік змінюється.[^electronics-tutorials-transformer-basics]

Для звичайного трансформатора пряме тривале підключення постійної напруги небезпечне: індуктивний опір, що обмежує змінний струм, для steady DC не діє, і струм визначається переважно малим опором мідного дроту. Це може перегріти обмотку; у практичних перетворювачах DC спершу комутують, створюючи змінний потік.[^electronics-tutorials-transformer-basics]

**Типова помилка:** казати, що трансформатор «передає AC». Він передає енергію через змінний магнітний потік, який можуть створювати як періодичний сигнал, так і імпульси; сталий потік наведеної напруги не підтримує.[^electronics-tutorials-transformer-basics]
