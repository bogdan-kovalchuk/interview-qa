---
id: emb-cppfound-0013
title: "Розберіть?"
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
int arr[3] = {1,2,3};
printf("%d %d", arr[2], *(arr+2));
```

## Short answer

Обидва вирази виводять **3** і є повністю еквівалентними за стандартом C.

`arr[2]` -> стандарт визначає як `*(arr+2)`: до адреси `arr` додається `2 * sizeof(int) = 8` байт, потім розіменовується.

Тому навіть `2[arr]` -> `*(2+arr)` -> 3 – теж коректно (через комутативність додавання, хоча й нечитабельно).[^embeddedinterviewlab]

## Detailed explanation

TODO
