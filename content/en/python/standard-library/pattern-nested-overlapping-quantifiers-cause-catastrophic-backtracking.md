---
id: py-stdlib-0018
title: "Why can a pattern with nested or overlapping quantifiers cause catastrophic backtracking on crafted input, and how do you reduce ReDoS risk?"
track: python
section: standard-library
sources:
  - source_id: py314-library-re
    title: "Python 3.14: Library/re"
    url: https://docs.python.org/3.14/library/re.html
  - source_id: owasp-regular-expression-denial-of-service-redos
    title: "OWASP: Regular Expression Denial of Service REDOS"
    url: https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS
---

## Short answer

**The backtracking `re` engine tries other ways to match when part of the pattern fails.**[^py314-library-re] If nested quantifiers or overlapping alternatives produce exponentially many such ways, a failing search becomes too slow; this is ReDoS, and `(a+)+$` on a long run of `a` followed by `!` is a classic example.[^owasp-regular-expression-denial-of-service-redos] Possessive quantifiers and atomic groups (since Python 3.11) do not backtrack, but they can change which strings match.[^py314-library-re] So for protection, remove overlapping repetitions (for example, replace `(a+)+$` with `a+$`) and limit the input length.

## Detailed explanation

The `re` engine matches the pattern from left to right. When the next part does not match, the engine returns to the earlier quantifiers and tries to take fewer characters: `a*a` on `aaaa` first takes all four `a`, then gives one back.[^py314-library-re] For an ordinary pattern there are few alternatives, so a failure comes quickly. The blow-up happens when the same fragment can be split in many ways: `(a+)+` splits a run of n characters `a` into non-empty groups in 2^(n-1) ways.

When the string ends with a character the pattern does not accept (here `!`), `$` does not match, and the engine tries every split before it gives up. According to OWASP, the number of paths for such a pattern doubles with each extra `a`.[^owasp-regular-expression-denial-of-service-redos] The code below shows how an atomic group changes this search.

```python
import re

# Vulnerable: returns None, after trying every split of the a's.
re.match(r"(a+)+$", "a" * 22 + "!")

# Atomic group: the inner a+ never gives characters back.
print(re.match(r"(?>a+)+$", "a" * 22 + "!"))  # None, without the blow-up
print(re.match(r"(?>a+)a", "aaa"))            # None: the group keeps all three a's
print(re.match(r"a+a", "aaa") is not None)    # True: ordinary backtracking gives one back
```

Atomicity has a price. An atomic group and a possessive quantifier do not give characters back, so they can discard a match that would exist with backtracking: `(?>a+)a` does not match `aaa`, while `a+a` does.[^py314-library-re] Possessive `x*+`, `x++`, `x?+` and `x{m,n}+` are equivalent to the atomic groups `(?>x*)`, `(?>x+)`, `(?>x?)` and `(?>x{m,n})`; they were added in Python 3.11.[^py314-library-re]

What to do. The nesting in `(a+)+$` is unnecessary here: `a+$` matches the same strings and has no double search. The typical vulnerable form, according to OWASP, is a group with a repetition, and inside it a repetition or an alternation with overlaps.[^owasp-regular-expression-denial-of-service-redos] Not every nested quantifier is vulnerable, but for untrusted input it is worth limiting the string length before calling `re`. Atomic groups and possessive quantifiers only reduce the search and do not replace this.

**Common mistakes:**
- treating a pattern as safe because a test with a short string runs instantly: the time grows with the input length, and this shows only on a long string;
- fixing a pattern with an atomic group without checking the set of matches, for example `(?>a+)a` no longer matches `aaa`;
- accepting a pattern or a string from a user without a length limit.
