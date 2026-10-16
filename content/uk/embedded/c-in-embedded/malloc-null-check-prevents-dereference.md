---
id: emb-cppfound-0084
title: "Навіщо завжди перевіряти повернення `malloc` на NULL?"
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

`malloc` повертає **NULL** при помилці виділення (нема пам'яті, heap fragmentation). Якщо не перевірити і розіменувати NULL -> <span class="warn">HardFault на MCU</span>.

```c
int *p = malloc(n * sizeof(int));
if(p == NULL) { error_handler(); return; }
// Тепер безпечно використовувати
```

У embedded: malloc може провалитися навіть при малих запитах через fragmentation. Safety-critical стандарти забороняють malloc взагалі – але якщо використовуєш, перевірка обов'язкова.[^embeddedinterviewlab]

## Detailed explanation

TODO
