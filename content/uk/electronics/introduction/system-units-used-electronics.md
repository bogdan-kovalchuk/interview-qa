---
id: emb-elintro-0020
title: Яку систему одиниць використовують в електроніці?
description: Яку систему одиниць використовують в електроніці?
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
  applicability: 'Historical question provenance: lecture 4 of the Udemy course. Original flashcards remain in imports.
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
- source_id: bipm-si
  title: 'BIPM: The International System of Units, SI Brochure'
  url: https://www.bipm.org/documents/20126/41483022/SI-Brochure-9.pdf
  accessed: 2026-10-04
  kind: official
  version: 9th edition, version 4.01
  applicability: SI base units, named derived units and decimal prefixes.
---

## Short answer

Електроніка використовує SI: base units включають second, metre, kilogram та ampere; volt, ohm, farad, henry, coulomb, joule, watt і hertz – derived units. Decimal prefixes на кшталт milli, micro та kilo масштабують одиниці. Регістр unit symbols і prefixes має значення. [^bipm-si]

## Detailed explanation

Сім SI base units – second (s), metre (m), kilogram (kg), ampere (A), kelvin (K), mole (mol) і candela (cd). Поширені електричні величини використовують SI units: current вимірюють в A, voltage – у V, resistance – в Ω, capacitance – у F, inductance – у H. Hertz (Hz) задає frequency як inverse seconds. [^bipm-si]

Співвідношення одиниць дозволяють перевіряти рівняння: `1 C = 1 A*s`, `1 V = 1 J/C`, `1 Ω = 1 V/A` та `1 W = 1 J/s = 1 V*A`. Числа без unit недостатньо для електричної величини. Наприклад, 5 mA і 5 A відрізняються в 1000 разів. [^bipm-si]

Prefixes позначають степені десяти: milli (m) – `10^-3`, micro (µ) – `10^-6`, nano (n) – `10^-9`, kilo (k) – `10^3`, mega (M) – `10^6`. Отже, mA і MA відрізняються в мільярд разів. Між value і unit пишіть пробіл, як у `10 kΩ`; зберігайте регістр symbols під час перекладу тексту. [^bipm-si]

## Sources

<!-- generated from frontmatter -->
