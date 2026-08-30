---
id: emb-cppfound-0072
title: "Як зберігається рядок у пам'яті і яка роль null-terminator?"
description: "How the null terminator marks the end of a C string."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
---

## Short answer

Рядок у C – масив символів де останній елемент = <span class="key">'\0' (null-terminator)</span>, байт зі значенням 0.<br><br>"hello" -> <code>['h','e','l','l','o','\0']</code> – 6 байт у пам'яті.<br><br>Null-terminator сигналізує стандартним функціям (<code>strlen</code>, <code>strcpy</code>, <code>printf %s</code>) де рядок закінчується. Без '\0' – читання виходить за межі -> UB.<br><br>Рядкові літерали автоматично мають '\0'. При ручному заповненні: <code>buf[n] = '\0';</code> обов'язково.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
