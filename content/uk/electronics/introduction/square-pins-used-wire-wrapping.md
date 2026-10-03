---
id: emb-elintro-0281
title: "Чому для wire wrapping використовують квадратні піни?"
description: "Чому для wire wrapping використовують квадратні піни?"
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
    applicability: "Походження питання: лекція 25, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: cooper-wire-wrap
    title: "CooperTools: Wire-Wrap Connections"
    url: https://static6.arrow.com/aropdfconversion/fc981550a66dae636e73dfb0581f75e8ea6a96eb/wirewrap.pdf
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Описує, як натягнутий дріт контактує з гострими кутами клеми та утворює газонепроникне з’єднання; не стверджує, що будь-який круглий контакт неможливий."
  - source_id: qatech-wire-wrap
    title: "QA Technology: Socket and Termination Selections"
    url: https://www.qatech.com/en/resources-general/socket-termination-selection.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Описує квадратні wire-wrap піни як тип клеми та вказує на газонепроникність з’єднання як захист від корозії."
---

## Short answer

Під час wire wrapping натягнутий дріт притискається до кутів квадратного піна, створюючи кілька щільних контактних ділянок і газонепроникне з’єднання. Це властивість правильно підібраної пари дроту, піна й інструмента, а не універсальна гарантія проти будь-якого круглого контакту.[^cooper-wire-wrap]

## Detailed explanation

Wire wrapping – це механічний спосіб створення електричного з’єднання без припою. Інструмент намотує оголений провід навколо металевого піна під контрольованим натягом. На квадратному піні кутові ребра втискаються в поверхню дроту, а дріт облягає кути в кількох місцях. Такий великий локальний тиск забезпечує щільний металевий контакт; правильно виконане з’єднання називають газонепроникним, бо контактні ділянки захищені від доступу повітря і корозії.[^cooper-wire-wrap]

Квадратна форма також дає передбачувану геометрію для спеціального біта інструмента. Але самої форми піна недостатньо: важливі сумісні діаметр проводу, розмір клеми, кількість витків і відповідний wrap tool. Неправильний біт або слабкий натяг може дати вільну чи відкриту намотку, яка не має потрібної механічної стабільності. Контактний опір і надійність залежать від матеріалів, покриття та якості виконання, тому слово «газонепроникний» не означає, що будь-яка саморобна намотка автоматично довговічна.[^cooper-wire-wrap]

На відміну від паяння, тут з’єднання утворюється тиском і деформацією контактних поверхонь, а не розплавленням припою. Цей метод зручний для монтажних панелей і макетів, де треба швидко з’єднати багато точок і за потреби переробити проводку. Він вимагає сумісних спеціальних пінів та інструменту і не є універсальною заміною паянню чи роз’єму.[^qatech-wire-wrap]

Приклад: якщо документація клеми задає квадратний пін 0.025 дюйма і провід 30 AWG, потрібно використати відповідні біт і гільзу інструмента, а не просто намотати довільний провід на будь-який квадратний штир.[^cooper-wire-wrap]

**Типові помилки:**
- Вважати, що квадратна форма сама по собі гарантує надійність без правильного інструмента й параметрів дроту.
- Пояснювати принцип лише «гострими гранями», не згадуючи натяг, контактний тиск і кілька точок контакту.
- Стверджувати, що круглий контакт завжди прокручується: висновок залежить від конструкції конкретного з’єднання.

## Sources

<!-- generated from frontmatter -->
