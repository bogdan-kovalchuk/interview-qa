"""Build a self-diagnosing font-check card.

Answers one question objectively on any client: did each embedded font actually
load, or is the device silently falling back to a system font?

Method: width comparison. The same string is measured with `"<family>", sentinel`
and with `sentinel` alone. If the widths differ, the family was used. Two
sentinels (monospace and serif) are tried, so a coincidental width match with one
of them cannot produce a false negative.

Latin and Cyrillic are measured separately on purpose: the faces are embedded as
per-subset files with `unicode-range`, so one subset can load while the other
falls back.

Run:  python packaging/anki/test-deck/build_font_check.py
"""

from __future__ import annotations

import pathlib
import sys

import genanki

ROOT = pathlib.Path(__file__).resolve().parents[3]
FONTS = ROOT / "packaging" / "anki" / "fonts"
OUT = ROOT / "packaging" / "anki" / "test-deck"

MODEL_ID = 1600000000002
DECK_ID = 1600000000200

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from build_test_deck import font_face_css, guid_for  # noqa: E402

FRONT = r"""
<div class="fc">
  <div class="fc-title">Font check</div>
  <div id="fc-report" class="fc-report">вимірювання…</div>

  <div class="fc-note" id="fc-api">Font Loading API: —</div>

  <hr class="fc-hr">
  <div class="fc-sub">Візуальне порівняння: зверху вбудований шрифт, знизу примусовий системний</div>

  <div class="fc-row"><span class="fc-tag">Literata</span>
    <div class="s-lit">Handgloves 1lI0O — Український їжак ґанок</div>
    <div class="s-fallback-serif">Handgloves 1lI0O — Український їжак ґанок</div></div>

  <div class="fc-row"><span class="fc-tag">Golos Text</span>
    <div class="s-golos">Handgloves 1lI0O — Український їжак ґанок</div>
    <div class="s-fallback-sans">Handgloves 1lI0O — Український їжак ґанок</div></div>

  <div class="fc-row"><span class="fc-tag">JetBrains Mono</span>
    <div class="s-mono">Handgloves 1lI0O — Український їжак</div>
    <div class="s-fallback-mono">Handgloves 1lI0O — Український їжак</div></div>
</div>

<script>
(function () {
  var LAT = "Handgloves 1lI0O";
  var CYR = "Український їжак ґанок";
  var TESTS = [["Literata", 700], ["Golos Text", 400], ["Golos Text", 500],
               ["Golos Text", 700], ["JetBrains Mono", 400]];

  function width(text, family, weight) {
    var s = document.createElement("span");
    s.style.cssText = "position:absolute;left:-9999px;top:-9999px;white-space:nowrap;font-size:72px;";
    s.style.fontWeight = weight;
    s.style.fontFamily = family;
    s.textContent = text;
    document.body.appendChild(s);
    var w = s.getBoundingClientRect().width;
    document.body.removeChild(s);
    return w;
  }

  function used(family, weight, text) {
    var sentinels = ["monospace", "serif"];
    for (var i = 0; i < sentinels.length; i++) {
      var s = sentinels[i];
      if (width(text, '"' + family + '", ' + s, weight) !== width(text, s, weight)) return true;
    }
    return false;
  }

  function render() {
    var rows = ['<table class="fc-table"><tr><th>Шрифт</th><th>Вага</th><th>Latin</th><th>Кирилиця</th></tr>'];
    var allOk = true;
    for (var i = 0; i < TESTS.length; i++) {
      var fam = TESTS[i][0], w = TESTS[i][1];
      var lat = used(fam, w, LAT), cyr = used(fam, w, CYR);
      if (!lat || !cyr) allOk = false;
      rows.push("<tr><td>" + fam + "</td><td>" + w + "</td>" +
        '<td class="' + (lat ? "ok" : "bad") + '">' + (lat ? "завантажено" : "FALLBACK") + "</td>" +
        '<td class="' + (cyr ? "ok" : "bad") + '">' + (cyr ? "завантажено" : "FALLBACK") + "</td></tr>");
    }
    rows.push("</table>");
    rows.push('<div class="fc-verdict ' + (allOk ? "ok" : "bad") + '">' +
      (allOk ? "УСІ ШРИФТИ ПРАЦЮЮТЬ" : "Є ПІДМІНА СИСТЕМНИМ ШРИФТОМ — див. рядки FALLBACK") + "</div>");
    document.getElementById("fc-report").innerHTML = rows.join("");

    var api = "недоступний";
    if (document.fonts && document.fonts.check) {
      api = "status=" + document.fonts.status + " | " +
            TESTS.map(function (t) {
              return t[0].split(" ")[0] + ":" + (document.fonts.check(t[1] + ' 19px "' + t[0] + '"') ? "y" : "n");
            }).join(" ");
    }
    document.getElementById("fc-api").textContent = "Font Loading API: " + api;
  }

  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(render).catch(render);
    setTimeout(render, 1200);
  } else {
    setTimeout(render, 600);
  }
})();
</script>
"""

