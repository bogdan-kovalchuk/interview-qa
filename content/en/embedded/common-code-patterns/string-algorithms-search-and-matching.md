---
id: emb-fund-0005
title: "What string algorithms do you know?"
track: embedded
section: common-code-patterns
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---
## Short answer

Basic operations: searching for a character or substring, comparison, copying, concatenation, tokenization, reverse, palindrome check, character frequency counting.[^dou-embedded-interview] In C you need to watch `\0`, buffer size, and overflow especially carefully.

Well-known algorithms: **KMP** for substring search in O(n+m), **Rabin-Karp** with a rolling hash, **Boyer-Moore** for fast practical search, Trie for a set of strings, Levenshtein distance for string similarity. For embedded, simple algorithms without heap and with controlled execution time are often important.

## Detailed explanation

TODO
