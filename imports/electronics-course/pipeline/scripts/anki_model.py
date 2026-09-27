"""
Anki model configuration for Electronics cards.
Based on Extra Spanish template, adapted for electronics without audio.
"""

ELECTRONICS_MODEL_NAME = "Electronics Q&A"

ELECTRONICS_FIELDS = [
    "Question",      # Front: питання
    "Answer",        # Back: відповідь
    "Context",       # Back: контекст/приклад
    "Importance",    # Footer: critical/important/nice-to-know
    "Lecture",       # Footer: номер лекції
]

ELECTRONICS_QFMT = """
<div class="card-wrap"><div class="bar"></div><div class="pad">
  <div class="question">{{Question}}</div>
  <div class="hint">Що це?</div></div></div>
"""

ELECTRONICS_AFMT = """
<div class="card-wrap"><div class="bar"></div><div class="pad">
  <div class="question">{{Question}}</div>
  <hr class="sep">
  <div class="answer">{{Answer}}</div>
  {{#Context}}
  <div class="context">{{Context}}</div>
  {{/Context}}
  <div class="foot">Лекція {{Lecture}} · {{Importance}}</div></div></div>
"""

ELECTRONICS_CSS = """
.card{background:#f4f5f7;}
.card-wrap{max-width:600px;margin:18px auto;background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 2px 14px rgba(0,0,0,.08);font-family:-apple-system,"Segoe UI",Roboto,sans-serif;color:#1c2330;}
.bar{height:8px;background:linear-gradient(90deg,#1f497d,#3b82f6);}
.pad{padding:26px 34px 30px;}
.question{font-size:22px;font-weight:600;margin:4px 0 12px;line-height:1.4;}
.hint{font-size:13px;color:#98a1b3;margin-top:16px;}
.sep{border:none;border-top:1px solid #eceef2;margin:20px 0;}
.answer{font-size:20px;font-weight:500;color:#1f497d;margin:0 0 18px;line-height:1.5;}
.context{padding:16px 18px;text-align:left;background:#f7f9fc;border-left:4px solid #3b82f6;border-radius:8px;font-size:16px;line-height:1.5;color:#4b5563;}
.context b,.context code{color:#1f497d;}
.foot{font-size:11px;color:#aab2c0;margin-top:22px;}
.nightMode.card{background:#15181d;}
.nightMode .card-wrap{background:#1e232b;color:#e7ebf2;box-shadow:none;}
.nightMode .sep{border-top-color:#2b313b;}
.nightMode .answer{color:#60a5fa;}
.nightMode .context{background:#232935;border-left-color:#3b82f6;color:#9ca3af;}
.nightMode .context b,.nightMode .context code{color:#93c5fd;}
.nightMode .hint{color:#6b7484;}
.nightMode .foot{color:#5a6474;}
"""
