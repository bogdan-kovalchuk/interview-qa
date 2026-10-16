---
id: py-funcs-0015
title: "Чому ім’я, визначене в тілі класу, не стає звичайним enclosing lexical scope для коду методу цього класу?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-reference-executionmodel-resolution-of-names
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#resolution-of-names
  - source_id: py314-reference-executionmodel-lazy-evaluation
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#lazy-evaluation
  - source_id: py314-reference-executionmodel-annotation-scopes
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes
---

## Short answer

**Scope імен, визначених у class block, обмежений самим class block і не поширюється на методи класу.**[^py314-reference-executionmodel-resolution-of-names] Методи не можуть звертатися до атрибутів класу через звичайний lexical lookup – потрібний явний доступ через `self.attr` або `ClassName.attr`. Виняток: annotation scopes (type parameters, annotations) мають доступ до namespace класу.

## Detailed explanation

Тіло класу виконується як звичайний блок, а імена, визначені в ньому, стають атрибутами класу (`Config.__dict__`). Але це не lexical scope для вкладених функцій: ім’я з class block видиме лише в самому class block. Метод є окремою функцією, тож ім’я в його тілі шукається в enclosing function scopes, далі в global namespace і builtins, а class block у цьому ланцюжку пропускається.[^py314-reference-executionmodel-resolution-of-names]

Приклад показує, що ім’я з тіла класу в методі не знаходиться, тоді як атрибут, доступний через `self`, знаходиться:

```python
class Config:
    timeout = 30                  # stored in Config.__dict__

    def get_timeout(self):
        return timeout            # NameError when called: name 'timeout' is not defined

    def get_timeout_ok(self):
        return self.timeout       # found on the class through the instance
```

Виклик `Config().get_timeout()` завершується з `NameError`. Гірше, коли в модулі є глобальна змінна з таким самим іменем: метод мовчки використає її, а не атрибут класу. Той самий механізм ламає comprehension у тілі класу: за `factor = 2` у класі вираз `[v * factor for v in values]` дає `NameError` на `factor`, бо документація прямо включає comprehensions і generator expressions до коду, який не бачить class block.[^py314-reference-executionmodel-resolution-of-names]

Виняток становлять annotation scopes. У 3.14 анотації параметрів і повернення виконуються в annotation scope, який бачить namespace класу, і обчислюються ліниво, тож `def f(self, x: T) -> T` працює поруч із `T = int` у класі, тоді як тіло того самого методу `T` не бачить.[^py314-reference-executionmodel-resolution-of-names][^py314-reference-executionmodel-lazy-evaluation] Раніше анотації обчислювалися одразу в тілі класу. У будь-якому разі `T = int` з класу в них видно.[^py314-reference-executionmodel-annotation-scopes]

**Типові помилки:**
- вважати, що ім’я з тіла класу видно в методах як звичайна змінна; для атрибута потрібен `self.attr` або `ClassName.attr`;
- не помітити, що глобальна змінна з тим самим іменем тихо підміняє задуманий атрибут класу в методі;
- переносити виняток для анотацій на звичайний код у тілі методу.
