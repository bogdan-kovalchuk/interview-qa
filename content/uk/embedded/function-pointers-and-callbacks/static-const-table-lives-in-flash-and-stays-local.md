---
id: emb-fnptr-0022
title: "Чому function pointer table варто робити `static const`?"
description: "На рівні файлу static const задає internal linkage і незмінність елементів; linker script визначає розміщення таблиці."
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
  - source_id: arm-cortex-m-startup
    title: "Arm: Decoding the startup file for Arm Cortex-M4"
    url: "https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/decoding-the-startup-file-for-arm-cortex-m4"
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Приклад Cortex-M4 показує, що read-only секція розміщується linker options; це не універсальна гарантія розміщення будь-якого const об’єкта у Flash."
---

## Short answer

**`static const`** на рівні файлу дає таблиці internal linkage і забороняє змінювати її елементи через цей об’єкт; розміщення у Flash залежить від toolchain та linker script.

Якщо linker script зіставляє read-only секцію з Flash, це може заощадити RAM. Незмінна таблиця також не піддається випадковому перезапису через цей доступ.[^arm-cortex-m-startup]

Приклад: `static const cmd_handler_t handlers[] = { cmd_ping, cmd_reset };`. Перевір linker map, щоб підтвердити фактичну секцію та адресу.[^arm-cortex-m-startup]

## Detailed explanation

У цьому оголошенні `static` і `const` задають різні властивості. На рівні файлу `static` надає ідентифікатору internal linkage: інші translation units не звертаються до цього імені через зовнішнє компонування. `const` кваліфікує елементи масиву, тож програма не може призначати їм нові значення через цей об’єкт. Самі ключові слова не наказують кожному компілятору зберігати масив за конкретною фізичною адресою чи в певній пам’яті.[^iso-c-n1570]

У типовому embedded build read-only секції на кшталт `.rodata` можуть бути зіставлені linker script із Flash. Тоді таблиця не займає відповідну кількість RAM під копію зі значеннями, як це могло б бути для змінних ініціалізованих даних. Але розміщення визначають ABI, формат object file, параметри компілятора та linker script; дивись map-файл і linker configuration конкретного проєкту, перш ніж стверджувати, що таблиця лежить у Flash.[^arm-cortex-m-startup]

`static` також не означає, що таблиця «локальна» у сенсі видимості лише всередині функції: file-scope об’єкт доступний функціям цього translation unit. І `const` не робить довільне інше посилання на ту саму пам’ять безпечним, якщо хтось має окремий writable alias. Практичний сенс тут – приховати символ від інших translation units і виразити незмінність таблиці в C типі.[^iso-c-n1570]

Приклад:

```c
typedef void (*cmd_handler_t)(void);
static const cmd_handler_t handlers[] = { cmd_ping, cmd_reset };
```

**Типові помилки:**

- Вважати, що `static` саме по собі розміщує об’єкт у Flash.
- Плутати file-scope internal linkage з локальною змінною функції.
- Приймати `const` за гарантію захисту фізичної пам’яті від усіх можливих записів.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->
