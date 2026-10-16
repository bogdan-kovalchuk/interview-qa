---
id: emb-elintro-0024
title: "Що таке ват?"
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
  - source_id: bipm-si-brochure
    title: "BIPM: The International System of Units, 9th edition"
    url: https://www.bipm.org/en/si-brochure-9
---

## Short answer

Ват (W) – одиниця потужності; `1 W = 1 J/s`. Потужність описує швидкість передавання або перетворення енергії.[^bipm-si-brochure]

## Detailed explanation

Потужність показує, скільки енергії передається або перетворюється за одиницю часу. Ват дорівнює одному джоулю за секунду, тому `P = E/t` для сталої потужності.[^bipm-si-brochure]

В електричному колі потужність споживача може перетворюватися на тепло, світло, звук або механічну роботу. Назва результату залежить від пристрою, але одиниця характеризує темп перетворення енергії, а не загальну кількість енергії.[^aac-direct-current]

Для резистивного елемента у відповідному режимі можна також обчислити потужність як `P = V*I`. Якщо струм або напруга змінюються з часом, миттєва потужність теж змінюється, і для енергії за інтервал треба врахувати її зміну в часі.[^aac-direct-current]

Однакова потужність не означає однакову кількість переданої енергії: важлива також тривалість роботи. Наприклад, навантаження потужністю `5 W`, яке працює `10 s`, отримує `50 J`, якщо потужність стала. Для реального джерела та навантаження фактичні значення залежать від режиму роботи й втрат, тож номінальну потужність компонента не слід автоматично вважати потужністю, яку він споживає постійно.[^aac-direct-current]

**Приклад:** пристрій, що протягом `10 s` передає `50 J` енергії, має середню потужність `P = E/t = 50 J/10 s = 5 W`.
