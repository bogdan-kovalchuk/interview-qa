---
id: py-prac-0009
title: "Спроєктуйте copy operation для tree з shared subtrees та possible cycles, зберігши graph topology без aliasing з original."
track: python
section: practical-coding
sources:
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
  - source_id: py314-library-functions-id
    title: "Python 3.14: Library/functions, id"
    url: https://docs.python.org/3.14/library/functions.html#id
---

## Short answer

**Використати memo-dict, ключований за `id()` оригінального вузла: перед рекурсивним копіюванням перевіряти, чи вузол вже скопійований, і повертати існуючу копію.**[^py314-library-copy]

```python
def deep_copy_graph(root):
    memo = {}
    def _copy(node):
        nid = id(node)
        if nid in memo:
            return memo[nid]
        if isinstance(node, list):
            new_list = []
            memo[nid] = new_list
            new_list.extend(_copy(item) for item in node)
            return new_list
        if isinstance(node, dict):
            new_dict = {}
            memo[nid] = new_dict
            for k, v in node.items():
                new_dict[_copy(k)] = _copy(v)
            return new_dict
        return node
    return _copy(root)
```

`id()` унікальний і сталий, поки об’єкт живий, а оригінальний граф живий під час копіювання, тож ключі не збігаються для різних вузлів.[^py314-library-functions-id] Код копіює лише `list` і `dict`; інші об’єкти, наприклад `tuple`, повертаються як є і лишаються спільними з оригіналом.

## Detailed explanation

Копіювання графа має дві вимоги: спільний вузол має скопіюватися один раз, а цикл не має призвести до нескінченної рекурсії. Наївна рекурсія не виконує жодної з них. Вона створює окрему копію для кожного посилання, а структура, що містить сама себе, викликає рекурсію без кінця. Модуль `copy` прямо описує цю проблему: рекурсивні об’єкти можуть спричинити рекурсивний цикл, а `deepcopy()` її уникає, зберігаючи memo dictionary вже скопійованих об’єктів поточного проходу.[^py314-library-copy]

Наївний варіант без memo на циклі падає:

```python
def naive_copy(node):
    if isinstance(node, list):
        return [naive_copy(item) for item in node]
    return node


cycle = [1]
cycle.append(cycle)
try:
    naive_copy(cycle)
except RecursionError as error:
    print(type(error).__name__)  # RecursionError: nothing stops the recursion
```

Порядок у memo-коді важливий. `memo[nid]` записується до рекурсивного спуску: порожній `new_list` кладеться в memo і лише потім заповнюється через `extend`. Коли спуск доходить назад до того самого вузла, функція повертає вже існуючу, ще неповну копію і не починає нову рекурсію. Для `dict` порядок той самий: спочатку `new_dict` записується в memo, потім копіюються ключі й значення. Якщо записати memo після спуску, цикл знову дає `RecursionError`.

Ключ береться з `id(node)`, а не з вмісту. `id()` унікальний для живих об’єктів, тому два різні списки з однаковими значеннями, наприклад `[1]` і `[1]`, не зливаються в одну копію.[^py314-library-functions-id]

Межі цього коду: він копіює лише `list` і `dict`. Інші типи повертаються без змін, тож після `deep_copy_graph({"t": t})["t"] is t` для `t = ("x", ["inner"])` отримуємо `True`: tuple і список всередині нього лишаються спільними з оригіналом. Це випливає з самого коду, який повертає без змін усе, крім `list` і `dict`. Для `copy.deepcopy` та сама перевірка (`copy.deepcopy(t) is t`) дає `False`; документація цього прямо не каже, тож це спостереження на 3.13 і 3.14. Щоб закрити прогалину, треба обробити всі типи-контейнери або дати класам власний `__deepcopy__`: модуль `copy` дозволяє користувацьким класам перевизначати копіювання.[^py314-library-copy]

**Типові помилки:**
- записувати memo після рекурсивного спуску: на циклі виникає `RecursionError`;
- використовувати ключ за вмістом, наприклад `repr(node)`, замість `id()`: різні, але рівні списки зливаються в одну копію;
- вважати, що `tuple` або власні об’єкти копіюються разом із контейнерами: вони лишаються спільними з оригіналом.
