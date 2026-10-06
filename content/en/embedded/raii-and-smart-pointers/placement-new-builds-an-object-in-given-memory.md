---
id: emb-raii-0015
title: "How do you construct an object without `malloc` in a preallocated buffer?"
description: "Placement new constructs an object in provided memory without allocation; the memory must suit the type's size and alignment, and the destructor is called explicitly."
track: embedded
section: raii-and-smart-pointers
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-06
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-06; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: cpp-draft-new-delete-placement
    title: "C++ working draft: Non-allocating forms ([new.delete.placement])"
    url: https://eel.is/c++draft/new.delete.placement
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that the library operator new(size_t, void* ptr) returns ptr and intentionally performs no other action, and that the matching placement operator delete intentionally does nothing; gives an example of constructing an object at a known address. Says nothing about buffer size or alignment."
  - source_id: cpp-draft-new-syn
    title: "C++ working draft: Header <new> synopsis ([new.syn])"
    url: https://eel.is/c++draft/new.syn
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Shows that the declarations of the placement forms of operator new belong to the <new> header. Says nothing about the semantics of the forms."
  - source_id: cpp-draft-expr-new
    title: "C++ working draft: New ([expr.new])"
    url: https://eel.is/c++draft/expr.new
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that the new-placement syntax supplies additional arguments to an allocation function, and that the new-expression assumes the block of storage the function returns is appropriately aligned and of the requested size. Gives no guarantee for a buffer supplied by the programmer: it is an assumption the program must satisfy itself."
  - source_id: cpp-draft-intro-object
    title: "C++ working draft: Object model ([intro.object])"
    url: https://eel.is/c++draft/intro.object
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that an array of unsigned char or std::byte provides storage for an object created in it if the array's lifetime has begun and not ended, the object fits entirely within the array, and no nested array satisfies these constraints. Does not guarantee alignment."
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States in a note that explicit destructor calls are rarely needed but are used for objects placed at specific addresses with placement new, including to cope with dedicated hardware resources and in memory management; that once a destructor is invoked the object's lifetime ends, and invoking it for an object whose lifetime has ended is undefined behavior."
  - source_id: cpp-draft-basic-life
    title: "C++ working draft: Object lifetime ([basic.life])"
    url: https://eel.is/c++draft/basic.life
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that a program may end the lifetime of a class-type object without invoking the destructor by reusing or releasing its storage, that a delete-expression invokes the destructor before releasing the storage, and that program correctness often depends on the destructor being invoked."
  - source_id: cpp-draft-optional-general
    title: "C++ working draft: Class template optional, general ([optional.optional.general])"
    url: https://eel.is/c++draft/optional.optional.general
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that the contained value of an optional is nested within the optional object. Says nothing about the size or cost of optional."
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

## Sources

<!-- generated from frontmatter -->
