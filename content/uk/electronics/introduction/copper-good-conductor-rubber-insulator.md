---
id: emb-elintro-0034
title: "Чому мідь – хороший провідник, а гума – ізолятор?"
description: "Чому мідь – хороший провідник, а гума – ізолятор?"
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
    applicability: "Походження питання: лекція 5, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: openstax-conductors-insulators
    title: "OpenStax University Physics Volume 2: Conductors, Insulators, and Charging by Induction"
    url: https://openstax.org/books/university-physics-volume-2/pages/5-2-conductors-insulators-and-charging-by-induction
    accessed: 2026-10-04
    kind: book
    version: "University Physics Volume 2"
    applicability: "Пояснює рухливість електронів провідності в металах, зокрема міді, та протиставляє провідники ізоляторам; не задає параметрів конкретної гумової суміші."
  - source_id: openstax-band-theory
    title: "OpenStax University Physics Volume 3: Band Theory of Solids"
    url: https://openstax.org/books/university-physics-volume-3/pages/9-5-band-theory-of-solids
    accessed: 2026-10-04
    kind: book
    version: "University Physics Volume 3"
    applicability: "Пояснює різницю зонної структури провідників та ізоляторів; застосовано лише до якісного пояснення, без матеріалоспецифічних чисел."
---

## Short answer

Мідь проводить струм, бо в твердому металі є рухливі електрони провідності; у гумі за звичайних умов рухливих носіїв значно менше. Різницю пояснюють електронні стани й енергетичні зони матеріалу, а не лише простим підрахунком валентних електронів окремого атома.[^openstax-conductors-insulators][^openstax-band-theory]

## Detailed explanation

Провідність залежить від того, чи може заряд реагувати на електричне поле й переміщатися крізь матеріал. У міді електрони провідності в металі можуть переміщуватися під дією поля; це не означає, що електрон вільний від взаємодії з кристалічною ґраткою, а описує його доступні стани у твердому тілі.[^openstax-conductors-insulators][^openstax-band-theory]

У зонній моделі провідника зайнята електронами верхня зона є частково заповненою, тому електрони можуть змінювати стани під дією поля без переходу через велику заборонену щілину. У типовому ізоляторі зайнята зона заповнена, а найближчі доступні стани відділені енергетичною щілиною; звичайного поля недостатньо, щоб масово створити рухливі носії. Саме ця модель точніша за твердження, ніби провідність міді пояснюється одним слабко зв’язаним електроном кожного атома.[^openstax-band-theory]

Гума – назва класу матеріалів і сумішей, тож її електричні властивості залежать від складу, наповнювачів, стану поверхні й умов експлуатації. У типовій ізоляційній гумі носіям важко переміщатися, і матеріал має високий опір; забруднення або волога можуть сприяти поверхневому витоку, а надмірне електричне поле – пробою. Тому «ізолятор» означає практично малу провідність у заданих умовах, а не абсолютну неможливість проходження струму.[^openstax-conductors-insulators]

Приклад: у кабелі мідна жила є шляхом для струму, а гумова оболонка відокремлює її від людини та інших провідників. Оболонка зменшує струм витоку, але її придатність визначають рейтинг напруги, товщина, температура, старіння й середовище, а не сама назва «гума». Провідник і ізоляція виконують різні функції в одному виробі, хоча обидва матеріали можуть відхилятися від ідеальної поведінки.[^openstax-conductors-insulators]

## Sources

<!-- generated from frontmatter -->
