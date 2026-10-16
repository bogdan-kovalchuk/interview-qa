---
id: py-itergen-0009
title: "Що делегує вираз `yield from subiterator` крім простого повторного `yield` кожного value?"
track: python
section: iterators-and-generators
sources:
  - source_id: py314-library-stdtypes-iterator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
  - source_id: py314-reference-datamodel-object-iter
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
  - source_id: pep-0380-yield-from
    title: "PEP 380: Syntax for Delegating to a Subgenerator"
    url: https://peps.python.org/pep-0380/
---

## Short answer

**`yield from` передає значення з `send()` і винятки з `throw()` до subiterator, якщо він їх підтримує.**[^py314-reference-expressions-yield-expressions] Якщо subiterator не має потрібного методу, `send()` піднімає `AttributeError` або `TypeError`, а `throw()` одразу піднімає переданий виняток.[^py314-reference-expressions-yield-expressions] Коли subiterator завершується, його `StopIteration.value` стає результатом самого виразу `yield from`.[^py314-reference-expressions-yield-expressions] `close()` делегувального генератора також передається subiterator-у, якщо в нього є цей метод.[^pep-0380-yield-from]

## Detailed explanation

`yield from` – не еквівалент `for v in sub: yield v`. Цикл передає назовні лише значення. `yield from` робить делегуючий generator прозорим: `send()` і `throw()` ідуть безпосередньо до subiterator, а його `return` стає значенням самого виразу.[^py314-reference-expressions-yield-expressions] Протокол делегування описано в PEP 380, де також сказано, що `close()` передається subiterator-у, якщо той має цей метод.[^pep-0380-yield-from]

Приклад: `outer()` делегує `sub()`. Значення, надіслане через `send()`, потрапляє в `sub`, виняток із `throw()` перехоплює `sub`, а `return "done"` стає результатом `yield from`. Далі звичайний цикл `for` над новим викликом `sub()` показує, що `send()` до нього не доходить:

```python
def sub():
    try:
        received = yield "ready"       # send() value arrives here
        yield f"got {received}"
        return "done"                  # becomes the value of the yield from expression
    except ValueError as exc:          # throw() reaches the subiterator
        yield f"sub caught {exc}"

def outer():
    result = yield from sub()
    print("yield from returned:", result)
    yield "outer finished"

g = outer()
print(next(g))                         # ready
print(g.send("A"))                     # got A
print(next(g))                         # yield from returned: done, then outer finished

h = outer()
print(next(h))                         # ready
print(h.throw(ValueError("boom")))     # sub caught boom

def plain_loop():
    for value in sub():                # the for loop calls next(), never send()
        yield value

k = plain_loop()
print(next(k))                         # ready
print(k.send("B"))                     # got None: "B" is not forwarded
```

Якщо subiterator – звичайний iterator без `send()`, наприклад `list_iterator`, то `send()` з непорожнім значенням піднімає `AttributeError` або `TypeError`, а `throw()` кидає переданий виняток прямо в точці `yield from`.[^py314-reference-expressions-yield-expressions]

**Типові помилки:**
- замінювати `yield from` на `for ... yield` і потім очікувати, що `send()` дійде до subiterator;
- вважати, що `return` у subgenerator віддається як елемент послідовності; насправді це результат `yield from`;
- викликати `send()` з непорожнім значенням для subiterator без `send()`, наприклад для `list_iterator`.
