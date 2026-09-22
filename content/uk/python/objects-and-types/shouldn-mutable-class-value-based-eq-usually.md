---
id: py-objtypes-0012
title: "Чому mutable class із value-based `__eq__` зазвичай не повинна успадковувати identity-based hash від `object`?"
description: "Контракт Python вимагає: якщо два об'єкти рівні за __eq__, вони повинні мати однаковий hash; identity-based hash від object використовує унікальний id(), тому рівні за значенням об'єкти потраплять у різні hash-корзини..."
track: python
section: objects-and-types
level: senior
type: mechanism
tags: [eq, object]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L206-L242
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Контракт Python вимагає: якщо два об'єкти рівні за `__eq__`, вони повинні мати однаковий hash; identity-based hash від `object` використовує унікальний `id()`, тому рівні за значенням об'єкти потраплять у різні hash-корзини dict/set і стануть «невидимими» при пошуку.**[^py314-reference-datamodel] Для mutable класу з value-based `__eq__` правильне рішення – або зробити клас unhashable (`__hash__ = None`), або визначити `__hash__` на основі тих самих полів, що й `__eq__`, і гарантувати їх незмінність після додавання в dict/set. <span class="warn">У CPython `object.__hash__` базується на `id()`, тобто на адресі об'єкта в пам'яті.</span>

## Detailed explanation

Контракт геш-таблиць у Python прямо вимагає: якщо `a == b`, то значення `hash(a) == hash(b)` має бути однаковим протягом усього життєвого циклу об'єктів.[^py314-reference-datamodel] За замовчуванням користувацькі класи успадковують `__eq__` та `__hash__` від `object`. У цій базовій реалізації рівність означає ідентичність (`self is other`), а геш обчислюється на основі `id()` (у CPython – адреси в пам'яті). Якщо ж клас перевизначає `__eq__` для порівняння значень (value-based equality), але залишає гешування за ідентичністю, контракт миттєво руйнується: два незалежні екземпляри з однаковими значеннями повертають `True` при порівнянні `==`, але мають різні геші.

Порушення цього інваріанта руйнує роботу `set` та `dict`. Під час пошуку ключа геш-таблиця спочатку обчислює `hash(key)`, знаходить відповідний слот (bucket) і лише серед колізій у цьому слоті перевіряє рівність за `__eq__`. Якщо два екземпляри мають різні геші, операція пошуку `b in {a}` шукатиме об'єкт `b` у зовсім іншому слоті й поверне `False`, навіть коли `a == b`. У результаті множина може містити дублікати об'єктів, які формально вважаються однаковими, що позбавляє колекцію фундаментальних гарантій унікальності.

Саме тому Python автоматично запобігає цій проблемі: у Python 3, якщо клас перевизначає `__eq__` і не оголошує `__hash__`, інтерпретатор неявно встановлює `__hash__ = None` і блокує успадкування від `object`.[^py314-reference-datamodel] Спроба гешувати такий об'єкт або додати його в `set` викликає `TypeError: unhashable type`. Якщо ж розробник вручну примусово повертає `__hash__ = object.__hash__`, він створює приховану пастку, у якій геш-таблиці перестають знаходити елементи.

Приклад порушення контракту гешування при ручному призначенні `object.__hash__`:

```python
class BrokenPoint:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, BrokenPoint):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    # Forcing identity hash breaks hash table lookups
    __hash__ = object.__hash__


p1 = BrokenPoint(1, 2)
p2 = BrokenPoint(1, 2)

print(p1 == p2)               # True (equal values)
print(hash(p1) == hash(p2))   # False (different id-based hashes)

points = {p1}
print(p2 in points)           # False (lookup checks different bucket!)

points.add(p2)
print(len(points))            # 2 (duplicate entries in a set)
```

**Практичні наслідки та архітектурні правила:**
- автоматичне блокування: перевизначення `__eq__` автоматично встановлює `__hash__ = None`, якщо `__hash__` не оголошено явно;
- незмінність гешованих полів: якщо об'єкт гешується за значеннями своїх атрибутів, ці атрибути мають бути незмінними (наприклад, через `frozen=True` у dataclass або read-only property);
- ризик мутації в колекції: зміна поля, від якого залежить геш, після додавання в `dict` або `set`, робить об'єкт «загубленим» у структурі даних без можливості зчитування чи видалення;
- явний вибір дизайну: якщо сутність є мутабельною, її слід або залишити негешованою (`__hash__ = None`), або спиратися суто на ідентичність і для рівності, і для гешування (`object.__eq__` та `object.__hash__`).

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
