# Суворе рев'ю плану проєкту Interview QA

**Дата перевірки:** 2026-09-03  
**Об'єкт:** архітектурний план репозиторію `interview-qa`  
**Стан репозиторію під час перевірки:** design-only, робоче дерево чисте  
**Рішення:** **не погоджено для переходу до M1**

## 1. Короткий вердикт

План має сильну основу: сталі question ID і Anki GUID, topic-shaped decks, програми як композиції, стабільні permalink та генерація прогресу з контенту. Проте документи ще не утворюють один виконуваний контракт. У кількох критичних місцях одночасно діють взаємовиключні правила.

Найнебезпечніші проблеми:

1. план одночасно заморожує структуру Anki note type і планує змінити її з двох до п'яти полів;
2. нормативний формат внутрішнього посилання не містить ні мови, ні GitHub Pages base path;
3. заборона читати `content/` напряму суперечить запланованій архітектурі Astro/Starlight;
4. правила `status`, `completeness`, публікації сайту, включення в `.apkg` і появи `Reference` не узгоджені;
5. roadmap використовує програми раніше, ніж реалізує їх resolver;
6. контентна модель не здатна однаково добре описати всі заявлені типи інтерв'ю;
7. прогрес вимірює заповнення файлів, але не доводить покриття компетенцій;
8. гарантії якості перекладу й достовірності відповідей значно сильніші у формулюваннях, ніж у запропонованих перевірках.

Документи можна довести до робочого стану без зміни базової ідеї проєкту. Але M0 не завершений: спочатку потрібна конвергенція контрактів і кілька ризикових прототипів.

## 2. Оцінка

| Напрям | Оцінка | Висновок |
|---|---:|---|
| Архітектурна ідея | 7/10 | Правильні межі домену, сталі ідентифікатори, розділення package/deck/program |
| Внутрішня узгодженість | 3/10 | Кілька нормативних документів описують різну поведінку тієї самої сутності |
| Безпека Anki-міграції | 3/10 | Найризикованіша зміна note type ще не має підтвердженого сценарію оновлення |
| Контентна модель | 4/10 | Добра для concept-питань, недостатня для coding, debugging, system design і behavioral |
| I18N | 4/10 | Структурний контроль добрий, семантичний контроль практично відсутній |
| QA та CI | 4/10 | Є перелік воріт, але бракує доказовості тверджень, production-path тестів і scale budget |
| Roadmap | 3/10 | Залежності між етапами порушені, а міграція і point of no return об'єднані |
| Готовність до M1 | 2/10 | Реалізація зараз закодує суперечності замість контрактів |

## 3. Що в плані зроблено добре

### 3.1. Ідентичність відокремлена від представлення

Question ID є ключем permalink, крос-посилань, GUID і звітів. Slug можна змінювати без зміни ідентичності. Це правильна довгострокова модель для бази знань і Anki.

Докази: `AGENTS.md:58–65`, `meta/ANALYSIS.md:128–138`, `meta/adr/0005-stable-permalinks.md:14–18`, `meta/adr/0006-anki-guid-strategy.md`.

### 3.2. Package, deck, tag і program не змішані

Рішення тримати колоди тематичними, пакети дистрибуційними, а рольові зрізи декларативними є сильнішим за дублювання карток між напрямами. Це знижує ризик розходження копій одного питання.

Докази: `AGENTS.md:23–24`, `meta/adr/0007-specializations-as-programs.md`, `meta/adr/0008-deck-packaging-model.md`.

### 3.3. Генерований прогрес кращий за ручний tracker

`progress.csv` і `progress.json`, побудовані зі стану файлів, усувають окрему таблицю, яка неминуче застаріє. Це правильне рішення, якщо звіт буде доповнений покриттям цілей, а не лише станом секцій.

Докази: `AGENTS.md:31–32`, `meta/PROGRESS_TRACKING.md:11–18`.

### 3.4. Відмова від custom domain виправдана

