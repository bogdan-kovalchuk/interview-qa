# Таксономія: треки, секції, назви

Пропозиція повного дерева контенту. Кожен рядок – це і назва теки, і сегмент URL.
Правила іменування і правило вибору домівки – у `meta/QUESTIONS.md` §2.

Легенда пріоритету:
- **P0** – запускаємо першим (уже є контент або він критичний);
- **P1** – друга хвиля;
- **P2** – коли з'явиться попит.

---

## 0. Верхній рівень

```
content/{en,uk}/
  index.md                     Головна
  start-here/                  Як користуватись, як учитись, як контриб'ютити   P0
  languages/…                  ↯ НЕ використовуємо: треки лежать плоско в корені
  python/                      P0   мовне ядро
  cpp/                         P0   мовне ядро (C + C++)
  cs/                          P0   computer science fundamentals
  systems/                     P1   ОС, пам'ять, процеси, мережі
  databases/                   P1
  engineering/                 P0   git, тести, CI/CD, code review, SDLC
  system-design/               P1
  embedded/                    P1   доменний трек
  data-science/                P1   доменний трек
  machine-learning/            P2   доменний трек
  data-engineering/            P2   доменний трек
  backend/                     P1   доменний трек
  devops/                      P2   доменний трек
  qa-automation/               P2   доменний трек
  behavioral/                  P1   soft skills та процес інтерв'ю
  programs/                    ⚙ генерується з programs/*.yml
  collections/                 ⚙ генеровані зрізи: by-level, tags, frameworks
  q/                           ⚙ генеровані permalink-редіректи
```

**Чому треки лежать плоско, а не під `languages/` і `specializations/`.**
URL-и потрапляють у тисячі карток Anki, тому кожен зайвий сегмент – це вічний борг:
`/uk/cpp/templates/sfinae/` замість `/uk/languages/cpp/templates/sfinae/`.
Групування «Мови / Фундамент / Спеціалізації / Процес» робиться **в сайдбарі**, а не в URL:
Starlight дозволяє описати групи навігації незалежно від структури тек.

Сайдбар (окремо від URL):

```
Languages          → python, cpp
Foundations        → cs, systems, databases
Specializations    → embedded, data-science, machine-learning,
                     data-engineering, backend, devops, qa-automation
Engineering        → engineering, system-design
Interview          → behavioral, start-here
Paths              → programs (генеровані)
```

---

## 1. `python/` – P0

Базується на наявних 23 темах Anki-репозиторію, з нормалізацією назв і закриттям прогалин.

```
python/
  fundamentals/                 модель виконання, bytecode, CPython vs інші рантайми
  syntax-and-control-flow/
  objects-and-types/            id, type, mutability, truthiness
  collections/                  list, tuple, dict, set, deque, namedtuple
  strings-and-text/             ★ нове: encoding, str vs bytes, f-strings, normalization
  functions-and-scope/          аргументи, замикання, LEGB
  oop-and-data-model/           dunder, MRO, descriptors, dataclasses, slots
  typing-and-annotations/       ★ нове: typing, Protocol, Generic, mypy/pyright
  decorators/
  iterators-and-generators/
  context-managers/
  exceptions/
  modules-and-imports/          import system, packages, циклічні імпорти
  packaging-and-environments/   ★ нове: venv, pip, uv, pyproject, wheels, версіонування
  files-and-io/
  comprehensions-and-functional/
  cpython-internals/            refcount, GC, memory arenas, інтернування
  concurrency-and-gil/          threads, processes, GIL, free-threaded build
  asyncio/
  standard-library/
  testing/                      pytest, fixtures, mocks, parametrize
  performance/                  профілювання, оптимізація, C-розширення
  practical-coding/             задачі «напиши код» на інтерв'ю
  frameworks/                   ⚠ тільки Python-специфічні, не веб (веб → backend/)
    pydantic/
```

★ – прогалини, знайдені при звірці з наявною таксономією 23 тем.

**Що переїжджає з наявного репозиторію в інші треки:**

| Наявна тема | Нова домівка |
|---|---|
| `21_algorithms_data_structures` | `cs/algorithms/` + `cs/data-structures/` |
| `22_databases_sql` | `databases/` |
| `23_git_cicd_sdlc` | `engineering/version-control/` + `engineering/ci-cd/` + `engineering/sdlc/` |

---

## 2. `cpp/` – P0

C і C++ в одному треку: на інтерв'ю вони майже завжди йдуть парою, а C-специфіка виноситься в окрему секцію.

