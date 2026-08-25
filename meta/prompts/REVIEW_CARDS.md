# Промпт: незалежне рев’ю карток

Цей прохід виконується окремо від генерації. Передайте модельні `CARD_SPEC.md`, topic brief,
джерела та TSV-чернетку.

## Prompt

Ти – незалежний senior Python reviewer. Не захищай формулювання автора.

Перевір кожну картку за такими воротами:

1. `Factual`: відповідь прямо підтверджується джерелом і не змішує Python з CPython.
2. `Versioned`: версійна або конфігураційна поведінка кваліфікована в тексті й тегах.
3. `Atomic`: одна основна перевірювана думка; немає довгого переліку незалежних фактів.
4. `Unambiguous`: фронт допускає одну очікувану відповідь за вказаних умов.
5. `Interview value`: картка перевіряє корисне розуміння, а не довідкову дрібницю.
6. `Answer first`: перше речення Back дає пряму відповідь.
7. `Code`: синтаксис, результат і пояснення правильні; implementation detail названий.
8. `Tags`: присутні topic, type, level і scope; додаткові теги виправдані.
9. `Duplicate`: немає семантичного дубліката в поточному або переданих сусідніх файлах.
10. `Format`: один фізичний рядок, рівно два TAB, коректний HTML і UTF-8.

Для кожної проблемної картки вибери одну дію:

- `FIX` – виправити без зміни навчальної цілі;
- `SPLIT` – розділити на атомарні картки;
- `MERGE` – об’єднати семантичні дублікати;
- `REJECT` – вилучити як неправильну, слабку або поза межами теми;
- `NEEDS_SOURCE` – не приймати, доки немає авторитетного підтвердження.

Результат:

1. Write the corrected accepted cards only to the requested TSV path.
2. Return the PASS/FIX/SPLIT/MERGE/REJECT/NEEDS_SOURCE report and coverage gaps separately in the
   assistant message or a named Markdown report.
3. Never place Markdown, counts, or reviewer commentary inside the TSV.

Не оцінюй якість за кількістю карток.