GitHub Pages URL довгий, але контрольований обліковим записом і назвою репозиторію. Для URL, надрукованого в картках на роки, це прийнятний компроміс.

Докази: `AGENTS.md:13–17`, `meta/adr/0005-stable-permalinks.md:29–37`.

### 3.5. Вибір Astro/Starlight загалом підтверджується

Starlight має штатну i18n-модель, а Pagefind індексує багатомовні сайти. Українська UI-локаль підтримується, хоча Pagefind не має українського stemming. Відмова від Material for MkDocs також має підстави: `mkdocs-static-i18n` заморожений, а екосистема MkDocs перебуває у переході до 2.0.

Джерела: [Starlight i18n](https://starlight.astro.build/uk/guides/i18n/), [Pagefind multilingual search](https://pagefind.app/docs/multilingual/), [Material for MkDocs 2.0](https://squidfunk.github.io/mkdocs-material/blog/2026/02/18/mkdocs-2.0/), [`mkdocs-static-i18n`](https://github.com/ultrabug/mkdocs-static-i18n), [MkDocs releases](https://pypi.org/project/mkdocs/).

## 4. Критичні блокери

### C-01. Контракт Anki note type суперечить сам собі

**Доказ у плані:**

- `AGENTS.md:25–28` заморожує `model_id`, назви й порядок полів та кількість template;
- `meta/ANKI_INTEGRATION.md:31–44` пропонує або розширити наявний `Python Interview Basic`, або створити новий `Interview QA Basic`;
- там само двопольову модель `Front`, `Back` перетворено на п'ятипольову: `Front`, `Back`, `Reference`, `Sources`, `QID`;
- `meta/ANKI_INTEGRATION.md:42–44` оголошує додавання полів безпечним, хоча це саме структурна міграція, яку верхній контракт забороняє виконувати як звичайне редагування.

**Перевірений фактичний стан predecessor:**

- `.apkg` існує і проходить наявний verifier: 392 notes, 392 cards, 23 subdecks;
- smoke test повторного імпорту зберігає GUID і card state для незмінного двопольового note type;
- поточний model: `Python Interview Basic`, `model_id = 1788409800655`;
- поля: `Front` ord 0, id `-96606943922847121`; `Back` ord 1, id `455697503161544713`;
- один template: `Card 1`, ord 0, id `7535841431736045922`.

Ці тести не доводять безпечність зміни note type. Вони доводять лише безпечність оновлення нотаток за незмінної структури.

Офіційна документація Anki попереджає, що оновлення наявних notes залежить від GUID і сумісності note type; зміна note type може призвести до ignored updates. Anki 23.10+ має додаткові режими merge/update, але вони залежать від вибору користувача і можуть вимагати full sync. Field і template IDs існують з Anki 2.1.67, отже їх теж треба включити до compatibility contract.

Джерела: [Anki packaged decks](https://docs.ankiweb.net/importing/packaged-decks.html), [Anki FAQ про змінений note type](https://github.com/ankitects/anki/blob/main/docs-site/faqs/some-updates-were-ignored-because-the-note-type-has-changed.mdx), [package importer source](https://github.com/ankitects/anki/blob/main/rslib/src/import_export/package/apkg/import/notes.rs), [text import and GUID guidance](https://docs.ankiweb.net/importing/text-files.html).

**Ризик:** дублікати, ignored updates, розходження template, примусовий full sync або незворотне пошкодження очікуваного update path.

**Обов'язкове виправлення:**

1. вибрати рівно один target note type;
2. зафіксувати `model_id`, field IDs, назви, ord, template IDs і ord;
3. окремо описати one-time migration зі старої двопольової моделі;
4. протестувати її на копії реального профілю на мінімальній і поточній підтримуваних версіях Anki;
5. перевірити default import, explicit merge/update, повторний імпорт, scheduling, suspended/buried state, flags, custom study та sync;
6. лише після міграції оголосити нову структуру замороженою.

### C-02. Нормативні URL не працюватимуть на GitHub Pages

**Доказ у плані:**

- `meta/CONTENT_SPEC.md:200–211` вимагає `[text](/q/{id}/)`;
- `AGENTS.md:61` вимагає `/{lang}/q/{id}/`;
- `meta/adr/0005-stable-permalinks.md:15–18` визначає повну route-схему `/{lang}/q/{id}/{slug}/` і короткий permalink `/{lang}/q/{id}/`;
- фактичний production base для project site буде `/interview-qa/`.

Root-relative URL `/q/...` на `bogdan-kovalchuk.github.io` веде до кореня домену, а не до `/interview-qa/`. Навіть `/{lang}/q/...` без base path має ту саму проблему.

Astro прямо вимагає `site` і `base: '/repo-name'` для GitHub Pages project site та попереджає, що внутрішні посилання мають враховувати `base`.

Джерело: [Deploy Astro to GitHub Pages](https://docs.astro.build/en/guides/deploy/github/).

**Обов'язкове виправлення:**

- у source Markdown зберігати language-neutral token або `qid:` reference, а не готовий root-relative URL;
- exporter має матеріалізувати правильний URL окремо для сайту, JSON і Anki;
- production test має будувати сайт саме з `base=/interview-qa`, а не тільки в dev server;
- перевіряти остаточний HTML і всі href після build.

### C-03. Data-flow invariant несумісний із запланованим сайтом

**Доказ у плані:**

- `AGENTS.md:67`, `meta/adr/0002-content-model.md:20` і `meta/REPOSITORY_TOPOLOGY.md:82–95` забороняють будь-якому consumer читати `content/` напряму;
- `meta/ANALYSIS.md:71–83` показує `site/` як прямого споживача `content/`;
- `meta/PIPELINE.md:31`, `90–99`, `239–258` також описує генерацію сайту безпосередньо з дерева `content/`;
- `meta/I18N.md` покладається на стандартну Starlight content structure.

Це не стилістична розбіжність. Від вибору залежить build graph, watch mode, schema validation, last-updated metadata, source edit links і локальна розробка.

Starlight штатно очікує docs collection під `src/content/docs`. Astro glob loader може читати інші каталоги, але custom root для Starlight вже мав обмеження в multilingual behavior та last-updated handling.

Джерела: [Starlight configuration and loaders](https://starlight.astro.build/uk/reference/configuration/), [Astro content loader reference](https://docs.astro.build/en/reference/content-loader-reference/), [Starlight custom content directory discussion](https://github.com/withastro/starlight/discussions/1257).

**Рекомендоване рішення:** exporter створює ігнороване generated mirror у `site/src/content/docs/`, а Starlight читає тільки його стандартним `docsLoader`. Source URL, question ID і checksum треба передавати в generated frontmatter. Якщо команда свідомо обере пряме читання `content/`, треба змінити invariant і ADR, а не залишати обидві моделі.

## 5. Major findings

### M-01. Немає єдиної таблиці життєвого циклу питання

Одні документи кажуть, що все публікується від першого дня, інші виключають `draft` і `review` з production:

- `meta/CONTENT_SPEC.md:164–189`: completeness не є воротами, сторінка існує обома мовами від першого дня;
- `meta/QUALITY_GATES.md:109–122`: `draft` не йде ні на сайт, ні в колоду; `review` є лише в preview; `published` йде всюди;
- `meta/I18N.md:100–102`: EN `stub` достатній, щоб сторінка існувала;
- `meta/ANKI_INTEGRATION.md:138–169`: картка без `Short answer` не відвантажується, `Reference` є завжди, коли картка відвантажена;
- `README.md:12–15` пов'язує картку з появою детального пояснення;
- `meta/PIPELINE.md:415–417` додає `Reference` лише після `Detailed explanation`.

**Виправлення:** створити одну нормативну truth table з осями `status × completeness × language`. Для кожної комбінації визначити: production page, preview page, navigation/search, `.apkg`, suspended state, `Reference`, status report і release eligibility. Усі інші документи мають посилатися на неї.

### M-02. Short permalink описаний як redirect, але статичний redirect не еквівалентний HTTP redirect

На static Astro adapter redirect зазвичай матеріалізується як HTML page з meta refresh. Це впливає на SEO, accessibility, canonical URL, cache behavior і тести. Формулювання «редіректить» зараз приховує реальну семантику.

Джерела: [Astro routing redirects](https://docs.astro.build/en/guides/routing/), [StaticRedirectNotAvailable](https://docs.astro.build/en/reference/errors/static-redirect-not-available/).

**Виправлення:** визначити short route як stable resolver page з `canonical`, immediate navigation, visible fallback link і tombstone behavior. Не тестувати її як HTTP 301/308, якщо hosting цього не забезпечує.

### M-03. Roadmap порушує залежності між program і deck build

- M3 обіцяє `deck build --program` та пакетування: `meta/ROADMAP.md:70–79`, `meta/PIPELINE.md:117–120`;
- resolver `programs/*.yml` з'являється лише в M6: `meta/ROADMAP.md:109–114`;
- M6 знову відкриває вже закрите ADR-0008 рішення: «колоди-програми або фільтровані колоди»;
- `meta/examples/program-example.yml:48–51` містить `Interview QA::Programs::*` і коментар, що рішення відкладене.

**Виправлення:** перенести мінімальний program resolver і schema до M1/M3, а з M6 прибрати повторне рішення про deck topology. Example YAML привести у відповідність до ADR-0008.

### M-04. Єдина структура body не покриває всі види інтерв'ю

`meta/CONTENT_SPEC.md:80–125` оптимізований під concept/mechanism question. Для заявленого scope бракує типоспецифічних контрактів:

- coding: constraints, input/output, examples, tests, complexity, edge cases;
- debugging: symptom, observations, hypotheses, diagnosis, fix, prevention;
- system design: requirements, scale assumptions, architecture, alternatives, trade-offs, failure modes;
- behavioral: assessed competency, expected signals, STAR evidence, follow-up prompts, red flags;
- practical task: environment, deliverable, acceptance criteria.

**Виправлення:** визначити discriminated schemas за `type`, спільне ядро й типоспецифічні секції. До замороження schema зробити мінімум по одному повному pilot кожного типу.

### M-05. Фізичний path contract конфліктує з taxonomy depth

`meta/CONTENT_SPEC.md:10–13` допускає рівно `content/{lang}/{track}/{section}/{slug}.md`. Водночас `meta/TAXONOMY.md:130–133` і `229–231` вводить третій рівень: `frameworks/qt`, `frameworks/boost`, `rtos/freertos`, `rtos/zephyr`.

**Виправлення:** або зробити path рекурсивним `content/{lang}/{track}/**/{slug}.md` з окремим canonical `section_id`, або сплющити taxonomy. Не виводити стабільні semantic IDs тільки з фізичного шляху.

### M-06. Progress report вимірює наповнення, а не покриття компетенцій

`meta/PROGRESS_TRACKING.md:22–91` добре відповідає на питання «які секції файлу заповнені», але не відповідає на питання «чи достатньо підготовлена людина до конкретного interview loop». Цільові 100 C++ і 50 embedded questions у `meta/ROADMAP.md:98–105` стимулюють досягнення числа, а не закриття прогалин.

**Виправлення:** додати окрему generated projection:

`role competency → learning/interview objective → level → question IDs → evidence status`.

Кількість карток має бути наслідком objective coverage. Не робити count target acceptance criterion.

### M-07. Рівні й типи не мають операційних визначень

Списки `junior/middle/senior` і типів існують, але немає критеріїв, за якими два reviewers однаково класифікують питання. Немає expected answer signal, depth, interview stage, time budget і red flags для рівня.

**Виправлення:** створити rubric для кожного `level × type`: що кандидат повинен назвати, пояснити, застосувати й захистити; які follow-up questions підвищують рівень; що є критичною помилкою.

### M-08. Машинна parity-перевірка не доводить якість перекладу

`meta/I18N.md:113–121` стверджує, що структурна перевірка «покриває всі реальні поломки перекладу», а ручне рев'ю може бути лише вибірковим. Це хибна гарантія. Однакові секції, code blocks, sources, xrefs і glossary не виявляють зміну заперечення, переплутану умову, втрату модальності або технічно правдоподібний, але неправильний переклад.

**Виправлення:** parity залишити mechanical gate. Окремо ввести semantic review gate для `published`, щонайменше для `Short answer`, чисел, умов, заперечень, API names і safety/security claims. AI translation не може сама підтверджувати свою правильність без source-based review.

### M-09. `source_updated` передбачає односторонній original, якого політика не має

`meta/I18N.md:94–96` дозволяє авторити будь-якою мовою. `meta/I18N.md:166–169` водночас описує «оригінал» і «переклад» та одностороннє поле `source_updated`.

**Виправлення:** використати симетричний revision contract, наприклад `content_revision` плюс `translated_from_revision`, або hashes кожної мовної пари. Зміна будь-якої сторони має позначати іншу як таку, що потребує semantic reconciliation.

### M-10. Source policy не забезпечує claim-level verification

`meta/QUALITY_GATES.md:45` перевіряє лише наявність хоча б одного не-community source. Одне загальне посилання не доводить усі технічні твердження у відповіді. `meta/I18N.md:117–119` пропонує звіряти джерело лише тоді, коли формулювання «виглядає сумнівним».

**Виправлення:**

- присвоювати source IDs;
- пов'язувати нетривіальні claims із source IDs;
- зберігати version/date/applicability та точний section/page/anchor;
- для code questions виконувати або компілювати приклади на заявлених runtime/compiler versions;
- інвалідовувати publication review після зміни змістовного тексту;
- відокремити `source present`, `source supports claim` і `example executed`.

### M-11. Source of truth для schema визначено у двох напрямах

- `meta/PIPELINE.md:292–323`: Pydantic є джерелом, з нього виходять JSON Schema і Zod;
- `meta/ROADMAP.md:40–49`: `question.schema.json` є джерелом, з нього генеруються Zod і Python schemas;
- `meta/adr/0002-content-model.md:27–28` формулює ще один варіант генерації обох schemas.

**Виправлення:** вибрати один canonical schema source і додати parity test, що generated artifacts clean після regeneration.

### M-12. Зайве дублювання metadata створить drift

`track` і `section` одночасно кодуються в path і frontmatter. `anki.deck` виводиться з taxonomy, але теж записується. `roles` дублюють program membership. Language-neutral metadata повторюється у двох мовних файлах.

**Виправлення:** для кожного поля визначити одне authoritative місце. Валідатор має або виводити значення, або вимагати точну parity, але не дозволяти незалежне редагування копій.

### M-13. Cutover predecessor не має безпечного rollback window

`meta/ROADMAP.md:83–94` в одному milestone виконує міграцію, release і архівацію predecessor. `meta/REPOSITORY_TOPOLOGY.md` називає це point of no return. На момент аудиту predecessor має великий dirty worktree, тому вимога «витягнути GUID до будь-яких змін» уже не є аудитовною без зафіксованої базової лінії.

**Виправлення:**

1. зафіксувати або тегувати відомий baseline predecessor;
2. зберегти hashes `.anki2`, `.apkg`, TSV, GUID map і note-type fingerprint;
3. виконати shadow build і порівняти його з baseline;
4. протестувати update на копіях реальних профілів;
5. випустити candidate release;
6. витримати observation/rollback window;
7. лише потім зробити predecessor read-only/archive.

### M-14. MIT декларація не закриває dependency licensing

Python package `anki`, який природно використовувати для `.apkg`, поширюється під AGPL-3.0-or-later. MIT сумісна як permissive license, але спосіб імпорту, зв'язування і розповсюдження combined builder потребує окремого аналізу. Це не доказ порушення, але план не має права оголосити питання закритим одним root `LICENSE`.

Джерела: [`anki` on PyPI](https://pypi.org/project/anki/), [GNU GPL FAQ](https://www.gnu.org/licenses/gpl-faq.en.html).

**Виправлення:** провести dependency license review до M3, зафіксувати рішення, додати `THIRD_PARTY_NOTICES` або dependency notice generation. За потреби ізолювати AGPL builder як окремий інструмент. Root license проєкту може залишитися MIT.

### M-15. Заявлений масштаб 4–5 тисяч сторінок не перевіряється

Архітектура передбачає тисячі bilingual pages, generated indexes, Pagefind і program views, але roadmap не містить performance budget або synthetic benchmark. Astro окремо документує `deferRender` для великих content collections, що підтверджує реальність build-memory risk.

Джерело: [Astro content loader reference](https://docs.astro.build/en/reference/content-loader-reference/).

**Виправлення:** до масового наповнення згенерувати 5 000 synthetic questions і виміряти build time, peak RAM, output size, Pagefind index size, search latency та broken-link scan time. Зафіксувати budgets у CI.

### M-16. CI-план не фіксує supply-chain та production-output checks

У QUALITY_GATES бракує явних вимог до lockfiles, pinned action SHAs, dependency audit, HTML validation, accessibility, sitemap, canonical/hreflang, production-base links і перевірки artifact provenance.

**Виправлення:** додати окремі ворота для:

- Python lock і Node lock;
- GitHub Actions, pinned за immutable commit SHA;
- SAST/dependency/license audit;
- built HTML, internal/external URL policy, `base=/interview-qa`;
- accessibility smoke test;
- canonical, hreflang, sitemap і robots;
- checksums, SBOM або принаймні dependency manifest для release artifacts.

## 6. Minor findings

### m-01. Мовні помилки в нормативних документах

- `meta/QUALITY_GATES.md:92`: `немає биті внутрішніх посилань` треба замінити на `немає битих внутрішніх посилань`;
- `meta/QUALITY_GATES.md:118`: `prewiew-збірці` треба замінити на `preview-збірці`;
- `meta/ANKI_INTEGRATION.md:151`: `у чергі повторень` треба замінити на `у черзі повторень`.

### m-02. Порушено глобальну типографічну вимогу

У Markdown-файлах знайдено 337 рядків із забороненим символом em dash U+2014. Shared library прямо вимагає всюди використовувати en dash U+2013.

**Виправлення:** виконати окрему mechanical normalization зміну й додати CI check, який падає при появі U+2014. Не змішувати її з семантичними правками плану.

### m-03. Локальні Markdown links наразі цілі

Механічний scan не знайшов broken relative/local links. Це позитивний результат, але він не перевіряє майбутні generated routes або production base path.

### m-04. GitHub infrastructure ще не існує

Під час перевірки локальний репозиторій не мав configured remote, GitHub API для `bogdan-kovalchuk/interview-qa` повертав 404, а очікуваний Pages URL також був недоступний. Для design-only фази це не дефект, але твердження про працездатний deployment поки не має фактичного підтвердження.

### m-05. Reference repository не має ліцензії

GitHub API повертав `license: null`, а endpoint `/license` для `tavor118/pj_python_interview_questions_and_answers` повертав 404. Отже план правильно використовує його лише як topic-discovery source і не повинен копіювати wording або структуру текстів.

Посилання: [reference repository](https://github.com/tavor118/pj_python_interview_questions_and_answers), [repository API](https://api.github.com/repos/tavor118/pj_python_interview_questions_and_answers), [license API](https://api.github.com/repos/tavor118/pj_python_interview_questions_and_answers/license).

## 7. Обов'язковий порядок виправлення плану

### M0.1 – Конвергенція документів

1. Визначити precedence: `AGENTS.md` → accepted ADR → normative specs → analysis/examples.
2. Створити lifecycle truth table.
3. Вирівняти URL contract і GitHub Pages base handling.
4. Вибрати єдиний data flow для site.
5. Вибрати canonical schema source.
6. Видалити stale alternatives, що суперечать accepted ADR.

**Вихід:** одна поведінка для кожної сутності, без взаємовиключних нормативних тверджень.

### M0.2 – Content model pilot

Створити по одному повному bilingual pilot для concept, coding, debugging, system design і behavioral. Перевірити schema, rendering, exports, review rubric та source traceability.

**Вихід:** content contract доведений прикладами всіх основних типів.

### M0.3 – GitHub Pages/Starlight spike

Перевірити дві локалі, `base=/interview-qa`, generated content mirror або custom loader, short permalink resolver, tombstone, canonical/hreflang, Pagefind і production broken-link scan.

**Вихід:** deployed test site з реальними production URL, а не лише dev-server result.

### M0.4 – Anki compatibility spike

Перевірити migration двопольового note type, field/template IDs, default reimport, edit update, tag update, scheduling, suspended state, sync і rollback на копії реального профілю.

**Вихід:** зафіксований target fingerprint і відтворюваний compatibility report.

### M0.5 – Scale spike

Зібрати 5 000 synthetic bilingual pages з indexes, programs і Pagefind. Зафіксувати budgets часу, RAM і розміру artifacts.

**Вихід:** доказ, що обрана архітектура витримує цільовий масштаб.

### M1 – Schema, validator і coverage model

Реалізувати canonical schema, typed body variants, objective map, parity, source traceability, generated progress і мінімальний program resolver.

### M2 – Site

Реалізувати production-accurate routes і deployment лише після успішного spike.

### M3 – Export і package build

Реалізувати export contract, thematic decks, release manifest і Anki compatibility gates.

### M4 – Shadow migration та cutover

Не архівувати predecessor в одному кроці з першим release. Спочатку shadow build, profile tests, candidate release і observation window.

### M5+ – Розширення через objective coverage

Планувати C++, Embedded та інші напрями за закриттям interview objectives. Число карток використовувати як метрику, а не як ціль.

## 8. Acceptance criteria для повторного погодження

План можна повторно подати на review, коли виконано всі умови:

- немає суперечностей щодо note type, status/completeness, Reference і publication;
- URL contract проходить production GitHub Pages build із `/interview-qa/`;
- data-flow contract має одну реалізаційну схему;
- schema source of truth визначено один раз;
- program resolver доступний до першої команди `deck build --program`;
- content model перевірений на всіх основних question types;
- Anki migration підтверджена compatibility report на копії реального профілю;
- migration має baseline, shadow release і rollback window;
- progress включає competency/objective coverage;
- semantic translation review відокремлений від machine parity;
- claims мають перевірювану прив'язку до sources;
- dependency licensing задокументований;
- 5 000-page synthetic build вкладається у зафіксовані budgets;
- production HTML, accessibility, canonical/hreflang, sitemap і links входять у CI;
- stale examples та друкарські помилки виправлені;
- U+2014 заборонений механічним gate.

## 9. Методика та межі перевірки

Перевірено:

- усі наявні Markdown design documents і accepted ADR;
- локальні cross-references та Git state;
- фактичний package/profile стан predecessor repository;
- офіційні Anki manual і importer source;
- офіційні Astro/Starlight/Pagefind матеріали;
- актуальний стан MkDocs-related stack;
- GitHub repository і license metadata reference project;
- доступні MCP resources.

У доступному MCP catalog не було GitHub connector, тому GitHub перевірявся через GitHub REST API і web. Review не є юридичним висновком щодо AGPL і не замінює тест на реальних підтримуваних Anki clients. Саме ці два пункти залишаються окремими implementation gates.

## 10. Підсумок

Проєкт варто продовжувати, але не за поточним roadmap. Архітектурні рішення в основному здорові; проблема в тому, що документація одночасно описує кілька несумісних реалізацій. Найкращий наступний крок не написання коду, а короткий M0.1: одна truth table, один URL contract, один site data flow, один schema source і один target Anki note type. Після цього п'ять pilot/spike перевірок дадуть достатньо доказів для безпечного старту M1.
