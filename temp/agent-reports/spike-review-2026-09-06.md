# Review: `packaging/anki/spike/`

**Дата:** 2026-09-06
**Рев'юер:** Cline (AI agent)
**Об'єкт:** `packaging/anki/spike/` — Anki compatibility harness

---

## ✅ Що працює правильно

| Перевірка | Результат |
|---|---|
| `run_spike.py` імпорти | ✅ Всі імпорти використовуються (`copy`, `NoteIdsLimit`, `ExportAnkiPackageOptions`) |
| `notetype_shape()` signature | ✅ Приймає `model: dict`, повертає `{model_id, name, fields, templates}` |
| `note_count_for_model()` | ✅ Використовується в експерименті A (рядки 342, 346) |
| `TARGET_MODEL_ID` (1788409800655) | ✅ Збігається з MEASUREMENTS.md predecessor |
| `run_tag_refresh.py` FIELD_DEFINITIONS | ✅ Збігається з `fingerprint.json` (5 полів, id/ord) |
| `run_tag_refresh.py` TEMPLATE_DEFINITIONS | ✅ Збігається з `fingerprint.json` (Card 1, ord 0, id 1600000001101) |
| `tag-refresh-evidence.json` environment | ✅ Збігається з MEASUREMENTS.md (Python 3.14.2, anki 26.8.1, genanki 0.13.1) |
| Експерименти A-J | ✅ Всі експерименти коректні та відповідають вимірюванням 1-9 у MEASUREMENTS.md |
| Експеримент I (overlapping packages) | ✅ 5+5 з перетином 2 = 8 нотаток, як у MEASUREMENTS.md |
| `write_genanki_package()` | ✅ Використовує `stable_deck_id(deck_name)`, а не `HISTORY_MODEL_ID` |
| Експеримент J (different model) | ✅ Використовує `copy.deepcopy()`, не має дубльованих ключів |

---

## 🟡 Помірні проблеми

### 1. `notetype_shape()` включає `"name"` для templates, але `meta/ANKI.md` каже `"[template id, ord]*"`

**meta/ANKI.md рядок 27-28:**
> "Fingerprint для CI = sha256 канонічного JSON із **`model_id`, назви моделі, `[field id, name, ord]*` і `[template id, ord]*`**."

**notetype_shape() повертає:**
```python
{
    "model_id": model["id"],
    "name": model["name"],
    "fields": [{"name": ..., "ord": ..., "id": ...}, ...],
    "templates": [{"name": ..., "ord": ..., "id": ...}, ...],  # ← name є!
}
```

**Невідповідність:** meta/ANKI.md описує `"[template id, ord]*"` (без `name`), але `notetype_shape()` включає `name` для templates. Це означає, що перейменування template змінить fingerprint, хоча meta/ANKI.md цього не згадує.

**Наслідок:** Документація та код розходяться. Але meta/ANKI.md рядок 30 каже: *"Це єдине визначення в проєкті; воно збігається з `notetype_shape()` у `packaging/anki/spike/run_spike.py`, і саме та функція має стати канонічною реалізацією"*. Тобто код є канонічним, а документація — ні. Але все одно це є невідповідністю.

**Рекомендація:** Оновити `meta/ANKI.md` — додати `"name"` до опису templates у fingerprint.

---

### 2. `desktop_default` сценарій: коментар суперечить evidence

**run_tag_refresh.py рядки 119-124:**
```python
# Anki Desktop 2025-ish default for the "Import file" dialog. Every flag is
# false in the pristine preset, which means the importer will NOT update notes,
# will NOT merge notetypes, and will NOT import scheduling.
pristine_desktop_preset_bytes = (
    b"\x08\x00\x10\x00\x18\x00 \x00(\x00"
)
```

**tag-refresh-evidence.json показує:**
```json
"desktop_default": {
    "update_applied_to_all_notes": true,
    "notes": {
        "x-tags-0001": {
            "fields_updated": true,
            ...
        }
    }
}
```

