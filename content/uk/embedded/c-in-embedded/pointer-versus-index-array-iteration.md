---
id: emb-cppfound-0094
title: "Як ефективно ітерувати по масиву через pointer vs індекс – різниця у генерованому коді?"
track: embedded
section: c-in-embedded
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Pointer iteration: `for(int *p=arr; p!=arr+n; p++) use(*p);` Index iteration: `for(int i=0; i<n; i++) use(arr[i]);`

На сучасних компіляторах з оптимізацією (`-O2`): **код зазвичай ідентичний** – компілятор сам перетворює між формами.

Але: pointer iteration уникає повторного обчислення базової адреси (`arr + i` кожен раз). Без оптимізації pointer може бути швидшим. У embedded (без оптимізації): pointer iteration ефективніша для Cortex-M0.[^embeddedinterviewlab]

## Detailed explanation

TODO