```
cpp/
  c-core/                       C-специфіка: масиви vs вказівники, UB, препроцесор, C-рядки
  language-basics/              declaration vs definition, storage duration, const-correctness
  types-and-conversions/        integral promotion, narrowing, cast-и, strict aliasing
  pointers-and-references/      raw/smart pointers, ownership, dangling
  memory-model-and-lifetime/    stack/heap, RAII, alignment, placement new
  move-semantics/               rvalue, perfect forwarding, copy elision, rule of 0/3/5
  oop-and-polymorphism/         vtable, slicing, віртуальні деструктори, множинне успадкування
  templates-and-generics/       SFINAE, concepts, CRTP, variadic, спеціалізація
  stl-containers/               складність, інвалідація ітераторів, allocator
  stl-algorithms-and-ranges/
  exceptions-and-error-handling/  noexcept, exception safety, коди помилок, expected
  concurrency-and-memory-model/   std::thread, atomic, memory_order, data race vs race condition
  compilation-and-linking/      TU, ODR, ABI, inline, статичні/динамічні бібліотеки, modules
  build-systems/                CMake, залежності, крос-компіляція
  tooling-and-diagnostics/      sanitizers, valgrind, gdb, perf, static analysis
  idioms-and-patterns/          pimpl, type erasure, RAII-guard, tag dispatch
  performance/                  cache locality, branch prediction, inlining, аллокації
  standards-evolution/          C++11/14/17/20/23/26 – що змінилось і чому питають
  practical-coding/
  frameworks/
    qt/
    boost/
```

---

## 3. `cs/` – P0

```
cs/
  complexity-and-analysis/      O-нотація, амортизація, trade-off пам'ять/час
  data-structures/              масиви, списки, дерева, купи, графи, хеш-таблиці, trie
  algorithms/                   сортування, пошук, обхід графів, DP, greedy, two pointers
  problem-solving-patterns/     упізнавані шаблони задач на інтерв'ю
  math-for-programmers/         біти, модульна арифметика, комбінаторика
  automata-and-parsing/         P2
```

---

## 4. `systems/` – P1

```
systems/
  operating-systems/            процеси, потоки, планувальник, сигнали
  memory-management/            віртуальна пам'ять, сторінки, mmap, фрагментація
  filesystems-and-io/           буферизація, syscalls, блокуючий/неблокуючий IO
  concurrency-primitives/       м'ютекси, семафори, deadlock, lock-free
  networking/                   TCP/UDP, HTTP, TLS, DNS, сокети
  linux-and-shell/              інструменти діагностики, права, процеси
  security-basics/              P2
```

---

## 5. `databases/` – P1

```
databases/
  relational-model/             нормалізація, ключі, схеми
  sql-queries/                  join-и, віконні функції, агрегації
  indexing-and-query-plans/     B-tree, покриваючі індекси, EXPLAIN
  transactions-and-isolation/   ACID, рівні ізоляції, локи, MVCC
  postgresql/
  nosql/                        документні, key-value, колонкові, вибір моделі
  orm-and-persistence/          N+1, lazy/eager, міграції
  scaling-and-replication/      P2
```

---

## 6. `engineering/` – P0

```
engineering/
  version-control/              git: rebase vs merge, конфлікти, стратегії гілок
  testing/                      піраміда, unit/integration/e2e, TDD, coverage, flaky
  ci-cd/                        пайплайни, артефакти, стратегії деплою
  code-quality/                 code review, лінтери, метрики, технічний борг
  design-principles/            SOLID, DRY/KISS/YAGNI, coupling/cohesion
  design-patterns/              GoF з прикладами на Python і C++
  refactoring/                  P2
  sdlc-and-process/             agile/scrum, оцінювання, документація
  licensing-and-legal/          P2
```

---

## 7. `system-design/` – P1

```
system-design/
  fundamentals/                 latency vs throughput, CAP, консистентність
  api-design/                   REST, gRPC, версіонування, ідемпотентність
  caching/
  messaging-and-queues/
  storage-choices/
  observability/                логи, метрики, трейси, SLO
  case-studies/                 типові задачі дизайну на інтерв'ю
  embedded-system-design/       ★ дизайн для ресурсно-обмежених систем
```

---

## 8. `embedded/` – P1

Найдетальніший доменний трек, бо він найдалі стоїть від «звичайного» backend-контексту.

```
embedded/
  fundamentals/                 MCU vs MPU vs SoC, bare-metal vs RTOS vs Linux, крос-компіляція
  toolchain-and-build/          GCC/Clang для ARM, лінкер, флаги, розмір бінаря
  c-in-embedded/                volatile, const, бітові поля, фіксована точка, freestanding
  cpp-in-embedded/              чому вимикають exceptions/RTTI, constexpr, статична алокація
  memory-and-linker/            linker script, секції .text/.data/.bss, startup code, стек vs купа
  interrupts-and-timing/        ISR, латентність, пріоритети, критичні секції, WCET
  peripherals-and-buses/        GPIO, UART, SPI, I2C, CAN, USB, DMA, ADC
  rtos/                         планування, пріоритетна інверсія, черги, семафори
    freertos/
    zephyr/
  power-management/             режими сну, wake-up, бюджет енергії
  bootloaders-and-ota/          завантажники, оновлення прошивки, відкат, підпис
  debugging-and-tracing/        JTAG/SWD, gdb, логічний аналізатор, трасування
  testing-embedded/             HIL, симуляція, mock-и периферії, unit-тести без заліза
  safety-and-standards/         MISRA C/C++, IEC 61508, ISO 26262, DO-178C, AUTOSAR
  connectivity/                 BLE, Wi-Fi, LoRa, MQTT, Modbus
  hardware-basics/              для прошивників: рівні, підтяжки, живлення, осцилограма
  linux-embedded/               P2: Yocto, buildroot, device tree, драйвери
```

