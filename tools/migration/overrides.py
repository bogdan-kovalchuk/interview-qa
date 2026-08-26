"""Hand-made classification decisions for the M4 predecessor migration.

Every table here is a judgement call the automatic converter (`migrate_legacy.py`)
cannot make from the legacy tags alone. Keeping them here, next to the code that
consumes them, is the audit trail for *why* a card ended up the way it did -
see the migration report for the reasoning behind each table.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# 1. topic file -> (track, section) for the 20 python-native decks (1:1 with
#    meta/TAXONOMY.md's python/ tree - tag-mapping.md does not move these).
# ---------------------------------------------------------------------------
TOPIC_FILE_SECTION: dict[str, tuple[str, str]] = {
    "01_python_fundamentals": ("python", "fundamentals"),
    "02_syntax_control_flow": ("python", "syntax-and-control-flow"),
    "03_objects_types_mutability": ("python", "objects-and-types"),
    "04_collections": ("python", "collections"),
    "05_functions_scope_closures": ("python", "functions-and-scope"),
    "06_oop_data_model": ("python", "oop-and-data-model"),
    "07_decorators": ("python", "decorators"),
    "08_iterators_generators": ("python", "iterators-and-generators"),
    "09_context_managers": ("python", "context-managers"),
    "10_exceptions": ("python", "exceptions"),
    "11_modules_packages_imports": ("python", "modules-and-imports"),
    "12_files_io": ("python", "files-and-io"),
    "13_comprehensions_functional": ("python", "comprehensions-and-functional"),
    "14_cpython_internals_memory": ("python", "cpython-internals"),
    "15_gil_threads_processes": ("python", "concurrency-and-gil"),
    "16_asyncio": ("python", "asyncio"),
    "17_standard_library": ("python", "standard-library"),
    "18_testing": ("python", "testing"),
    "19_performance_best_practices": ("python", "performance"),
    "20_practical_coding": ("python", "practical-coding"),
    # 21-23 move tracks per tag-mapping.md; every card in these three files
    # gets an explicit per-card section below instead of a file-level default.
}

# Section prefixes already reserved by the nine pilots (do not reassign).
EXISTING_PREFIXES = {
    "cs/complexity-and-analysis": "cmplx",
    "python/concurrency-and-gil": "gil",
    "python/practical-coding": "prac",
    "cpp/pointers-and-references": "ptrref",
    "cpp/tooling-and-diagnostics": "tooling",
    "databases/orm-and-persistence": "orm",
    "system-design/messaging-and-queues": "msgq",
    "behavioral/teamwork-and-conflict": "team",
    "engineering/version-control": "vcs",
}

# New section prefixes this migration introduces. 3-8 lowercase letters,
# validated by facets-vocabulary; recorded once in meta/vocabulary.yml.
NEW_PREFIXES: dict[str, str] = {
    "python/fundamentals": "fund",
    "python/syntax-and-control-flow": "syntax",
    "python/objects-and-types": "objtypes",
    "python/collections": "coll",
    "python/functions-and-scope": "funcs",
    "python/oop-and-data-model": "oop",
    "python/decorators": "decor",
    "python/iterators-and-generators": "itergen",
    "python/context-managers": "ctxmgr",
    "python/exceptions": "excpt",
    "python/modules-and-imports": "modimp",
    "python/files-and-io": "fileio",
    "python/comprehensions-and-functional": "compfn",
    "python/cpython-internals": "cpyint",
    "python/asyncio": "async",
    "python/standard-library": "stdlib",
    "python/testing": "testing",
    "python/performance": "perf",
    "cs/algorithms": "algo",
    "cs/data-structures": "dstruct",
    "databases/indexing-and-query-plans": "idxplan",
    "databases/sql-queries": "sqlq",
    "databases/transactions-and-isolation": "txiso",
    "databases/relational-model": "relmod",
    "engineering/ci-cd": "cicd",
    "engineering/code-quality": "codeq",
}

# English/Ukrainian navigation labels for the sections NEW_PREFIXES introduces.
NEW_SECTION_LABELS: dict[str, dict[str, str]] = {
    "python/fundamentals": {"en": "Fundamentals", "uk": "Основи"},
    "python/syntax-and-control-flow": {"en": "Syntax and control flow", "uk": "Синтаксис і потік керування"},
    "python/objects-and-types": {"en": "Objects and types", "uk": "Об'єкти і типи"},
    "python/collections": {"en": "Collections", "uk": "Колекції"},
    "python/functions-and-scope": {"en": "Functions and scope", "uk": "Функції та область видимості"},
    "python/oop-and-data-model": {"en": "OOP and data model", "uk": "ООП і модель даних"},
    "python/decorators": {"en": "Decorators", "uk": "Декоратори"},
    "python/iterators-and-generators": {"en": "Iterators and generators", "uk": "Ітератори та генератори"},
    "python/context-managers": {"en": "Context managers", "uk": "Контекстні менеджери"},
    "python/exceptions": {"en": "Exceptions", "uk": "Винятки"},
    "python/modules-and-imports": {"en": "Modules and imports", "uk": "Модулі та імпорти"},
    "python/files-and-io": {"en": "Files and I/O", "uk": "Файли та ввід-вивід"},
    "python/comprehensions-and-functional": {"en": "Comprehensions and functional", "uk": "Comprehensions і функціональний стиль"},
    "python/cpython-internals": {"en": "CPython internals", "uk": "Внутрішній устрій CPython"},
    "python/asyncio": {"en": "Asyncio", "uk": "Asyncio"},
    "python/standard-library": {"en": "Standard library", "uk": "Стандартна бібліотека"},
    "python/testing": {"en": "Testing", "uk": "Тестування"},
    "python/performance": {"en": "Performance", "uk": "Продуктивність"},
    "cs/algorithms": {"en": "Algorithms", "uk": "Алгоритми"},
    "cs/data-structures": {"en": "Data structures", "uk": "Структури даних"},
    "databases/indexing-and-query-plans": {"en": "Indexing and query plans", "uk": "Індексація та плани запитів"},
    "databases/sql-queries": {"en": "SQL queries", "uk": "SQL-запити"},
    "databases/transactions-and-isolation": {"en": "Transactions and isolation", "uk": "Транзакції та ізоляція"},
    "databases/relational-model": {"en": "Relational model", "uk": "Реляційна модель"},
    "engineering/ci-cd": {"en": "CI/CD", "uk": "CI/CD"},
    "engineering/code-quality": {"en": "Code quality", "uk": "Якість коду"},
}

# ---------------------------------------------------------------------------
# 2. Per-card (track, section) override for the 21 cards that move out of
#    python/ per tag-mapping.md ("21/22/23 move to cs, databases, engineering").
#    Reasoning is in the migration report; kept short here.
# ---------------------------------------------------------------------------
SECTION_OVERRIDE: dict[str, tuple[str, str]] = {
    # 21_algorithms_data_structures -> cs/
    "PYI_21_001": ("cs", "complexity-and-analysis"),  # nested-loop O(n^2)
    "PYI_21_002": ("cs", "complexity-and-analysis"),  # Big O drops constants
    "PYI_21_003": ("cs", "data-structures"),          # hash table vs min-heap
    "PYI_21_004": ("cs", "data-structures"),          # deque vs list
    "PYI_21_005": ("cs", "algorithms"),                # binary search preconditions
    "PYI_21_006": ("cs", "algorithms"),                # BFS vs DFS
    "PYI_21_007": ("cs", "algorithms"),                # memoization / DP
    # 22_databases_sql -> databases/
    "PYI_22_001": ("databases", "indexing-and-query-plans"),  # index trade-off
    "PYI_22_002": ("databases", "sql-queries"),                # LEFT JOIN
    "PYI_22_003": ("databases", "transactions-and-isolation"),  # ACID atomicity
    "PYI_22_004": ("databases", "transactions-and-isolation"),  # isolation levels
    "PYI_22_005": ("databases", "relational-model"),            # constraints/integrity
    "PYI_22_006": ("databases", "sql-queries"),                 # parameterized SQL
    "PYI_22_007": ("databases", "indexing-and-query-plans"),    # keyset vs offset pagination
    # 23_git_cicd_sdlc -> engineering/
    "PYI_23_001": ("engineering", "version-control"),  # merge vs rebase
    "PYI_23_002": ("engineering", "version-control"),  # rebase safety
    "PYI_23_003": ("engineering", "version-control"),  # revert/reset/reflog
    "PYI_23_004": ("engineering", "ci-cd"),             # CI gate selection
    "PYI_23_005": ("engineering", "ci-cd"),             # deployment strategies
    "PYI_23_006": ("engineering", "ci-cd"),             # CI feedback loop
    "PYI_23_007": ("engineering", "code-quality"),      # review judgement
}

# ---------------------------------------------------------------------------
# 3. type::Code (28 cards) reclassification - tag-mapping.md #4.
#
# The old `Code` tag meant "predict the output of this snippet", which is a
# `mechanism` or `pitfall` shape, not the new `coding` (which needs a real
# Task/Solution/Tests). 15 of the 28 are that predict-the-output shape and
# are reclassified straight to mechanism/pitfall with no Anki impact.
#
# The other 13, all in 20_practical_coding, literally say "Implement X" /
# "Design X" and are genuinely coding-shaped questions - but this migration
# does not author Task/Constraints/Solution/Tests for them (that would be
# inventing content, not converting it). They keep type `coding` and are
# reported with `anki.export: false` so the unwritten Task never reaches a
# shipped Front (see CODING_EXPORT_FALSE below).
# ---------------------------------------------------------------------------
TYPE_OVERRIDE: dict[str, str] = {
    # --- predict-the-output Code cards -> mechanism ---
    "PYI_02_002": "mechanism",  # `[] or "fallback"` -> short-circuit or
    "PYI_02_013": "mechanism",  # `-3 ** 2` operator precedence
    "PYI_05_004": "mechanism",  # *args/**kwargs binding
    "PYI_07_002": "mechanism",  # decorator stacking order
    "PYI_21_001": "mechanism",  # nested-loop complexity
    "PYI_20_001": "mechanism",  # short-circuit `and`, no side effect
    # --- predict-the-output Code cards -> pitfall (starts from a surprise/bug) ---
    "PYI_03_016": "pitfall",  # 1 / 1.0 / True collapse to one dict key
    "PYI_04_005": "pitfall",  # tuple mutates before TypeError
    "PYI_05_006": "pitfall",  # mutable default argument
    "PYI_05_016": "pitfall",  # late-binding closures in a loop
    "PYI_07_012": "pitfall",  # decorator returns None
    "PYI_10_005": "pitfall",  # return-in-finally overrides try
    "PYI_20_002": "pitfall",  # shallow copy aliasing bug
    "PYI_20_003": "pitfall",  # match/case capture leaks to scope
    "PYI_20_004": "pitfall",  # unhashable type (__eq__ without __hash__)
    # --- genuinely "implement X" Code cards -> stay `coding`, export disabled ---
    "PYI_20_005": "coding",
    "PYI_20_006": "coding",
    "PYI_20_007": "coding",
    "PYI_20_009": "coding",
    "PYI_20_011": "coding",
    "PYI_20_012": "coding",
    "PYI_20_013": "coding",
    "PYI_20_014": "coding",
    "PYI_20_015": "coding",
    "PYI_20_016": "coding",
    "PYI_20_018": "coding",
    "PYI_20_019": "coding",
    "PYI_20_020": "coding",

    # --- type::Scenario -> comparison override (the content genuinely weighs
    # two or more named alternatives against each other; everything else in
    # type::Scenario defaults to `practical` per tag-mapping.md / PLAN.md). ---
    "PYI_01_008": "comparison",
    "PYI_01_011": "comparison",
    "PYI_03_011": "comparison",
    "PYI_03_015": "comparison",
    "PYI_03_018": "comparison",
    "PYI_03_021": "comparison",
    "PYI_04_001": "comparison",
    "PYI_04_004": "comparison",
    "PYI_04_009": "comparison",
    "PYI_04_013": "comparison",
    "PYI_04_021": "comparison",
    "PYI_04_023": "comparison",
    "PYI_05_008": "comparison",
    "PYI_05_021": "comparison",
    "PYI_05_022": "comparison",
    "PYI_06_011": "comparison",
    "PYI_06_014": "comparison",
    "PYI_06_025": "comparison",
    "PYI_06_030": "comparison",
    "PYI_07_007": "comparison",
    "PYI_08_016": "comparison",
    "PYI_09_006": "comparison",
    "PYI_10_001": "comparison",
    "PYI_10_014": "comparison",
    "PYI_10_015": "comparison",
    "PYI_11_006": "comparison",
    "PYI_13_010": "comparison",
    "PYI_15_017": "comparison",
    "PYI_15_018": "comparison",
    "PYI_15_020": "comparison",
    "PYI_15_021": "comparison",
    "PYI_15_022": "comparison",
    "PYI_16_022": "comparison",
    "PYI_17_001": "comparison",
    "PYI_17_004": "comparison",
    "PYI_17_011": "comparison",
    "PYI_17_013": "comparison",
    "PYI_17_014": "comparison",
    "PYI_17_016": "comparison",
    "PYI_17_018": "comparison",
    "PYI_18_008": "comparison",
    "PYI_18_010": "comparison",
    "PYI_18_016": "comparison",
    "PYI_19_006": "comparison",
    "PYI_19_008": "comparison",
    "PYI_21_003": "comparison",
    "PYI_21_004": "comparison",
    "PYI_22_007": "comparison",
    "PYI_23_003": "comparison",
    "PYI_23_005": "comparison",
}

# The 13 cards that keep type `coding` but ship no card (Task/Solution/Tests
# were never authored - writing them would be inventing content this
# migration was told not to invent). Reported explicitly in the M4 report.
CODING_EXPORT_FALSE: frozenset[str] = frozenset(
    {
        "PYI_20_005",
        "PYI_20_006",
        "PYI_20_007",
        "PYI_20_009",
        "PYI_20_011",
        "PYI_20_012",
        "PYI_20_013",
        "PYI_20_014",
        "PYI_20_015",
        "PYI_20_016",
        "PYI_20_018",
        "PYI_20_019",
        "PYI_20_020",
    }
)

# ---------------------------------------------------------------------------
# 4. 21_algorithms_data_structures.txt has English-language Back fields (a
#    predecessor authoring inconsistency - fronts are Ukrainian, backs are
#    not). The owner's instruction is "cards are Ukrainian only", so these 7
#    Short answers are hand-translated here instead of auto-converted from
#    the (English) legacy Back. Meaning is preserved 1:1 from the legacy text
#    (verified against tools/migration_work/extracted.json); nothing is
#    invented beyond restating the same claims in Ukrainian.
# ---------------------------------------------------------------------------
UK_SHORT_ANSWER_OVERRIDE: dict[str, str] = {
    "PYI_21_001": (
        "**Часова складність – O(n²), що пояснюється трикутною сумою "
        "0 + 1 + 2 + ... + (n-1) = n(n-1)/2.** Внутрішній цикл виконується `i` разів "
        "для кожного `i` від 0 до n-1, що в сумі дає n(n-1)/2 викликів `work()`. "
        "Перевірено на Python 3.14: n=10 -> 45 викликів, n=100 -> 4950 викликів. "
        "Сталий множник 1/2 відкидається в Big O нотації."
    ),
    "PYI_21_002": (
        "**Big O описує швидкість зростання при n -> нескінченність, коли домінантний "
        "член переважає над константами й доданками нижчого порядку.** Наприклад, "
        "3n² + 5n + 100 спрощується до O(n²), бо для великих n домінує квадратичний "
        "член. Однак для реальних скінченних input constant factor і доданки нижчого "
        "порядку визначають фактичний час виконання – алгоритм O(n²) з малою "
        "константою може випереджати O(n log n) на практичних значеннях n."
    ),
    "PYI_21_003": (
        "**`dict` дає O(1) середню складність пошуку за ключем; min-heap на основі "
        "`heapq` дає O(log n) для push/pop і O(1) для перегляду найменшого елемента.** "
        "Обирайте hash table, коли основна операція – пошук або оновлення job за "
        "унікальним ID. Обирайте min-heap, коли потрібно постійно вилучати job з "
        "найменшим priority – heap не підтримує O(1) довільний пошук за ID."
    ),
    "PYI_21_004": (
        "**`deque` дає O(1) для append і pop з обох кінців, тоді як `list` коштує "
        "O(n) для `pop(0)` або `insert(0, v)`, бо елементи доводиться зсувати в "
        "пам'яті.** Для FIFO-черги або sliding-window алгоритму, що додає/видаляє "
        "елементи на початку, `collections.deque` уникає цієї лінійної вартості. "
        "Використовуйте `list`, коли append/pop потрібні лише в кінці (стек) або "
        "потрібен O(1) доступ за індексом."
    ),
    "PYI_21_005": (
        "**Binary search вимагає відсортованої послідовності; `bisect` знаходить "
        "позицію вставки за O(log n), але `list.insert()` зсуває елементи за O(n).** "
        "Передумова – відсортований input: `bisect_left` і `bisect_right` "
        "покладаються на порядок за `__lt__`. Навіть якщо сам пошук логарифмічний, "
        "вставка в `list` усе одно потребує зсуву до n елементів, тому сумарна "
        "вартість вставки – O(n)."
    ),
    "PYI_21_006": (
        "**BFS обходить граф рівень за рівнем через queue і знаходить найкоротший "
        "шлях у неважених графах; DFS йде вглиб через stack і використовує менше "
        "пам'яті на широких графах.** Обирайте BFS, коли потрібен найкоротший шлях "
        "або обхід за рівнями. Обирайте DFS для topological sorting, виявлення "
        "циклів або коли ціль глибоко, а граф широкий – пам'ять DFS становить "
        "O(depth) проти O(width) у BFS."
    ),
    "PYI_21_007": (
        "**Мемоїзація або bottom-up DP зводить рекурсію з експоненційним часом і "
        "overlapping subproblems до поліноміального часу, розв'язуючи кожен "
        "унікальний subproblem лише один раз.** Наприклад, наївний рекурсивний "
        "Fibonacci має складність O(2^n), але з таблицею memo кожен з n subproblems "
        "обчислюється один раз – це дає O(n) часу і O(n) пам'яті. Компроміс – "
        "додаткова пам'ять під кеш замість повторних обчислень."
    ),
}

# ---------------------------------------------------------------------------
# 5. The over-length legacy answers, trimmed to <=5 sentences.
#
# Measured with a sentence splitter that (unlike the shipped validator) does
# not undercount a sentence starting with inline code, and that correctly
# excludes the `<div class="source">` block (source text is not prose and
# was never meant to be counted as an answer sentence). Under that count,
# 4 of the 392 converted answers ran to 6 sentences; none reached higher.
# The trim always merges same-shape enumeration sentences with semicolons -
# every fact each sentence stated is still present, only the sentence
# boundary is removed.
# ---------------------------------------------------------------------------
SHORT_ANSWER_TRIM_OVERRIDE: dict[str, str] = {
    "PYI_18_003": (
        "**Баланс визначається test pyramid: багато швидких unit-тестів, помірна "
        "кількість integration і мінімум e2e-тестів.** Unit-тести дають найшвидший "
        "feedback і найменший maintenance cost, але нижчу fidelity; integration-тести "
        "дорожчі й повільніші, проте перевіряють реальні контракти між компонентами; "
        "e2e-тести мають найвищу fidelity, але найповільніші й найдорожчі. "
        '<span class="warn">Інверсія піраміди (багато e2e, мало unit) призводить до '
        "повільного CI та flaky-тестів.</span> Ризик-орієнтований підхід: критичні "
        "шляхи (payment, auth) потребують більше integration/e2e, тоді як "
        "бізнес-логіка покривається unit-тестами."
    ),
    "PYI_19_003": (
        "**Кожен із цих факторів робить замір систематично відмінним від «чистої» "
        "продуктивності коду: перший замір включає імпорт та заповнення кешів, "
        "OS-контекст змінює доступний CPU, а нерепрезентативні вхідні дані приховують "
        "реальний розподіл навантаження.** Warm-up дає повільніші перші ітерації через "
        "завантаження модулів і заповнення кешів процесора; caching (`lru_cache`, "
        "інтернування рядків) робить повторні виклики штучно швидшими; system load від "
        "фонових процесів і планувальника ОС додає варіативність; а input distribution "
        "синтетичних даних може не покривати worst case. "
        '<span class="warn">Порада: робити warm-up прогін, використовувати `timeit` з '
        "`repeat` і брати `min()`, тестувати на різних розподілах вхідних даних.</span>"
    ),
    "PYI_19_006": (
        "**Кожен контейнер оптимізований під певний набір операцій, і неправильний "
        "вибір перетворює O(1) на O(n) на гарячих шляхах.** `list` дає O(1) для "
        "індексації й append, але O(n) для пошуку та вставки в середину; `set`/`dict` "
        "дають O(1) для перевірки належності та видалення в середньому, але O(n) у "
        "гіршому випадку; `deque` дає O(1) append/pop з обох кінців; heap (`heapq`) "
        "дає O(log n) push/pop і O(1) для min/max. "
        '<span class="warn">Якщо dominant operation – membership test, `list` замість '
        "`set` дає O(n) замість O(1).</span>"
    ),
    "PYI_22_005": (
        "**Constraints декларують правила валідації безпосередньо в схемі БД, і СУБД "
        "застосовує їх автоматично при кожній операції `INSERT`/`UPDATE`/`DELETE`, "
        "незалежно від application code.** `PRIMARY KEY` гарантує унікальність і NOT "
        "NULL; `FOREIGN KEY` забезпечує referential integrity відносно значення в "
        "іншій таблиці; `UNIQUE` запобігає дублікатам; а `CHECK` валідує довільну "
        "Boolean-умову, наприклад `price > 0`. Це означає, що навіть якщо application "
        "code має баг або обходить валідацію, БД не допустить некоректних даних."
    ),
}

# ---------------------------------------------------------------------------
# 6. `short-answer-limits` sentence-count workaround.
#
# `tools/iqa/validate.py::_sentence_count` strips backticks/underscores before
# looking for a sentence boundary, then requires the character right after the
# boundary to be uppercase (or a digit). A legacy sentence that starts with an
# inline-code term - `` `deque` кращий... ``, `` `frozen=True` додає... `` - has
# its code term reduced to a lowercase word by that same stripping step, so
# the boundary in front of it is never recognised and the sentence silently
# merges into the previous one. For most of the 392 cards this only makes an
# already-in-range count smaller (harmless); for these 9 it collapses a
# genuine 2-3 sentence answer down to 1, which trips the real `2 <= count <=
# 5` gate. The fix is minimal and meaning-preserving: a short capitalized
# lead-in word restores a real sentence start in front of the code term -
# nothing is added to the claims themselves.
# ---------------------------------------------------------------------------
SHORT_ANSWER_BOUNDARY_FIX: dict[str, str] = {
    "PYI_04_008": (
        "**`d[key]` викликає `KeyError`; `d.get(key)` повертає `None` (або переданий "
        "default) без побічних ефектів; `d.setdefault(key, default)` вставляє "
        "`default` у словник, якщо ключ відсутній, і повертає його.** Метод "
        '<span class="warn">`setdefault()` завжди обчислює аргумент `default`, навіть '
        "коли ключ існує – це може бути небажаним side effect, якщо створення default "
        "дороге.</span>"
    ),
    "PYI_04_023": (
        "**`deque` гарантує O(1) append і pop з обох кінців, тоді як `list` вимагає "
        "O(n) для `insert(0, v)` та `pop(0)` через зсув елементів у масиві.** Тому "
        "`deque` кращий для черг, ковзних вікон та алгоритмів, де потрібна ефективна "
        'робота з обома кінцями. <span class="warn">Водночас `deque` має O(n) доступ '
        "до середини за індексом, тому для random access list залишається "
        "кращим.</span>"
    ),
    "PYI_05_013": (
        "**`global` прив'язує ім'я до namespace модуля (top-level), а `nonlocal` – до "
        "найближчого enclosing function scope, не включаючи модуль.** При цьому "
        "`nonlocal` шукає binding лише у функціях-обгортках; якщо такого binding "
        "немає, виникає `SyntaxError`. Натомість `global` завжди посилається на "
        "модульний рівень, навіть якщо ім'я визначено у вкладеній функції."
    ),
    "PYI_06_027": (
        "**`eq=True` (default) генерує `__eq__`; `frozen=True` з `eq=True` генерує "
        "`__hash__`; `frozen=False` з `eq=True` встановлює `__hash__ = None` "
        "(unhashable); `eq=False` залишає `__hash__` від superclass; "
        "`unsafe_hash=True` примусово генерує `__hash__`.** Крім того, `frozen=True` "
        "додає `__setattr__`/`__delattr__`, що викликають `FrozenInstanceError`, "
        "емулюючи immutable instances. А `unsafe_hash=True` використовується, коли "
        "клас логічно immutable, але може бути mutable."
    ),
    "PYI_16_013": (
        "**`wait()` повертає два множества `(done, pending)` і підходить для "
        "контролю через `return_when`; `as_completed()` повертає ітератор "
        "результатів у порядку завершення – зручний для потокової обробки.** При "
        "цьому `wait()` не скасовує pending tasks при timeout і приймає лише "
        "Task/Future (не coroutine). А `as_completed()` теж не скасовує tasks при "
        "зупинці ітерації, але дає результати одразу в порядку готовності, що краще "
        "для прогрес-барів або early-exit сценаріїв."
    ),
    "PYI_20_009": (
        "**Параметризований decorator: зовнішня функція приймає `max_attempts` і "
        "`exceptions`, внутрішня – `functools.wraps` для збереження metadata, цикл з "
        "`try/except` і `raise` на останній спробі.**\n\n"
        "```python\n"
        "import functools\n\n"
        "def retry(max_attempts, exceptions):\n"
        "    def decorator(func):\n"
        "        @functools.wraps(func)\n"
        "        def wrapper(*args, **kwargs):\n"
        "            for attempt in range(1, max_attempts + 1):\n"
        "                try:\n"
        "                    return func(*args, **kwargs)\n"
        "                except exceptions:\n"
        "                    if attempt == max_attempts:\n"
        "                        raise\n"
        "        return wrapper\n"
        "    return decorator\n"
        "```\n\n"
        "Тут `except exceptions` працює з tuple типів; bare `raise` на останній "
        "спробі зберігає оригінальний traceback. А `functools.wraps` копіює "
        "`__name__`, `__doc__` та інші атрибути."
    ),
    "PYI_20_016": (
        "**`functools.wraps` копіює metadata (`__name__`, `__doc__`, `__wrapped__`), "
        "`time.perf_counter()` для high-resolution elapsed time, return value "
        "передається через `return result`, exception propagation гарантується "
        "відсутністю `try/except` що ловить помилки.** Тут "
        '<span class="warn">`time.time()` має нижчу точність та чутливий до system '
        "clock changes; `time.perf_counter()` є monotonic та має найвищу доступну "
        "точність.</span>\n\n"
        "```python\n"
        "import time\n"
        "import functools\n\n"
        "def timed(func):\n"
        "    @functools.wraps(func)\n"
        "    def wrapper(*args, **kwargs):\n"
        "        start = time.perf_counter()\n"
        "        try:\n"
        "            result = func(*args, **kwargs)\n"
        "            return result\n"
        "        finally:\n"
        "            elapsed = time.perf_counter() - start\n"
        "            wrapper.last_elapsed = elapsed\n"
        "    wrapper.last_elapsed = None\n"
        "    return wrapper\n\n"
        "@timed\n"
        "def slow_add(a, b):\n"
        "    time.sleep(0.01)\n"
        "    return a + b\n\n"
        "slow_add(1, 2)  # 3\n"
        "slow_add.__name__  # 'slow_add'\n"
        "```"
    ),
    "PYI_20_018": (
        "**`__exit__` перевіряє `exc_type is None` для commit, інакше rollback; "
        "`return False` (або неявний `None`) не приховує exception – він propagate "
        'далі.** Водночас <span class="warn">`return True` з `__exit__` приховує '
        "exception – це небезпечно для transaction semantics, бо caller не "
        "дізнається про failure.</span>\n\n"
        "```python\n"
        "class Transaction:\n"
        "    def __init__(self, name):\n"
        "        self.name = name\n"
        "        self.committed = False\n"
        "        self.rolled_back = False\n\n"
        "    def __enter__(self):\n"
        "        return self\n\n"
        "    def __exit__(self, exc_type, exc_val, exc_tb):\n"
        "        if exc_type is None:\n"
        "            self.committed = True\n"
        "        else:\n"
        "            self.rolled_back = True\n"
        "        return False  # do not suppress exception\n\n"
        "t = Transaction(\"tx1\")\n"
        "with t:\n"
        "    pass\n"
        "t.committed  # True\n"
        "```"
    ),
    "PYI_06_001": (
        "**`__new__` створює та повертає новий instance, тоді як `__init__` лише "
        "ініціалізує вже створений instance і не повинен повертати значення.** Сам "
        "`__new__` – неявний staticmethod, який отримує `cls` і повертає об'єкт "
        "(зазвичай instance `cls`). А `__init__` отримує готовий `self`, налаштовує "
        "його атрибути і має повертати `None`."
    ),
    "PYI_06_014": (
        "**Instance method – коли потрібен доступ до стану конкретного об'єкта; "
        "`@classmethod` – коли потрібен доступ до класу з підтримкою polymorphism; "
        "`@staticmethod` – коли метод не залежить ні від instance, ні від класу.** "
        "Тут `@classmethod` отримує підклас як `cls`, тому factory-методи коректно "
        "працюють при успадкуванні (повертають екземпляр підкласу). А "
        "`@staticmethod` не отримує жодного implicit аргументу і фактично є "
        "звичайною функцією, розміщеною в namespace класу; polymorphism для нього "
        "неможливий."
    ),
}
