---
id: emb-cppfound-0060
title: "Що виведе?"
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

## Question code

```c
int arr[3][3]={{1,2,3},{4,5,6},{7,8,9}};
printf("%d", *(*(arr+1)+2));
```

## Short answer

`6`.

`arr+1` -> вказівник на другий рядок `arr[1]` (тип `int(*)[3]`). `*(arr+1)` -> decay до `int*`, вказує на `arr[1][0] = 4`. `*(arr+1)+2` -> вказує на `arr[1][2] = 6`. `*(*(arr+1)+2)` -> значення = `6`.

Еквівалентно: `arr[1][2]`.[^embeddedinterviewlab]

## Detailed explanation

TODO
