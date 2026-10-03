---
id: emb-elintro-0242
title: "Чому термін `saturation` у MOSFET може плутати після BJT?"
description: "Чому термін `saturation` у MOSFET може плутати після BJT?"
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
    applicability: "Походження питання: лекція 22, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: toshiba-mosfet-drive
    title: "Toshiba: MOSFET Gate Drive Circuit, Application Note"
    url: https://toshiba.semicon-storage.com/info/TPH4R50ANH1_application_note_en_20180726_AKX00068.pdf?did=59460&prodName=TPH4R50ANH1
    accessed: 2026-10-04
    kind: official
    version: "AKX00068-1, 2018-07-26"
    applicability: "Режими роботи MOSFET, умови відкривання, залежність R_DS(on) від V_GS і температури та втрати перемикання."
---

## Short answer

У BJT `saturation` означає, що обидва переходи зміщені прямо і транзистор у ключовій схемі має малу `V_CE`; це не просто синонім увімкненого стану. У MOSFET `saturation` означає pinch-off біля стоку й часто відповідає області підсилення. Для ввімкненого MOSFET-ключа потрібна `linear/triode` область із малим `R_DS(on)`.[^aac-semiconductors] [^toshiba-mosfet-drive]

## Detailed explanation

Слово `saturation` має різний зміст у BJT і MOSFET, тому механічне перенесення терміна між ними легко призводить до неправильної робочої точки. У BJT насичення описує стан, коли перехід база–емітер і перехід база–колектор зміщені прямо. У типовому низькобічному ключі це дає малу напругу `V_CE`, хоча конкретне падіння залежить від струму колектора й керування базою.[^aac-semiconductors]

Для enhancement-mode MOSFET область `saturation` визначається напругою `V_DS`, що досягає приблизно `V_GS - V_th`: канал звужується біля стоку (pinch-off). У спрощеній моделі струм після цього змінюється слабше зі зростанням `V_DS`, тож область часто використовують для підсилення. Це не означає нульового опору чи «повного відкривання» ключа.[^toshiba-mosfet-drive]

Увімкнений силовий MOSFET зазвичай працює при невеликому `V_DS`, нижче межі pinch-off, у `linear/triode` області. Там канал має малий `R_DS(on)`; його значення виробник задає для конкретних `V_GS` та умов вимірювання. Саме цей режим дає мале падіння напруги на транзисторі під час провідності.[^toshiba-mosfet-drive]

Приклад: якщо у схемі ключа `V_GS` достатня, а навантаження задає струм, MOSFET установлює мале `V_DS` відповідно до струму й ефективного опору каналу. Якщо ж напруга на навантаженні змушує транзистор підтримувати велике `V_DS`, він може перейти в `saturation`; добирати його як низьковтратний ключ треба за умовами навантаження та datasheet, а не за самою назвою режиму.[^toshiba-mosfet-drive]

**Типова помилка:** вважати, що насичення означає одне й те саме для обох транзисторів. Щоб уникнути плутанини, пов’язуйте термін із графіком і умовою конкретного компонента: прямозміщеними переходами в BJT або pinch-off у MOSFET.[^aac-semiconductors] [^toshiba-mosfet-drive]

## Sources

<!-- generated from frontmatter -->
