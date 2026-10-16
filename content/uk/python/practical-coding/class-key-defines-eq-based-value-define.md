---
id: py-prac-0005
title: "Клас `Key` визначає `__eq__` за `value`, але не визначає `__hash__`: що станеться при `{Key(1): \"x\"}` і як виправити contract для immutable key?"
track: python
section: practical-coding
sources:
  - source_id: py314-reference-datamodel-object-hash
    title: "Python 3.14: Reference/datamodel, object.__hash__"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__hash__
  - source_id: py314-library-dataclasses-dataclass
    title: "Python 3.14: Library/dataclasses, dataclass"
    url: https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass
---

## Short answer

**Піднімається `TypeError` (unhashable), бо клас, що визначає `__eq__` без `__hash__`, отримує `__hash__ = None`.**[^py314-reference-datamodel-object-hash] Для immutable key визначте `__hash__`, який дає однаковий результат для рівних за `__eq__` об’єктів, наприклад `def __hash__(self): return hash(self.value)`.[^py314-reference-datamodel-object-hash] Для mutable класу з власним `__eq__` `__hash__` визначати не слід, бо зміна значення після вставки в dict ламає пошук.[^py314-reference-datamodel-object-hash]

## Detailed explanation

Хеш потрібен, щоб `dict` і `set` могли знайти ключ за його хешем. Python вимагає одну обов’язкову властивість: об’єкти, які рівні за `__eq__`, мають мати однаковий хеш.[^py314-reference-datamodel-object-hash] Коли клас перевизначає `__eq__` і не визначає `__hash__`, Python ставить `__hash__ = None`. Тоді взяття хешу піднімає `TypeError`, а `isinstance(obj, collections.abc.Hashable)` для такого об’єкта дає `False`.[^py314-reference-datamodel-object-hash]

Приклад: клас з `__eq__` без `__hash__` і літерал `dict`. Помилка виникає вже під час побудови словника:

```python
class Key:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return isinstance(other, Key) and self.value == other.value


try:
    d = {Key(1): "x"}
except TypeError as error:
    print(error)  # 3.13: unhashable type: 'Key'
                  # 3.14: cannot use 'Key' as a dict key (unhashable type: 'Key')
```

Текст повідомлення залежить від версії, тому в коментарі вказано обидва варіанти. Для виправлення immutable key `__hash__` має хешувати ті самі поля, що й `__eq__`. Найкоротший варіант – `@dataclass(frozen=True)`: коли `eq` і `frozen` увімкнені та клас сам не визначає `__hash__`, dataclass генерує `__hash__`; явно визначений `__hash__` він не змінює. `eq` за замовчуванням увімкнено.[^py314-library-dataclasses-dataclass] Приклад:

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Key:
    value: int


d = {Key(1): "x"}
print(d[Key(1)])  # x
```

Для mutable класу `__hash__` визначати не слід. Об’єкт лежить у dict у bucket, який відповідає хешу на момент вставки. Якщо поле, що входить у хеш, змінити після вставки, об’єкт опиняється в «неправильному» bucket, і пошук його не знаходить.[^py314-reference-datamodel-object-hash] Тому mutable клас з `__eq__` або лишають unhashable, або роблять immutable.

**Типові помилки:**
- визначити `__eq__` і забути `__hash__`, а потім отримати `TypeError` на першому `dict` або `set`;
- визначити `__hash__` для mutable класу, а потім змінити поле, яке входить у хеш;
- хешувати поля, яких немає в `__eq__`: рівні об’єкти матимуть різні хеші.
