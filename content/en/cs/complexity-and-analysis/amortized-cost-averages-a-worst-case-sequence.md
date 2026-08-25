---
id: cs-cmplx-0001
title: "What does amortized complexity guarantee, and what does it not?"
description: "Amortized cost averages a worst-case sequence of operations, not a distribution of inputs."
track: cs
section: complexity-and-analysis
level: junior
type: concept
tags: [amortized-analysis, complexity, dynamic-array]
status: published
updated: 2026-09-03
content_revision: 1
reconciled_with:
  uk: 1
see_also: [py-prac-0001]
anki:
  export: true
sources:
  - source_id: clrs-amortized-analysis
    title: "Introduction to Algorithms, 4th edition, chapter 16: Amortized Analysis"
    url: https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
    accessed: 2026-09-03
    kind: book
    version: "4th edition"
    applicability: "Aggregate, accounting and potential methods; language-independent."
  - source_id: cppreference-vector-push-back
    title: "cppreference: std::vector::push_back"
    url: https://en.cppreference.com/w/cpp/container/vector/push_back
    accessed: 2026-09-03
    kind: spec
    version: "C++20"
    applicability: "The amortized constant complexity that the standard requires of push_back, through C++20."
---

## Short answer

**Amortized complexity is the cost per operation averaged over a worst-case sequence**, not over a
distribution of inputs. A single operation may still be slow; the guarantee is that any sequence of
`n` operations costs `n` times the amortized bound.[^clrs-amortized-analysis] Appending to a dynamic
array is the standard example: a reallocation is linear, but it is rare enough that `push_back` is
amortized constant.[^cppreference-vector-push-back] Average-case complexity, by contrast, is
probabilistic and promises nothing about one particular run.

## Detailed explanation

Three different statements are easy to confuse.

*Worst case* bounds a single operation: no call ever costs more than this. *Average case* bounds the
expected cost of a single operation under an assumed distribution of inputs; if the real inputs are
distributed differently, the bound says nothing. *Amortized* bounds the total cost of a sequence and
divides it by the length of that sequence, with no assumption about inputs at all. Amortized analysis
is therefore a worst-case technique, which is why it survives adversarial input while average-case
analysis does not.[^clrs-amortized-analysis]

The dynamic array shows why the average over a sequence can be much better than the worst case of one
operation. Growing by doubling means that inserting `n` elements triggers reallocations at sizes
1, 2, 4, ..., up to `n`, and the elements copied add up to less than `2n`. Spread over `n` insertions
that is a constant per insertion, even though one individual insertion out of every power of two costs
linear time.[^cppreference-vector-push-back]

The constant factor of the growth policy matters, but only for memory. Doubling wastes up to half the
allocated buffer; growing by 1.5 wastes less and still keeps the amortized bound constant, because any
growth factor strictly greater than one gives a geometric series. Growing by a fixed number of slots
does not: the copies then add up to a quadratic total, and the amortized cost per insertion becomes
linear.

The practical consequence is about latency, not throughput. An amortized constant bound is compatible
with an individual call that stalls for milliseconds, which is why real-time and interactive systems
either reserve capacity up front or use a container with a true per-operation worst-case bound.

## Sources

<!-- generated from frontmatter -->
