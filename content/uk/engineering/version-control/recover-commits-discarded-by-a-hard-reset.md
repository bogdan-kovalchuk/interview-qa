---
id: eng-vcs-0001
title: "Відновити два коміти, які hard reset прибрав із гілки"
description: "Коміти досі в базі об'єктів; reflog – це те, що досі їх називає."
track: engineering
section: version-control
level: middle
type: practical
tags: [git, reflog, reset, recovery, object-database]
status: published
updated: 2026-09-03
content_revision: 2
reconciled_with:
  en: 2
execution:
  language: shell
  standard: null
  toolchain:
    name: git
    version: "2.52.0"
  flags: []
applies_to:
  - product: Git
    version: "2.52"
anki:
  export: true
sources:
  - source_id: git-reflog-docs
    title: "git-reflog documentation"
    url: https://git-scm.com/docs/git-reflog
    accessed: 2026-09-03
    kind: official
    version: "2.52"
    applicability: "Вміст reflog, синтаксис ref@{n} і підкоманди expiry; reflog локальний для репозиторію і ніколи не передається push чи fetch."
  - source_id: git-reset-docs
    title: "git-reset documentation"
    url: https://git-scm.com/docs/git-reset
    accessed: 2026-09-03
    kind: official
    version: "2.52"
    applicability: "Що саме змінюють --soft, --mixed і --hard і який з них знищує вміст робочого дерева."
  - source_id: git-config-gc-reflog
    title: "git-config documentation: gc.reflogExpire and gc.reflogExpireUnreachable"
    url: https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcreflogExpire
    accessed: 2026-09-03
    kind: official
    version: "2.52"
    applicability: "Типове зберігання reflog 90 днів і 30 днів для записів, недосяжних із поточного tip."
---

## Short answer

**`git reset --hard` рухає вказівник гілки; він не видаляє коміти.** Вони лишаються в базі об'єктів,
недосяжні з жодної гілки, але все ще названі в reflog, тож відновлення – це пошук, а не
ремонт.[^git-reflog-docs] Прочитай `git reflog`, знайди хеш, на який гілка вказувала до reset, і
створи на цьому хеші гілку, а не роби ще один reset, щоб і ця дія лишалась оборотною.
<span class="warn">Робота, яку не закомітили, – інша справа: зміни поза index ніколи
не були об'єктами, а ті, що пройшли `git add`, лишаються лише dangling blob.</span>[^git-reset-docs]

## Detailed explanation

У hard reset відбуваються дві окремі речі, і оборотна лише одна з них. Ref гілки перезаписується на
цільовий коміт – це бухгалтерія, і її можна скасувати. Робоче дерево та index перезаписуються під
нього, і це знищує все, що ніколи не було закомічене.[^git-reset-docs] Паніка зазвичай стосується
комітів, а вони і є відновною половиною.

Коміти є об'єктами, адресованими за вмістом. Коли гілка перестає на коміт вказувати, у самому коміті
не змінюється нічого: він просто стає недосяжним, а недосяжні об'єкти живуть, доки їх не приберене
garbage collection. Від збирання їх тим часом тримає reflog: кожне оновлення `HEAD` і кожного tip
гілки записується туди разом із попереднім значенням, тож хеш до reset записаний, хоч його й не
називає жодна гілка.[^git-reflog-docs]

Це й задає форму відновлення. Знайти хеш, переконатися, що він правильний, і знову зробити його
досяжним. Створення нової гілки краще за переміщення поточної: це додавання, тож якщо хеш виявиться
не тим, більше нічого не втрачається, а два стани можна порівняти поруч.

Дедлайн існує. Записи reflog спливають – типово через 90 днів, а для записів, недосяжних із поточного
tip, через 30 днів, – після чого garbage collection може прибрати об'єкти
насправді.[^git-config-gc-reflog] Reflog також строго локальний: його не пушать, не фетчать, і в
свіжому клоні його немає, тож клон колеги не постачить твій запис reflog, хоча застарілий
remote-tracking ref або відкритий pull request можуть усе ще називати той самий коміт.

