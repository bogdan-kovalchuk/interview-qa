# Backlog review карток

Стан на 2026-09-08. Це єдиний постійний список незавершеного review письмових пар EN/UK.
Тимчасові звіти з `.audit-run-*` після перенесення сюди не є джерелом істини й видаляються.

Review пари вважається завершеним, коли перевірено обидві мови, фактичні твердження, точність і
доречність джерел, відповідність перекладу, кодові блоки та frontmatter. Виправлення мають зберегти
однаковий код у парі, підняти `content_revision`, синхронізувати `reconciled_with`, оновити `updated`
і пройти `python -m iqa validate`.

## Зведення

Письмовий `Detailed explanation` мають 185 пар. Стан review:

| Обсяг | Пар | Стан |
|---|---:|---|
| Python | 120 | Людський review ще не виконано |
| Embedded | 40 | Review виконано, усі 40 мають незакриті зауваження |
| Інші треки | 25 | 9 виправлено, 1 без зауважень, 15 мають незакриті зауваження |

## Python: review ще не виконано

Потрібно послідовно перевірити всі 120 письмових пар у таких секціях:

- `python/asyncio` - 24;
- `python/collections` - 22;
- `python/comprehensions-and-functional` - 5;
- `python/concurrency-and-gil` - 20;
- `python/context-managers` - 2;
- `python/cpython-internals` - 16;
- `python/decorators` - 4;
- `python/fundamentals` - 12;
- `python/practical-coding` - 1;
- `python/syntax-and-control-flow` - 14.

Попередній прохід лише перелічив тіла й виконав механічні пошуки. Він не створив підтверджених
висновків і не зараховується як review.

## Embedded: підтверджені незакриті зауваження

### Спільні для 40 пар

- Community-джерело `dou-embedded-interview` або `embeddedinterviewlab` використане як доказ
  фактичної відповіді, хоча перше лише перелічує питання, а друге веде на домашню сторінку.
  Зберегти запис як provenance, прибрати його citation-токен із фактичних тверджень і додати точне
  authoritative джерело.
- Усі 20 пар `embedded/memory-alignment-and-endianness` містять нерелевантний roadmap
  `https://acode.com.ua/end-cpp-what-is-next/` та додане заради нього рекламне речення. Прибрати
  джерело й речення, залишити точні ISO C, Arm, GCC або POSIX джерела.
- Прибрати нерелевантний `mcuboot-design` із `device-tree-describes-board-hardware`,
  `mcu-boot-sequence-vector-table-to-main` і `mcu-boot-sequence-reset-vector-to-main-scheduler`.
- Прибрати нерелевантний або невикористаний `gcc-overall-options` із CMake, duplicate-symbol,
  symbol-export, lifecycle, Makefile, static/dynamic library і merge/rebase карток. Для CMake,
  GNU make, ISO C/GCC inline, GNU ld/ELF, Microsoft PE/DLL і lifecycle додати точні первинні
  джерела. `gcc-overall-options` доречне лише для `-E`, `-S` і `-c`.

### `embedded/bootloaders-and-ota` - 7 пар

- `device-tree-describes-board-hardware`: ATAGS не є способом передавання DTB; `/memory` є вузлом,
  а не root property; відокремити Devicetree format від Linux behavior; обмежити `r2` 32-bit Arm
  boot protocol і дати точні Devicetree та Linux посилання.
- `bootloader-runs-before-application-firmware`: secondary slot, swap і VTOR не універсальні.
  Додати one-slot, Cortex-M0 без VTOR, memory remap та forwarding як умовні альтернативи.
- `bootloader-tasks-before-application`: bootloader може бути в ROM або незахищеній Flash;
  scratch, VTOR, signature/CRC, chain of trust і anti-rollback не є обов'язковими. Відокремити
  мінімальну функцію від secure-update options і кваліфікувати Evaluation guide за target/threat
  model.
- `firmware-update-methods-wired-bootloader-dual-bank-ota-rollback`: розділити debug probe,
  serial bootloader, dual-bank hardware та A/B slots; не вимагати однакові банки або одночасне
  виконання; trial boot та application confirmation описати умовно й виправити Evaluation guide.
