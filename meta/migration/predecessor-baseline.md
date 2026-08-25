# Базовий стан попереднього Anki-репозиторію

Знімок виконано 2026-09-03T09:33:02.5751307Z для
C:/Users/bogdan/Desktop/python_interview_questions.

## Стан репозиторію

- Гілка: main.
- HEAD: b73a6d1990a9dc212f149a128c3855e0476f7207.
- Робоче дерево брудне.
- Remote не налаштований.
- Після розгортання згорнутих untracked-каталогів є 135 змінених файлів: 48 доданих або
  untracked, 13 модифікованих і 74 видалених.
- Звичайний git status --porcelain=v1 показує 118 записів, бо згортає untracked-каталоги
  authoring/ і requirements/. У staging area є рівно одна зміна: видалення
  spec/examples/01_python_fundamentals_preview.apkg. Решта tracked-змін не індексована.

Зміна в цілому є незакоміченою перебудовою структури проєкту:

- матеріали зі spec/ переносяться до authoring/, одночасно частково редагуються;
- authoring/ отримав колекцію Python Interview Questions.anki2 і актуальний manifest.json;
- старі cards/drafts/ і cards/ready/ видаляються, а 23 джерела колод переносяться безпосередньо
  до cards/;
- кожен із 23 нових cards/*.txt відрізняється від відповідного колишнього cards/ready/*.txt
  рівно директивою назви колоди: Python Interview замінено на Python Interview Questions;
- додаються зібраний APKG, build та verification-скрипти, окремі requirements і дані перевірки
  ідентичності нотаток;
- README та частина старих службових матеріалів видаляються або переносяться.

Тому поточний HEAD не є відтворюваним baseline для виміряних артефактів: артефакти належать
брудному робочому дереву поверх цього HEAD.

## SHA-256 критичних артефактів

Усі mtime наведено в UTC.

| Шлях від кореня predecessor | Розмір, байт | mtime UTC | SHA-256 |
|---|---:|---|---|
| authoring/collection/Python Interview Questions.anki2 | 966656 | 2026-09-03T04:33:50.590567Z | f5ad26e9cf164cb1f6a64a76dbb410d537abf39ba4fa7058be8a9a61c0a961f5 |
| authoring/manifest.json | 3321 | 2026-09-03T04:59:20.566730Z | dba28dff1aa78cd5bb912a384a4b17c5d3e087472dd38eef664ff3d60948fe46 |
| cards/01_python_fundamentals.txt | 14803 | 2026-09-03T04:32:52.293666Z | 4bc53e8d99a2db14e75de19c460878a41efd254862ce5451a56d2f41137f8969 |
| cards/02_syntax_control_flow.txt | 16588 | 2026-09-03T04:32:52.292665Z | 9a6aa6bb610790ab2365f486555fd8a2a0f03cca3ab6de7ee3e46ac1bff28bbd |
| cards/03_objects_types_mutability.txt | 28062 | 2026-09-03T04:32:52.300668Z | f287905acf24644c42ef6e36406ad7cfceb4af3e173b2bcdb0f02686a217b009 |
| cards/04_collections.txt | 28164 | 2026-09-03T04:32:52.289289Z | fcab5b7a8ad468ad31df51363029ba2c3924919f7ae0e84563847b1b45456a02 |
| cards/05_functions_scope_closures.txt | 31448 | 2026-09-03T04:32:52.294666Z | 1549b5dd47b0f9120399e0938aa0b33e47294e9e632da636053e1ce6b3b9a4f2 |
| cards/06_oop_data_model.txt | 39733 | 2026-09-03T04:32:52.300668Z | 0eb306a114ba3b746e5bc7b7ff3742682eef0bea3361ba85b70282f57e340aa7 |
| cards/07_decorators.txt | 16047 | 2026-09-03T04:32:52.291664Z | 01bb8860ececa56243cfcf83d623e1a9f53ebb9be0a15f77bb5a38b7872b7146 |
| cards/08_iterators_generators.txt | 21786 | 2026-09-03T04:32:52.286291Z | 8d776cf3fa30c9ed4e75c00be77c870b05ce4c9cbe8502db6a511aff8432be0b |
| cards/09_context_managers.txt | 11871 | 2026-09-03T04:32:52.273495Z | be4e7e1b54ab12297095f89d5434f84f9bcaae280b03b2fcf970701cabb42291 |
| cards/10_exceptions.txt | 20313 | 2026-09-03T04:32:52.306063Z | 161e8a8734e31e379d76d5b7c83ae5e2c25ad95b83701575c69ed359633e5fa2 |
| cards/11_modules_packages_imports.txt | 18555 | 2026-09-03T04:32:52.306063Z | b11aa7aae8272abee2bb7fecf4dbd41cd51d798d2357eba7642b089be557855c |
| cards/12_files_io.txt | 17199 | 2026-09-03T04:32:52.304724Z | 280d0743a9a8f457e892533cdfa97cca27eaa7729685a033b6b813b3ec15f568 |
| cards/13_comprehensions_functional.txt | 14362 | 2026-09-03T04:32:52.308549Z | 37e66e6929b4271f4bd0c25f8fdb72ec71548b53a1a66b1e27d27722eff04128 |
| cards/14_cpython_internals_memory.txt | 26724 | 2026-09-03T04:32:52.309549Z | 5037f68ca0b69ef3acbf642b87b586f2824482ae2c26da8834e14b92cd773b60 |
| cards/15_gil_threads_processes.txt | 29339 | 2026-09-03T04:32:52.302714Z | ab50cf6125a18643aba30c757ae2e9b3c1a6dbd28ad5c7d3ef77def59b8661c8 |
| cards/16_asyncio.txt | 28892 | 2026-09-03T04:32:52.307549Z | 96cb1e4f0b6caf1e269fd0f64110c11bfa9f59cfa21d7ab236d5cd698791d858 |
| cards/17_standard_library.txt | 20970 | 2026-09-03T04:32:52.310549Z | 575a7cf9598ecdc897478651c02b19b8ef5de7358150e77b80c697c9542fa2e1 |
| cards/18_testing.txt | 23413 | 2026-09-03T04:32:52.304724Z | 9b655cb9940365b4aaff32c4591760573ca12c3869b130ed47a04a2700dd58cb |
| cards/19_performance_best_practices.txt | 31608 | 2026-09-03T04:32:52.307549Z | 460c1be32a89f3efc20551a516a638a2191ea6d1c24a0250539b8bcddd864b46 |
| cards/20_practical_coding.txt | 35723 | 2026-09-03T04:32:52.303726Z | 76b04ae7d5b78316b58edbe5120768a88e456016338fb3faff1c865c9ab83e7c |
| cards/21_algorithms_data_structures.txt | 5564 | 2026-09-03T04:32:52.298669Z | f7f0be0d09885c4c538a0be3963f137ebaf32898c7fa31c0d49d455626969448 |
| cards/22_databases_sql.txt | 9614 | 2026-09-03T04:32:52.294666Z | 0117402f42ec464374967d2db7253f4b68a6ce8177ccf7095c927b518fb9fbc0 |
| cards/23_git_cicd_sdlc.txt | 10147 | 2026-09-03T04:32:52.287289Z | badd6df7a93f1b2ff9e56d81151e5d213dfc189264e8b31742f53b4dc89f083d |
| cards/Python Interview Questions.apkg | 214002 | 2026-09-03T05:27:11.603220Z | 3facfdc7533909a1099383241a658b2bedeb56026b8c62e04532325309e5161f |

## Fingerprint note type

Колекція використовує modern layout з таблицями notetypes, fields і templates. Усі 392 нотатки
посилаються на один прикладний note type.

| Елемент | Назва | ord | ID |
|---|---|---:|---:|
| Note type | Python Interview Basic | – | 1788409800655 |
| Поле | Front | 0 | -96606943922847121 |
| Поле | Back | 1 | 455697503161544713 |
| Шаблон | Card 1 | 0 | 7535841431736045922 |

SHA-256 канонічного JSON fingerprint: 33d9f3dc1f05fdd8bc1094867d6ef9331b82e6a6dd65a6c4c4a21cb6bab412c9.
Ідентифікатори в канонічному JSON подано десятковими рядками, щоб уникнути втрати точності
64-бітних значень у JSON-реалізаціях.

Виміряні значення повністю збігаються з тим, що зафіксовано в проєктних документах.

## Кількості

| Об'єкт | Кількість |
|---|---:|
| Нотатки | 392 |
| Картки | 392 |
| Підколоди кореня Python Interview Questions | 23 |
| Усі рядки decks, разом з Default і коренем | 25 |

У modern schema ієрархічні назви підколод збережено з роздільником U+001F, а не двома
двокрапками. Це формат зберігання, а не розбіжність у кількості.

## Що оркестратор має закомітити й позначити тегом

1. У C:/Users/bogdan/Desktop/python_interview_questions треба закомітити весь поточний стан
   робочого дерева одним baseline-комітом: усі 48 untracked-файлів, 13 модифікованих і
   74 видалених файли. Частковий коміт не відповідатиме наведеним хешам.
2. Тег baseline треба поставити на новий коміт із цього стану. Поточний
   b73a6d1990a9dc212f149a128c3855e0476f7207 позначати тегом не можна, бо виміряні артефакти
   в ньому відсутні.
3. У C:/Users/bogdan/Desktop/interview-qa треба закомітити точні файли:
   meta/migration/predecessor-baseline.json і meta/migration/predecessor-baseline.md.
4. Назву нового predecessor-коміту й тегу цей знімок навмисно не задає: їх створює оркестратор,
   після чого доцільно записати фактичні commit SHA і tag до журналу міграції.

---

## Крок 0 закрито (2026-09-03)

Незакомічену перебудову зафіксовано в predecessor одним комітом, і на нього поставлено тег.

| | |
|---|---|
| baseline commit | `2372bb7175111701f883cc9dc3aba624dcb0bbdf` |
| tag | `baseline-2026-09-03` |
| стан робочого дерева після | чисте |

Отже хеші в цьому маніфесті тепер прив'язані до конкретного коміту, і вимога «витягнути GUID
до будь-яких змін» стала перевірною: будь-яку подальшу зміну можна продіфити проти тега.
