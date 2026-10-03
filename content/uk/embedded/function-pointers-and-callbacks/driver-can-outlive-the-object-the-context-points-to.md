---
id: emb-fnptr-0028
title: "Що таке callback lifetime problem?"
description: "Driver може зберегти callback/context довше, ніж живе об’єкт, на який вони вказують."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

**Driver може зберегти callback/context довше, ніж живе об’єкт, на який вони вказують.**

Наприклад, реєструють `ctx = &local_config` у функції init, функція повертається, stack frame зникає, а interrupt пізніше викликає callback із dangling context. Це use-after-scope.

Правило: context pointer для async callback має вказувати на object із достатнім lifetime: static storage, heap object з ownership, або driver instance, який гарантовано живий до unregister.[^embeddedinterviewlab] [^iso-c-n1570]

## Detailed explanation

Context pointer дає callback доступ до стану його власника, але сам pointer не керує lifetime цього стану. Якщо driver зберіг callback і `ctx`, він може викликати їх значно пізніше за функцію реєстрації, тому об’єкт за `ctx` має залишатися живим до завершення всіх можливих викликів або до гарантованого unregister.[^iso-c-n1570]

У C час життя об’єкта з automatic storage duration завершується, коли виконання виходить із блока, де його оголошено. Коли lifetime закінчився, значення pointer, що вказував на цей об’єкт, стає indeterminate; використання об’єкта через callback не є безпечним. Це не виправляється тим, що stack memory ще фізично містить старі байти: наступний виклик може повторно використати цю область, а оптимізатор не зобов’язаний зберігати її вміст.[^iso-c-n1570]

Практичний наслідок для embedded API: документація має визначати, чи driver копіює context, чи лише зберігає pointer, і коли припиняє викликати callback. Якщо driver зберігає pointer, lifetime контексту має охоплювати весь період реєстрації; до звільнення або виходу власника з області видимості треба зупинити джерело подій та завершити unregister згідно з контрактом драйвера.[^iso-c-n1570]

Наприклад, `init` може зареєструвати `&local_config`, але повернутися раніше за наступне переривання таймера. Саме відкладене виконання перетворює локальний pointer на dangling context. Натомість caller може передати довгоживучий об’єкт, або власник може зберігати driver і контекст в одному екземплярі, життєвий цикл якого ним контролюється.[^iso-c-n1570]

**Типова помилка:** вважати, що передача `void *` копіює структуру. Копіюється лише значення адреси; ownership і час життя залишаються відповідальністю коду, який створив об’єкт. Перевіряй контракт реєстрації та порядок зупинки: спочатку заборонити нові callbacks, потім дочекатися завершення вже активних і лише після цього знищувати контекст. Точний механізм очікування залежить від драйвера й RTOS.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->
