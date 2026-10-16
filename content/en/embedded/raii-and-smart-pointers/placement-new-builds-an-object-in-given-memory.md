---
id: emb-raii-0015
title: "How do you construct an object without `malloc` in a preallocated buffer?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-new-delete-placement
    title: "C++ working draft: Non-allocating forms ([new.delete.placement])"
    url: https://eel.is/c++draft/new.delete.placement
  - source_id: cpp-draft-new-syn
    title: "C++ working draft: Header <new> synopsis ([new.syn])"
    url: https://eel.is/c++draft/new.syn
  - source_id: cpp-draft-expr-new
    title: "C++ working draft: New ([expr.new])"
    url: https://eel.is/c++draft/expr.new
  - source_id: cpp-draft-intro-object
    title: "C++ working draft: Object model ([intro.object])"
    url: https://eel.is/c++draft/intro.object
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
  - source_id: cpp-draft-basic-life
    title: "C++ working draft: Object lifetime ([basic.life])"
    url: https://eel.is/c++draft/basic.life
  - source_id: cpp-draft-optional-general
    title: "C++ working draft: Class template optional, general ([optional.optional.general])"
    url: https://eel.is/c++draft/optional.optional.general
---

## Question code

```cpp
alignas(T) std::byte storage[sizeof(T)];
T* obj = new (storage) T(args); // placement new
obj->~T(); // явний виклик dtor
```

## Short answer

**Placement new constructs an object in provided memory without allocation.**

The library `operator new(size_t, void*)` just returns the pointer it is given and does nothing else.[^cpp-draft-new-delete-placement] The memory can be a static array or a memory pool; the standard assumes it has the right size and alignment, so that is the programmer's responsibility.[^cpp-draft-expr-new] The destructor must be called explicitly (`obj->~T()`) because `delete` does not apply here.[^cpp-draft-class-dtor]

Rule: placement new plus explicit dtor equals dynamic construction without the heap.

## Detailed explanation

TODO
