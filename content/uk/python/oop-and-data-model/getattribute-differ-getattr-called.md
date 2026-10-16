---
id: py-oop-0005
title: "Чим `__getattribute__` відрізняється від `__getattr__` і коли викликається кожен із них?"
track: python
section: oop-and-data-model
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
  - source_id: py314-howto-descriptor
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html
  - source_id: py314-howto-mro
    title: "Python 3.14: Howto/mro"
    url: https://docs.python.org/3.14/howto/mro.html
  - source_id: py314-library-dataclasses
    title: "Python 3.14: Library/dataclasses"
    url: https://docs.python.org/3.14/library/dataclasses.html
  - source_id: py314-reference-datamodel-object-getattribute
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__
  - source_id: py314-reference-datamodel-object-getattr
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__
  - source_id: py314-reference-datamodel-special-method-lookup
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#special-method-lookup
---

## Short answer

**`__getattribute__` викликається для кожного явного доступу до атрибута екземпляра (`obj.name` або `getattr(obj, 'name')`); `__getattr__` – лише як fallback, коли звичайний lookup завершився `AttributeError`.**[^py314-reference-datamodel-object-getattribute] <span class="warn">Якщо перевизначити `__getattribute__`, потрібно обережно делегувати до `super().__getattribute__()`, інакше можна зламати доступ до всіх атрибутів, включно з методами.</span>[^py314-reference-datamodel-object-getattribute] `__getattr__` безпечніший: він не зачіпає нормальний шлях пошуку.[^py314-reference-datamodel-object-getattr]

## Detailed explanation

`__getattribute__` реалізує сам доступ до атрибута екземпляра. Python викликає його для кожного явного звернення `obj.name` і `getattr(obj, 'name')`, навіть якщо атрибут існує і звичайний пошук його знайде.[^py314-reference-datamodel-object-getattribute] `__getattr__` працює інакше: він викликається лише тоді, коли звичайний доступ завершився `AttributeError` або коли сам `__getattribute__` підняв `AttributeError`.[^py314-reference-datamodel-object-getattr] Тож `__getattr__` – це запасний варіант для відсутніх атрибутів, а `__getattribute__` бачить кожне звернення.

Приклад показує порядок викликів:

```python
class Tracer:
    def __init__(self):
        self.real = 1

    def __getattribute__(self, name):
        print(f"__getattribute__({name!r})")
        return object.__getattribute__(self, name)

    def __getattr__(self, name):
        print(f"__getattr__({name!r})")
        return "fallback"

    def __len__(self):
        return 3

t = Tracer()
print(t.real)      # __getattribute__('real'), then 1
print(t.nothing)   # __getattribute__('nothing'), __getattr__('nothing'), then 'fallback'
print(len(t))      # no __getattribute__ line: len() looks up __len__ on the type, prints 3
```

Рядок `len(t)` не дає жодного виклику `__getattribute__`: неявний виклик спеціального методу шукає `__len__` у типі, минаючи звичайний доступ до атрибута.[^py314-reference-datamodel-special-method-lookup] Тож перехоплювач не бачить неявні виклики спеціальних методів.

Головна пастка – у тому, як написано перевизначення. `__getattribute__` має звертатися до атрибутів через базовий `object.__getattribute__` або `super().__getattribute__()`.[^py314-reference-datamodel-object-getattribute] Якщо написати `return self.__dict__[name]`, доступ до `self.__dict__` знову піде через `__getattribute__`, і виклики зациклюються до `RecursionError`. Якщо ж повертати значення лише для окремих імен і інакше піднімати `AttributeError`, методи класу перестануть знаходитися.

Тому для проксі, ледачого обчислення або значень за замовчуванням зазвичай досить `__getattr__`, який не змінює звичайний шлях пошуку. `__getattribute__` доречний, коли треба перехоплювати кожен явний доступ, наприклад для аудиту, і тоді делегування до базового методу обов’язкове.

**Типові помилки:**
- вважати, що `__getattr__` викликається для кожного звернення, і логувати в ньому доступ до існуючих атрибутів; він їх не побачить;
- писати `self.__dict__` або `self.name` всередині `__getattribute__`, що дає рекурсію;
- очікувати, що `len(obj)` або `obj + 1` пройдуть через `__getattribute__`.
