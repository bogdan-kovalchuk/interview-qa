---
id: emb-elintro-0010
title: Чому не можна підключати електролітичний конденсатор у зворотній полярності?
description: Чому не можна підключати електролітичний конденсатор у зворотній полярності?
track: electronics
section: introduction
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
anki:
  export: true
sources:
- source_id: udemy-electronics-course
  title: 'Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу'
  url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  accessed: 2026-09-27
  kind: community
  version: null
  applicability: 'Historical question provenance: lecture 3 of the Udemy course. Original flashcards remain in imports.
    Current answers and explanations were independently revised against cited technical sources on 2026-10-04; this
    source is not factual proof of the revised prose.'
- source_id: aac-direct-current
  title: 'All About Circuits textbook, Volume I: DC'
  url: https://www.allaboutcircuits.com/textbook/direct-current/
  accessed: 2026-09-27
  kind: book
  version: null
  applicability: 'Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання;
    конкретні номінали й схеми курсу можуть відрізнятися.'
- source_id: aac-semiconductors
  title: 'All About Circuits textbook, Volume III: Semiconductors'
  url: https://www.allaboutcircuits.com/textbook/semiconductors/
  accessed: 2026-09-27
  kind: book
  version: null
  applicability: 'Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела
    живлення; конкретні номінали й схеми курсу можуть відрізнятися.'
- source_id: nichicon-polarity
  title: 'Nichicon: Technical notes for aluminum electrolytic capacitors'
  url: https://www.nichicon.co.jp/english/products/pdf/aluminum.pdf
  accessed: 2026-10-04
  kind: official
  version: null
  applicability: Polarized oxide dielectric, charge/energy relations and reverse-voltage damage, section 2-3-2.
- source_id: vishay-tantalum
  title: 'Vishay: Solid tantalum capacitor FAQ'
  url: https://www.vishay.com/docs/40110/faq.pdf
  accessed: 2026-10-04
  kind: official
  version: null
  applicability: 'Polarity markings: white bar marks the positive anode on molded SMD tantalum capacitors.'
---

## Short answer

Reverse voltage може пошкодити dielectric polarized electrolytic capacitor, спричинивши leakage, нагрівання й утворення газу. Polarity визначайте за marking і datasheet точного компонента: типові radial aluminum parts позначають negative side, тоді як смуга на molded SMD tantalum capacitors позначає positive anode. [^nichicon-polarity] [^vishay-tantalum]

## Detailed explanation

У polarized aluminum electrolytic capacitor тонкий oxide dielectric сформовано для заданої polarity. Nichicon пояснює, що reverse voltage може збільшити leakage та спричинити нагрівання й утворення газу з можливим venting чи failure. Вибух – можливий тяжкий наслідок, а не гарантована реакція на кожне коротке переполюсування. [^nichicon-polarity]

У типових radial aluminum parts орієнтації допомагають negative stripe та необрізаний довший positive lead. Після обрізання довжина виводу вже ненадійна. Не поширюйте convention negative stripe на всі electrolytics: Vishay прямо вказує, що white bar на molded SMD tantalum parts визначає positive anode. [^vishay-tantalum]

Перед монтажем зіставте body marking і datasheet pinout зі schematic та PCB polarity. Перевірте також форму напруги: позитивне середнє значення не робить reverse excursions автоматично допустимими. Дотримуйтеся rated voltage й permitted ripple current. Bipolar electrolytics – окремий specified part type; не припускайте, що звичайний polarized part поводиться так само. [^nichicon-polarity]

## Sources

<!-- generated from frontmatter -->
