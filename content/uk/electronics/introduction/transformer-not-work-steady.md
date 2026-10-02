---
id: emb-elintro-0085
title: "Чому трансформатор не працює від сталого `DC`?"
description: "Чому трансформатор не працює від сталого `DC`?"
track: electronics
section: introduction
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання: лекція 9, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-mutual-inductance
    title: "All About Circuits: Mutual Inductance"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-14/mutual-inductance/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює взаємну індукцію та залежність індукованої напруги від зміни магнітного потоку; охоплює сталий DC і AC."
---


## Short answer

Трансформатор передає енергію між обмотками через змінний магнітний потік. Сталий `DC` після перехідного процесу дає сталий потік і не створює вторинної напруги; первинна обмотка може перегрітися через надмірний струм.[^aac-mutual-inductance]

## Detailed explanation

Трансформатор передає енергію між обмотками завдяки взаємній індукції: зміна струму в первинній обмотці змінює магнітний потік у осерді, а зміна потоку індукує напругу у вторинній обмотці. За сталого `DC` після перехідного процесу струм і потік у первинній обмотці сталі, тому вторинна напруга не підтримується.[^aac-mutual-inductance]

Коли джерело постійної напруги спершу під’єднують, струм у котушці не може миттєво змінитися: виникає короткий перехідний процес, і відповідна зміна потоку може індукувати короткий імпульс у вторинній обмотці. Після встановлення сталого струму потік перестає змінюватися, отже, індукована напруга зникає. При змінному струмі полярність і величина струму змінюються безперервно, тому змінюється і потік, що дає змогу трансформатору працювати.[^aac-mutual-inductance]

На практиці не можна просто під’єднати обмотку трансформатора до джерела `DC`: після перехідного процесу первинна обмотка поводиться переважно як її опір дроту, а струм може стати надмірним і перегріти обмотку. Фактичний струм залежить від опору обмотки та джерела; осердя також може насититися. Трансформаторні схеми з батареєю все ж існують, але вони переривають або перемикають струм, створюючи змінний потік, а не подають на обмотку сталий струм.[^aac-mutual-inductance]

Приклад: перемикач, який коротко подає батарею на первинну обмотку, може спричинити імпульс напруги у вторинній під час вмикання й вимикання. Якщо залишити батарею під’єднаною, після цього імпульсу сталого виходу не буде, зате первинна обмотка може нагріватися. Типова помилка – казати, що DC взагалі не створює магнітного поля: він створює поле, але для сталої індукованої напруги потрібна саме зміна потоку.[^aac-mutual-inductance]

## Sources

<!-- generated from frontmatter -->
