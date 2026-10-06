---
id: emb-raii-0007
title: "How do you use `unique_ptr` with a custom deleter for a HAL resource?"
description: "A `unique_ptr` with a stateless lambda deleter calls the HAL teardown on scope exit without a control block or reference counting, managing an already existing handle."
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
  - source_id: cpp-draft-unique-ptr-general
    title: "C++ working draft: Unique-ownership pointers, General ([unique.ptr.general])"
    url: https://eel.is/c++draft/unique.ptr.general
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines a unique pointer as an object that stores a pointer and disposes of it through an associated deleter when itself destroyed; unique_ptr is not copyable but is movable. Says nothing about the size of unique_ptr."
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines the constructors taking a deleter, the destructor (`if (get()) get_deleter()(get());`, undefined behavior if the call throws), `release()` and `reset()`, and the requirements on the deleter type. Does not govern the size of unique_ptr or inlining."
  - source_id: cpp-draft-unique-ptr-dltr-dflt
    title: "C++ working draft: default_delete ([unique.ptr.dltr.dflt])"
    url: https://eel.is/c++draft/unique.ptr.dltr.dflt
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Says `default_delete::operator()` calls `delete` on the pointer; says nothing about other deleters."
  - source_id: cpp-draft-expr-delete
    title: "C++ working draft: Delete ([expr.delete])"
    url: https://eel.is/c++draft/expr.delete
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Says the operand of a single-object delete must be null, the result of a previous non-array new, or a pointer to a base class subobject of such an object, otherwise the behavior is undefined. Does not describe what happens on a particular platform."
  - source_id: cpp-draft-lambda-capture
    title: "C++ working draft: Lambda captures ([expr.prim.lambda.capture])"
    url: https://eel.is/c++draft/expr.prim.lambda.capture
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Says an unnamed non-static data member is declared in the closure type for each entity captured by copy, while for entities captured by reference this is unspecified. Does not define sizeof of the closure type or of unique_ptr."
---

## Question code

```cpp
auto del = [](UART_HandleTypeDef* h) {
  HAL_UART_DeInit(h);
};
std::unique_ptr<UART_HandleTypeDef, decltype(del)>
  uart(&huart1, del);
```

## Short answer

**A `unique_ptr` with a lambda deleter calls the HAL teardown when destroyed, that is, on scope exit.** A HAL is a hardware abstraction layer. Here `unique_ptr` does not allocate `huart1`: it only manages the teardown of an existing handle, calling the deleter only if the stored pointer is not null.[^cpp-draft-unique-ptr-single] There is no control block or reference counting. Rule: keep the deleter stateless (a lambda without capture or an empty functor) so `unique_ptr` usually stays pointer-sized; a function pointer deleter usually makes it larger.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
