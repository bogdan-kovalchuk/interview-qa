---
id: emb-fnptr-0040
title: "Trap: what is wrong with passing a non-static method as a C callback?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: cppreference-member-pointers
    title: "cppreference: Pointers"
    url: https://en.cppreference.com/w/cpp/language/pointer
---

## Question code

```cpp
class App {
public:
    void on_rx(uint8_t b);
};

uart_register(&App::on_rx);
```

## Short answer

<span class="warn">`&App::on_rx` has pointer-to-member type, not `void (*)(uint8_t)`.</span>

The method needs a specific object for `this`. The C callback ABI does not know which object to call. Even if a cast forces the types to match, the call will be incorrect.

Protection: write `static void on_rx_thunk(void *ctx, uint8_t b) { static_cast<App *>(ctx)->on_rx(b); }` and register `this` as the context.[^cppreference-member-pointers]

## Detailed explanation

TODO