- `mcu-boot-sequence-vector-table-to-main`: звузити питання до Cortex-M; відокремити
  architectural reset від toolchain runtime startup; не називати `0x00000000` універсальною
  фізичною Flash; виправити кількість на максимум 256 entries разом із початковим stack-pointer
  word; додати startup/ABI джерела.
- `mcu-boot-sequence-reset-vector-to-main-scheduler`: так само розділити architecture, ABI,
  vendor startup і RTOS; VTOR та priority grouping зробити умовними; RTTI не впливає на vector
  table, натомість C++ exceptions можуть додавати unwind tables; виправити `з адресу` на
  `з адреси`.
- `ota-update-risks-power-loss-signature-rollback-version`: використовувати MCUboot
  pending/test/confirm/revert; fleet rollout підтвердити окремим OTA-джерелом; явно задати threat
  model і пояснити, коли фіксується monotonic security counter, щоб trial rollback був можливий.

### `embedded/toolchain-and-build` - 13 пар

- `c-source-to-firmware-image-stages`: GCC `-S` створює assembly, не LLVM IR. Clang/LLVM IR
  описати як окремий optional path; не вимагати `cc1` у загальній відповіді.
- `cmake-in-cross-compilation-projects`: послатися на `cmake-toolchains(7)`, пояснити
  `CMAKE_SYSROOT` і `CMAKE_FIND_ROOT_PATH_MODE_*`, віддати перевагу target compile/link options.
- `cmake-toolchain-file-sysroot-and-target-flags`: точно описати `--sysroot`, `find_*` і root-path
  modes; toolchain file є рекомендованим reproducible механізмом, але не єдиною можливістю.
- `duplicate-symbol-fails-at-link-time`: замінити неправильне пояснення C `inline`; розділити ISO C
  external definition та C++ inline rules.
- `exporting-symbols-from-a-shared-library`: `extern "C"` дає C linkage/symbol names, а не
  стабільний ABI; додати джерела GCC visibility/GNU ld та Microsoft `dllexport`/import libraries.
- `git-basic-commands-and-branch-sync`: `git pull` виконує fetch і потім інтегрує через обраний
  merge, rebase або fast-forward-only mode; послатися на точний `git-pull` manual.
- `git-merge-vs-rebase-history-shape`: межа безпеки rebase - наявність downstream work, а не сам
  факт push; додати точні `git-merge` і `git-rebase` розділи.
- `git-three-states-modified-staged-committed`: three-state model стосується tracked content;
  історія є commit graph, не обов'язково line; використати точний Pro Git/manpage section.
- `inspect-preprocessing-assembly-object-files`: GCC source покриває лише `-E/-S/-c`; додати
  Clang, Binutils і CMake sources; замінити `grep` по JSON на JSON-aware query або verbose build.
- `interactive-rebase-edits-commit-history`: безпека залежить від downstream work; перед
  `reset --hard` вимагати clean worktree/stash або спершу створювати rescue branch.
- `library-development-lifecycle-stages`: подати lifecycle як один defensible варіант, а
  safety/real-time практики - як requirements-dependent; додати реальну lifecycle/versioning
  policy.
- `makefile-firmware-build-workflow`: використовувати справжній tab або явний `<TAB>`, послатися
  на GNU make і назвати всі rebuild conditions, не лише newer source.
- `static-vs-dynamic-library-build-and-link`: `.lib` буває static та import library; page sharing
  і writable state залежать від loader/OS; додати linker/loader та Microsoft sources; виправити
  `оперційної` на `операційної`.

## Інші треки: 15 пар із незакритими зауваженнями

- `behavioral/teamwork-and-conflict/technical-disagreement-resolved-without-authority`: замінити
  generic publisher search на стабільну сторінку видання з chapter/pages; прибрати непідтверджене
  `follow-up almost always`.
- `cs/algorithms/preconditions-binary-search-need-inserting-sorted-list`: прибрати batch-wide
  source list, залишити точні джерела для binary search та insertion behavior.