---

## 9. `data-science/`, `machine-learning/`, `data-engineering/` – P1/P2

Розділені навмисно: на ринку це три різні вакансії з різними питаннями.

```
data-science/
  statistics-and-probability/
  experimentation/              A/B-тести, p-value, потужність
  data-wrangling/               чистка, пропуски, типи
  exploratory-analysis/
  visualization/
  sql-for-analytics/            ⚠ базовий SQL живе в databases/; тут – аналітичні патерни
  frameworks/
    pandas/
    polars/
    numpy/                      канонічна домівка numpy – саме тут
    matplotlib/

machine-learning/
  ml-fundamentals/              bias/variance, регуляризація, крос-валідація
  classical-ml/                 лінійні моделі, дерева, ансамблі, кластеризація
  feature-engineering/
  model-evaluation/             метрики, витік даних, дисбаланс класів
  deep-learning/                архітектури, оптимізатори, регуляризація
  nlp/
  computer-vision/
  llm-and-genai/                промптинг, RAG, ембединги, evals, fine-tuning
  mlops/                        serving, версіонування моделей, дрейф, моніторинг
  frameworks/
    pytorch/
    scikit-learn/
    tensorflow/

data-engineering/
  pipelines-and-orchestration/  Airflow, DAG-и, ідемпотентність, backfill
  storage-and-formats/          Parquet, Avro, колонкові формати, партиціонування
  batch-processing/             Spark
  streaming/                    Kafka, вікна, exactly-once
  warehouse-modeling/           star schema, dbt, повільно змінювані виміри
  data-quality/
```

---

## 10. `backend/`, `devops/`, `qa-automation/` – P1/P2

```
backend/
  web-fundamentals/             HTTP, cookies, CORS, сесії
  authentication-and-authorization/   OAuth2, JWT, RBAC
  async-and-scaling/            воркери, черги, фонові задачі
  frameworks/
    django/
    fastapi/
    flask/
  security/                     OWASP, ін'єкції, секрети

devops/
  containers/                   Docker, образи, шари
  orchestration/                Kubernetes
  infrastructure-as-code/       Terraform, Ansible
  cloud-fundamentals/           AWS/GCP/Azure – базові поняття
  monitoring-and-incidents/     алерти, on-call, постмортем

qa-automation/
  test-design/                  еквівалентні класи, граничні значення
  ui-automation/                Selenium, Playwright
  api-testing/
  performance-testing/
  test-infrastructure/
```

---

## 11. `behavioral/` – P1

```
behavioral/
  interview-process/            етапи, формати, як готуватись, як ставити питання
  storytelling/                 STAR, як описувати проєкти
  teamwork-and-conflict/
  leadership-and-ownership/
  system-of-work/               оцінювання, пріоритизація, комунікація
  compensation-and-offers/      P2
```

---

## 12. Генеровані розділи

Не редагуються руками; походять з фасетів і `programs/`.

```
programs/{program-id}/          сторінка-шлях підготовки до конкретної ролі
collections/by-level/{level}/   junior | middle | senior
collections/tags/{tag}/
collections/frameworks/{name}/  всі питання з фасетом frameworks
q/{id}/                         permalink-редірект (по одному на мову)
```

---

## 13. Стартовий набір програм (`programs/*.yml`)

| id | Назва | Композиція (скорочено) |
|---|---|---|
| `python-backend-engineer` | Python Backend Engineer | python + backend + databases + engineering + system-design |
| `python-data-scientist` | Python Data Scientist | python (core) + data-science + machine-learning (fundamentals) + sql |
| `python-data-engineer` | Python Data Engineer | python + data-engineering + databases + systems |
| `cpp-systems-engineer` | C++ Systems Engineer | cpp + systems + cs + engineering |
| `embedded-cpp-engineer` | Embedded C++ Engineer | cpp (підмножина) + embedded + cs (біти, FSM) |
| `embedded-c-firmware-engineer` | Embedded C Firmware Engineer | cpp/c-core + embedded + hardware-basics |
| `ml-engineer` | ML Engineer | python + machine-learning + mlops + system-design |
| `qa-automation-python` | QA Automation (Python) | python + qa-automation + engineering/testing |

---

## 14. Оцінка обсягу

| Трек | Реалістична ціль питань |
|---|---|
| python | 400–600 |
| cpp | 350–500 |
| cs | 150–250 |
| embedded | 200–300 |
| data-science + ml + de | 300–450 |
| решта | 300–500 |
| **разом** | **~1800–2600** |

При 1 файл = 1 питання × 2 мови це ~4–5 тисяч файлів. Astro з content collections це витримує; це також аргумент проти ручної навігації в стилі референсу – навігація мусить генеруватись.
