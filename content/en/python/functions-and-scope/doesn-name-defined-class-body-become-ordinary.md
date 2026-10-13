---
id: py-funcs-0015
title: "Why doesn't a name defined in a class body become an ordinary enclosing lexical scope for the code of that class's methods?"
description: "Why doesn't a name defined in a class body become an ordinary enclosing lexical scope for the code of that class's methods?"
track: python
section: functions-and-scope
level: senior
type: mechanism
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-executionmodel-resolution-of-names
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#resolution-of-names
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, section Resolution of names: scope of names in a class block and the annotation-scope exception."
  - source_id: py314-reference-executionmodel-lazy-evaluation
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#lazy-evaluation
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, section Lazy evaluation: most annotation scopes, including annotations, are lazily evaluated."
  - source_id: py314-reference-executionmodel-annotation-scopes
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, section Annotation scopes: since 3.14 annotation scopes are also used for annotations (Changed in version 3.14)."
---

## Short answer

**The scope of names defined in a class block is limited to the class block and does not extend to the class's methods.**[^py314-reference-executionmodel-resolution-of-names] Methods cannot reach class attributes through ordinary lexical lookup; explicit access such as `self.attr` or `ClassName.attr` is required. Exception: annotation scopes (type parameters, annotations) can access the class namespace.

## Detailed explanation

A class body runs as an ordinary block, and the names bound in it become attributes of the class (`Config.__dict__`). That block is not a lexical scope for nested functions, though: a name defined in a class block is visible only inside that class block. A method is a separate function, so a name in its body is looked up in the enclosing function scopes, then in the global namespace and the builtins, and the class block is skipped in that chain.[^py314-reference-executionmodel-resolution-of-names]

The example shows that a plain class-level name is not found from a method, while an attribute reached through `self` is:

```python
class Config:
    timeout = 30                  # stored in Config.__dict__

    def get_timeout(self):
        return timeout            # NameError when called: name 'timeout' is not defined

    def get_timeout_ok(self):
        return self.timeout       # found on the class through the instance
```

Calling `Config().get_timeout()` ends with a `NameError`. It is worse when the module has a global variable with the same name: the method silently uses that global instead of the class attribute. The same rule breaks a comprehension in a class body: with `factor = 2` in the class, `[v * factor for v in values]` raises `NameError` for `factor`, because the documentation explicitly includes comprehensions and generator expressions among the code that does not see the class block.[^py314-reference-executionmodel-resolution-of-names]

The exception is annotation scopes. In 3.14, parameter and return annotations run in an annotation scope that can see the class namespace and are evaluated lazily, so `def f(self, x: T) -> T` works next to `T = int` in the class, while the body of the same method cannot see `T`.[^py314-reference-executionmodel-resolution-of-names][^py314-reference-executionmodel-lazy-evaluation] In earlier versions, annotations were evaluated immediately in the class body. Either way they can see `T = int` from the class.[^py314-reference-executionmodel-annotation-scopes]

**Common mistakes:**
- assuming that a name from the class body is visible in methods as an ordinary variable; an attribute needs `self.attr` or `ClassName.attr`;
- missing that a global with the same name silently replaces the intended class attribute inside a method;
- applying the annotation exception to ordinary code in a method body.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
