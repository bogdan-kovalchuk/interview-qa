---
id: emb-fnptr-0029
title: "Trap: what is wrong with this context pointer?"
track: embedded
section: function-pointers-and-callbacks
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
void init(void) {
    struct App app;
    timer_register(on_timer, &app);
}
```

## Short answer

<span class="warn">`&app` becomes a dangling pointer after returning from `init`.</span>

If the timer callback fires later, it receives the address of a stack object that no longer exists. On an MCU this can look like random state corruption, a HardFault or a flaky bug.

Protection: make `app` static or global, store it in caller-owned storage, or unregister the callback before the object's lifetime ends.[^embeddedinterviewlab] [^iso-c-n1570]

## Detailed explanation

TODO
