---
id: emb-cppfound-0026
title: "Чим відрізняється `const int *p` від `int * const p`?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`const int *p` (або `int const *p`) – **вказівник на константний int**:
- `*p = 5` – заборонено (дані захищені);
- `p = &y` – дозволено (адресу можна змінити).

`int * const p` – **константний вказівник на int**:
- `*p = 5` – дозволено;
- `p = &y` – заборонено (адреса фіксована).

`const int * const p` – і дані, і адреса незмінні. Правило: читай справа наліво.[^embeddedinterviewlab]

## Detailed explanation

TODO