- `cs/complexity-and-analysis/amortized-cost-averages-a-worst-case-sequence`: growth factor впливає
  і на memory overhead, і на reallocation/copy constants; cppreference позначити `community` або
  замінити standard draft.
- `cs/complexity-and-analysis/time-complexity-code-range-range-work-sum`: half as many calls не
  гарантує twice-fast runtime; точно задати nesting і fixed `k`; прибрати бездоказове виконання,
  source contamination і зіпсований імпортний tag.
- `cs/data-structures/deque-better-list-queue-sliding-window-algorithm`: CPython block internals
  потребують pinned source/applies_to або видалення; slicing unsupported; `O(n*k)` лише
  bounded-window worst case; почистити sources.
- `cs/data-structures/stream-jobs-choose-hash-table-lookup-id`: завершити lazy-deletion model через
  entry-finder/tombstone або generation; не називати indexed priority queue без position index;
  почистити sources.
- `databases/indexing-and-query-plans/index-speed-up-read-query-increase-storage`: B-tree/TID/HOT
  звузити до PostgreSQL; прибрати `2-4 page reads` та `almost no cost`; додати точні джерела.
- `databases/sql-queries/parameterized-sql-query-protect-against-injection-string`: відокремити
  portable guarantee від driver protocol, використовувати parameterized ORM API та allowlist для
  identifiers/order expressions; замінити нерелевантні sources.
- `databases/sql-queries/write-query-returns-all-customers-including-zero`: фактичний SQL уже
  виправлено; в українському тексті лишилося послідовно перекласти або оформити inline code слова
  `customers`, `orders` і `paid orders`.
- `databases/transactions-and-isolation/failure-debit-credit-transaction-leave-partial-transfer`:
  відокремити server-side abort до commit від ambiguous outcome при втраті відповіді; послатися на
  PostgreSQL transaction tutorial.
- `databases/transactions-and-isolation/isolation-level-affect-concurrent-anomalies-stronger-isolation`:
  snapshot у PostgreSQL Repeatable Read береться на першому non-control statement; обидві
  serialization failures мають SQLSTATE `40001`; таблицю явно звузити до PostgreSQL.
- `engineering/ci-cd/choose-rolling-blue-green-canary-deployment-based`: DNS switch не atomic;
  zero downtime і seconds-fast rollback не гарантуються; canary не обмежує shared-schema side
  effects; додати умови та точні sources, скоротити English Short answer.
- `engineering/ci-cd/running-ci-pull-request-shorten-feedback-loop`: `instantly` замінити на
  `after each push, within pipeline latency`, лишити точне CI-джерело.
- `engineering/code-quality/reviewer-approve-imperfect-change-improves-overall-code`: використати
  Google Engineering Practices, прибрати unrelated sources, зробити blocking debt risk-based;
  скоротити English Short answer.
- `engineering/version-control/recover-commits-discarded-by-a-hard-reset`: додати локальні Git
  identity settings, отримувати фактичний hash замість вигаданого, звузити твердження про
  unstaged content.

Без додаткових зауважень пройшла пара
`databases/orm-and-persistence/n-plus-one-queries-from-lazy-relation-access`.

## Що вже виправлено з review інших треків

Повторно не відкривати без нового доказу: BFS/DFS, memoization, Big O, keyset pagination,
PostgreSQL constraints, payment CI, Stripe webhook ordering/retries, `unique_ptr`/`shared_ptr` та
intermittent ASan callback case. Фактичний paid-order SQL також виправлено, але сама пара лишається
в backlog через українське формулювання. Усі ці виправлення вже пройшли парні ревізії й валідатор.

## Сирі машинні звіти

LanguageTool повернув 987 евристичних кандидатів у 173 файлах, але їх не тріажили; це не
підтверджені дефекти. URL scan мав 130 відповідей HTTP 200, 5 відповідей 403, 28 timeout/cancel і
один malformed quoted URL; це також не надійний broken-link список. За потреби обидві перевірки
слід запустити заново на актуальному corpus, а не відновлювати старі raw файли.
