---
id: emb-cppoop-0016
title: "What is a pure virtual function and an abstract class?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-abstract
    title: "C++ working draft: Abstract classes ([class.abstract])"
    url: https://eel.is/c++draft/class.abstract
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
  - source_id: cpp-core-guidelines
    title: "C++ Core Guidelines: C.121 (interface as pure abstract class)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c121-if-a-base-class-is-used-as-an-interface-make-it-a-pure-abstract-class
---

## Question code

```cpp
class Sensor {
public:
  virtual int16_t read() = 0;
  virtual ~Sensor() = default;
};
```

## Short answer

**`= 0` makes a function pure virtual; a class with a function whose final overrider is pure is abstract, so its objects can exist only as subobjects of derived classes.**[^cpp-draft-class-abstract] It defines an interface (contract): a derived class that leaves any pure virtual function unimplemented stays abstract too. In embedded code it is the C++ way to describe a driver/HAL interface; the Core Guidelines advise building it from pure virtual functions and a virtual destructor.[^cpp-core-guidelines]

## Detailed explanation

TODO
