---
id: emb-cppfound-0078
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
int arr[]={5,10,15};
printf("%d", 2[arr]);
```

## Short answer

`15`.

`2[arr]` -> за стандартом: `*(2 + arr)` – ідентично `arr[2]`. Subscript operator симетричний через комутативність додавання: `arr[2] == *(arr+2) == *(2+arr) == 2[arr]`.

Всі 4 форми дають однаковий код. `2[arr]` – валідний C, але нечитабельний. Зустрічається як питання на інтерв'ю для перевірки розуміння pointer arithmetic.[^embeddedinterviewlab]

## Detailed explanation

TODO
