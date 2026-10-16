---
id: py-decor-0008
title: "Чим class decorator відрізняється від metaclass за моментом і областю впливу на class object?"
track: python
section: decorators
sources:
  - source_id: py314-glossary-term-decorator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-decorator
  - source_id: py314-library-functools-functools-wraps
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.wraps
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
  - source_id: py314-reference-compound-stmts-class-definitions
    title: "Python 3.14: Reference/compound Stmts, Class definitions"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#class-definitions
  - source_id: py314-reference-datamodel-creating-the-class-object
    title: "Python 3.14: Reference/datamodel, Creating the class object"
    url: https://docs.python.org/3.14/reference/datamodel.html#creating-the-class-object
  - source_id: py314-reference-datamodel-customizing-class-creation
    title: "Python 3.14: Reference/datamodel, Customizing class creation"
    url: https://docs.python.org/3.14/reference/datamodel.html#customizing-class-creation
  - source_id: py314-reference-datamodel-metaclasses
    title: "Python 3.14: Reference/datamodel, Metaclasses"
    url: https://docs.python.org/3.14/reference/datamodel.html#metaclasses
---

## Short answer

**Class decorator отримує вже побудований class object і може його змінити або замінити.**[^py314-reference-compound-stmts-class-definitions] Metaclass керує самим створенням класу: його викликають як `metaclass(name, bases, namespace)` ще до того, як class object існує.[^py314-reference-datamodel-creating-the-class-object] Decorator діє лише на клас, до якого застосований.[^py314-reference-datamodel-customizing-class-creation] Метаклас успадковується підкласами, тож впливає на всю ієрархію.[^py314-reference-datamodel-metaclasses] Тому decorator простіший і локальніший, а metaclass потужніший, але має ширший вплив.

## Detailed explanation

Class decorator – це callable, який застосовують після того, як інструкція `class` виконала тіло класу й створила class object. Довідка описує це як приблизно еквівалентне `Foo = f1(arg)(f2(Foo))`, тож декоратор бачить готовий клас з атрибутами та методами й може повернути інший об’єкт.[^py314-reference-compound-stmts-class-definitions] Синтаксис той самий, що й для function decorators, які в глосарії описані як функція, що повертає іншу функцію і зазвичай застосовується через `@`.[^py314-glossary-term-decorator] Такий механізм зручний для реєстрації, перевірки чи додавання атрибутів, але декоратор отримує результат створення класу, а не його вхідні дані: `name`, `bases` і `namespace` до нього вже не доходять.

Metaclass – це клас, екземплярами якого є інші класи. Під час створення класу Python викликає його як `metaclass(name, bases, namespace)`, тому його `__new__` отримує сирі `name`, `bases` і `namespace` ще до існування класу.[^py314-reference-datamodel-creating-the-class-object] Саме на цьому етапі метаклас може, наприклад, змінити namespace, перевірити поля або зареєструвати клас до того, як він стане доступним. Наступний приклад показує момент і охоплення обох механізмів: метаклас записує `meta:Base` раніше, ніж декоратор записує `Base`.

```python
registry = []

def register(cls):                 # class decorator: runs after the class body
    registry.append(cls.__name__)
    return cls

class RegisterMeta(type):          # metaclass: runs while the class is being created
    def __new__(mcls, name, bases, namespace, **kwargs):
        registry.append("meta:" + name)
        return super().__new__(mcls, name, bases, namespace, **kwargs)

@register
class Base(metaclass=RegisterMeta):
    x = 1

class Child(Base):                 # the decorator is not re-applied; the metaclass is inherited
    pass

print(registry)   # ['meta:Base', 'Base', 'meta:Child']
```

Охоплення також різне. Class decorator діє лише на той клас, до якого прикріплений, тоді як `__init_subclass__` стосується майбутніх підкласів.[^py314-reference-datamodel-customizing-class-creation] Метаклас успадковується: підклас отримує той самий метаклас від батьківського класу, який його задає.[^py314-reference-datamodel-metaclasses] У прикладі `Child` не проходить через декоратор повторно, але потрапляє до `registry` через метаклас.

На практиці декоратор підходить для одного класу, а метаклас – коли правило має діяти на всю ієрархію. Якщо потрібна лише реакція на створення підкласів, зазвичай простіше `__init_subclass__` у батьківському класі, без окремого метакласу.[^py314-reference-datamodel-customizing-class-creation]

**Типові помилки:**
- вважати, що class decorator діє на підкласи: вони його не отримують, як видно з прикладу;
- писати metaclass там, де достатньо decorator або `__init_subclass__`;
- очікувати, що decorator змінить те, як клас створювався: він отримує вже готовий class object.