**Невідповідність:** Коментар каже *"the importer will NOT update notes"*, але evidence показує `"update_applied_to_all_notes": true, "fields_updated": true`.

**Можливі пояснення:**
1. Protobuf encoding неправильний — field numbers не збігаються з `ImportAnkiPackageOptions`.
2. Anki 26.8.1 має іншу поведінку, ніж очікувалось.
3. Це і є висновок експерименту — desktop preset насправді оновлює нотатки.

**Проблема:** Якщо це висновок, то чому коментар не оновлений? Коментар вводить в оману.

**Рекомендація:** Оновити коментар у `run_tag_refresh.py` — пояснити, чому desktop_default оновлює нотатки, незважаючи на прапорці false.

---

### 3. `tag-refresh-evidence.json` не згадується в `MEASUREMENTS.md`

**AGENTS.md рядок 136-137:**
> "Claims about Anki behaviour come from `packaging/anki/spike/`, which is re-runnable, and land in `meta/MEASUREMENTS.md`."

**Проблема:** `tag-refresh-evidence.json` є результатом вимірювання, але не згадується в `MEASUREMENTS.md`. Висновок експерименту (теги замінюються повністю, відсутні теги зникають) вже зафіксований у вимірюванні #7 таблиці MEASUREMENTS.md, але без посилання на `evidence.json` як доказ.

**Наслідок:** Evidence є orphan — не частиною доказової бази проєкту.

**Рекомендація:** Додати посилання на `tag-refresh-evidence.json` у `MEASUREMENTS.md`.

---

### 4. Експерименти A та H не згадуються в `MEASUREMENTS.md`

**Експеримент A:** Перевіряє, що додавання полів не ламає існуючі нотатки. Не згадується в MEASUREMENTS.md.

**Експеримент H:** Перевіряє, що імпорт у порожню колекцію працює. Не згадується в MEASUREMENTS.md.

**Проблема:** Ці експерименти є частиною harness, але їхні висновки не зафіксовані в MEASUREMENTS.md.

**Рекомендація:** Додати висновки експериментів A та H у `MEASUREMENTS.md`.

---

## 🟢 Дрібні зауваження

### 1. `test-deck/` не існує, але `build.py` посилається на нього

**build.py рядок 12:**
> "the GUID formula (`guid_for`) is exactly the one in `packaging/anki/test-deck/build_test_deck.py`"

**Проблема:** `test-deck/` не існує (перевірено через `Test-Path`). Це не є проблемою spike, але build.py посилається на неіснуючий файл.

**Рекомендація:** Видалити посилання з `build.py` або створити `test-deck/`.

---

## Підсумок

| # | Проблема | Серйозність |
|---|---|---|
| 1 | `notetype_shape()` включає `"name"` для templates, але `meta/ANKI.md` каже `"[template id, ord]*"` | 🟡 Помірна |
| 2 | `desktop_default` коментар суперечить evidence (прапорці false, але нотатки оновлюються) | 🟡 Помірна |
| 3 | `tag-refresh-evidence.json` не згадується в `MEASUREMENTS.md` | 🟡 Помірна |
| 4 | Експерименти A та H не згадуються в `MEASUREMENTS.md` | 🟡 Помірна |
| 5 | `test-deck/` не існує, але `build.py` посилається на нього | 🟢 Дрібна (не проблема spike) |

---

## Загальний стан

**spike є функціональним та коректним.** Проблеми — це невідповідності між документацією та кодом, а також orphan evidence.

**Головні дії:**
1. Оновити `meta/ANKI.md` — додати `"name"` до опису templates у fingerprint.
2. Оновити коментар у `run_tag_refresh.py` — пояснити, чому desktop_default оновлює нотатки, незважаючи на прапорці false.
3. Додати посилання на `tag-refresh-evidence.json` у `MEASUREMENTS.md`.
4. Додати висновки експериментів A та H у `MEASUREMENTS.md`.
