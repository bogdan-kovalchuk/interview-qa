---
id: emb-cppfound-0068
title: "Що виведе на little-endian?<br><pre class=\"code-block\"><code>uint8_t arr[4]={0x01,0x02,0x03,0x04};<br>uint32_t *p=(uint32_t*)arr;<br>printf(\"%08X\",*p);</code></pre>"
description: "How little-endian byte order affects reading a byte array as a 32-bit integer."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? c-in-embedded; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

<code>04030201</code>.<br><br>На little-endian (Cortex-M) байти у пам'яті: <code>[01][02][03][04]</code>. При читанні як <code>uint32_t</code>: молодший байт – перший у пам'яті: LSB=0x01, потім 0x02, 0x03, MSB=0x04. Значення: <code>0x04030201</code>.<br><br><span class="warn">Увага</span>: такий cast може бути misaligned на MCU без підтримки. Безпечно: <code>uint32_t val; memcpy(&amp;val, arr, 4);</code>[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
