---
id: emb-raii-0026
title: "Trap: why is forgetting `= delete` on the copy constructor of a resource wrapper critical?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-copy-ctor
    title: "C++ working draft: [class.copy.ctor]"
    url: https://eel.is/c++draft/class.copy.ctor
  - source_id: cpp-draft-new-delete-single
    title: "C++ working draft: [new.delete.single]"
    url: https://eel.is/c++draft/new.delete.single
  - source_id: cpp-draft-structure-specifications
    title: "C++ working draft: [structure.specifications]"
    url: https://eel.is/c++draft/structure.specifications
---

## Short answer

<span class="warn">The default copy ctor makes a shallow copy of the handle -> two objects own one resource -> double free.</span>[^cpp-draft-class-copy-ctor]

On destruction of both, the dtor releases the resource twice. For `new`/`delete` this is undefined behavior, because the precondition of `operator delete` is violated,[^cpp-draft-new-delete-single][^cpp-draft-structure-specifications] while for an RTOS handle the result depends on the API: an error, corruption, or closing an already closed resource.

Defense: usually either `= delete` copy or move semantics with zeroing the source.[^embeddedinterviewlab]

## Detailed explanation

TODO