## Environment

- Локальний репозиторій Git, Git 2.52 або новіший, будь-яка платформа. Виміряний прогін – Git 2.52.0
  на Windows.
- Гілка щонайменше з трьома комітами, з яких останні два існують лише локально і не були запушені.
- Після reset не запускали garbage collection, і репозиторій має типові налаштування expiry.
- Лише доступ до shell; хостинг-провайдер, GUI або можливості IDE використовувати не можна.

Створити початковий стан:

```sh
git init recover-demo && cd recover-demo
printf 'a\n' > f && git add f && git commit -m first
printf 'b\n' >> f && git commit -am second
printf 'c\n' >> f && git commit -am third
git reset --hard HEAD~2
```

## Deliverable

Короткий транскрипт shell, придатний для командного runbook, який:

1. Встановлює, на що гілка вказувала до reset, не вгадуючи хеш.
2. Повертає два втрачені коміти на гілку з незмінними оригінальними хешами, авторством і датами.
3. Лишає стан після reset також доступним для порівняння, тож саме відновлення оборотне.
4. Одним рядком формулює, чому та сама процедура не відновила б незакомічені зміни.

Розібрана відповідь:

```sh
git reflog                                  # find the pre-reset hash of HEAD
git branch rescue 58fd2a2                   # make it reachable again, additively
git log --oneline rescue                    # verify: third, second, first
git diff HEAD rescue                        # confirm what the reset removed
git switch rescue                           # adopt the recovered state when satisfied
```

`git reset --hard HEAD@{1}` дістає той самий коміт одним кроком і є поширеним скороченням, але він
рухає поточну гілку, тож хибна догадка потребує другого відновлення. У runbook кладуть саме форму
з додаванням.

## Acceptance criteria

- `git log --oneline rescue` показує всі три коміти, а `git rev-parse rescue` дорівнює хешу, який
  reflog записав до reset.
- Хеші відновлених комітів ідентичні оригінальним, що водночас підтверджує незмінність авторства, дат
  і повідомлення; розв'язання, яке перестворює еквівалентні коміти з новими хешами, не проходить.
- Гілка, яку зресетили, досі вказує на свій коміт після reset, тож обидва стани існують.
- Хеш отриманий із reflog або з рівноцінного запису в транскрипті, а не набраний з пам'яті чи зі
  скролбеку.
- Ніде в транскрипті не з'являються `git gc`, `git prune` чи `--prune=now`.
- Транскрипт зазначає, що зміни, які ніколи не були закомічені, у такий спосіб не відновлюються, а
  якщо вони були staged – вказує на `git fsck --lost-found` як на часткове відновлення.

## Evaluation guide

### Expected signals

- Розрізняє закомічену роботу, яку можна відновити, і незакомічену, яку не можна.
- Знає, що коміти недосяжні, а не видалені, і називає reflog тим, що досі на них посилається.
- Відновлює створенням гілки або тега на хеші, а не ще одним `reset --hard`.
- Знає, що reflog локальний і обмежений у часі, тож відновлення доступне не безкінечно.

### Red flags

- Тягнеться по `git pull` або свіжий клон як метод відновлення, який працював би лише якби коміти
  були запушені.
- Вважає `git reset --hard` невідновним і радить переписати роботу руками.
- Не може сказати, чому у свіжому клоні немає reflog.
- Запускає `git gc --prune=now` під час діагностики.

### Level-up follow-up

Спитати, як відновити зміну, яку додали через `git add`, а потім знищили `reset --hard` до того, як
з'явився будь-який коміт. Сильна відповідь знає, що `git add` уже записав blob у базу об'єктів і його
можна знайти серед dangling objects через `git fsck --lost-found`, і що це відновлення по файлах, без
повідомлення коміту, дерева і порядку.

## Sources

<!-- generated from frontmatter -->