BACK = FRONT + """
<hr class="fc-hr">
<div class="fc-sub">Якщо десь стоїть FALLBACK – саме цей шрифт або підмножина не доїхали
на пристрій. Перевірте, що файли <code>_iqa-*.woff2</code> є в collection.media.</div>
"""

EXTRA_CSS = """
.fc { max-width: 680px; margin: 18px auto; padding: 24px 28px; background: var(--surface);
      border-radius: 16px; box-shadow: 0 2px 14px rgba(0,0,0,.08); }
.fc-title { font-family: var(--font-display); font-size: 26px; font-weight: 700; margin-bottom: 14px; }
.fc-report { margin-bottom: 10px; }
.fc-table { width: 100%; border-collapse: collapse; font-size: 15px; }
.fc-table th, .fc-table td { border-bottom: 1px solid var(--line); padding: 6px 4px; text-align: left; }
.fc-table th { color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: .08em; }
.ok { color: #1f8a4c; font-weight: 700; }
.bad { color: var(--warning); font-weight: 700; }
.fc-verdict { margin-top: 12px; font-size: 16px; }
.fc-note { color: var(--muted); font-size: 13px; word-break: break-all; }
.fc-hr { margin: 18px 0; border: 0; border-top: 1px solid var(--line); }
.fc-sub { color: var(--muted); font-size: 13px; margin-bottom: 10px; }
.fc-row { margin: 14px 0; }
.fc-tag { display: inline-block; font-size: 11px; letter-spacing: .1em; text-transform: uppercase;
          color: var(--muted); font-weight: 700; margin-bottom: 4px; }
.fc-row div { font-size: 21px; line-height: 1.35; }
.s-lit { font-family: "Literata"; font-weight: 700; }
.s-fallback-serif { font-family: Georgia, serif; font-weight: 700; opacity: .55; }
.s-golos { font-family: "Golos Text"; font-weight: 400; }
.s-fallback-sans { font-family: -apple-system, "Segoe UI", Roboto, sans-serif; opacity: .55; }
.s-mono { font-family: "JetBrains Mono"; font-weight: 400; }
.s-fallback-mono { font-family: Consolas, monospace; opacity: .55; }

.card { --surface:#fff; --line:#eceef2; --muted:#98a1b3; --warning:#c43d4b; --text:#1c2330;
        --font-display:"Literata",Georgia,serif;
        --font-text:"Golos Text",-apple-system,"Segoe UI",Roboto,sans-serif;
        --font-mono:"JetBrains Mono",Consolas,monospace;
        background:#f4f5f7; color:var(--text); font-family:var(--font-text);
        font-size:17px; line-height:1.5; text-align:left; }
.nightMode.card { --surface:#1e232b; --line:#2b313b; --muted:#778294; --text:#e7ebf2; background:#15181d; }
.mobile .fc { margin:0; border-radius:0; box-shadow:none; padding:18px 16px; }
code { font-family: var(--font-mono); font-size: .9em; }
"""


def main() -> int:
    model = genanki.Model(
        MODEL_ID, "Interview QA Font Check",
        fields=[{"name": "Front"}, {"name": "QID"}],
        templates=[{"name": "Card 1", "qfmt": FRONT, "afmt": BACK}],
        css=font_face_css() + "\n" + EXTRA_CSS,
    )
    deck = genanki.Deck(DECK_ID, "Interview QA Test::Font check")
    deck.add_note(genanki.Note(model=model, fields=["font-check", "fc-0001"],
                               tags=["iqa::test", "qid::fc-0001"], guid=guid_for("fc-0001")))
    pkg = genanki.Package([deck])
    pkg.media_files = [str(p) for p in sorted(FONTS.glob("_iqa-*.woff2"))]
    path = OUT / "Interview QA Font Check.apkg"
    pkg.write_to_file(str(path))
    print(f"{path.name}  {path.stat().st_size} B")
    return 0


if __name__ == "__main__":
    sys.exit(main())
