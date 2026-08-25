---
id: bhv-team-0001
title: "Tell me about a technical disagreement with a colleague and how it ended"
description: "The question is about how a decision was reached, not about who turned out to be right."
track: behavioral
section: teamwork-and-conflict
level: middle
type: behavioral
tags: [conflict, disagree-and-commit, decision-making, communication]
status: published
updated: 2026-09-04
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: amazon-leadership-principles
    title: "Amazon leadership principles: Have Backbone; Disagree and Commit"
    url: https://www.amazon.jobs/content/en/our-workplace/leadership-principles
    accessed: 2026-09-03
    kind: official
    version: null
    applicability: "The behaviour this principle names as expected at Amazon; other companies phrase the same expectation differently or not at all."
  - source_id: crucial-conversations-3e
    title: "Crucial Conversations: Tools for Talking When Stakes Are High, 3rd edition"
    url: https://www.mheducation.com/highered/product/crucial-conversations-tools-talking-when-stakes-are-high-third-edition-grenny-mcmillan/9781260474183.html
    accessed: 2026-09-03
    kind: book
    version: "3rd edition"
    applicability: "General technique for high-stakes disagreement: separating observation from conclusion, and stating a shared goal before a position."
---

## Short answer

**Answer with the mechanism by which the disagreement was resolved, not with the verdict.** Name the
decision at stake, then what you did to make it cheap to settle: agreeing in advance on the evidence
that would decide it. Say what you did once the decision went against you, because committing visibly
to a lost argument is the behaviour being probed.[^amazon-leadership-principles] Keep the colleague
recognisable as competent; a story where the other side is foolish answers a different question.

## Detailed explanation

The question looks like it is about conflict. It is about whether disagreement with you is safe and
productive for the people around you, which is a property of behaviour, not of opinions.

Three things make an answer weak regardless of how the story ended. Choosing a disagreement with no
real stakes, so nothing is revealed. Framing it as a competence gap in the other person, which tells
the interviewer what disagreeing with you is like. And ending at "and I was right", which leaves the
question of what happens when you are not.

What makes an answer strong is a decision procedure. Interviewers listen for whether the candidate
converted an argument about opinions into a question about evidence: a benchmark, a spike, a
reversible trial, a written comparison, or an agreed escalation to whoever owns the decision. Agreeing
on what would change your mind, before gathering it, is the move that separates people who can work
through disagreement from people who can only win or lose it.[^crucial-conversations-3e]

The second half matters as much as the first. Organisations that name this behaviour explicitly ask
for both parts: argue the position honestly, then commit fully to the decision that is
taken.[^amazon-leadership-principles] A candidate who quietly kept working their preferred way, or who
relitigated the decision for months, has answered the question in the negative without noticing.

Prepare one real story with genuine stakes where you can describe the other position fairly. Two is
better: one you won and one you lost, since the follow-up almost always asks for the other kind.

## Competency assessed

- **Collaboration under disagreement:** whether a technical dispute stays about the technical question
  and remains safe for the other party.
- **Decision hygiene:** whether the candidate can convert an opinion clash into an evidence question
  and identify who owns the decision.
- **Commitment after a lost argument:** whether a decision they argued against still gets their full
  execution.[^amazon-leadership-principles]
- **Communication:** whether they can state a position clearly, hear the strongest form of the
  opposing one, and describe both fairly afterwards.
- **Self-awareness:** whether they can name their own contribution to the friction.

## STAR outline or illustrative example

The example below is **illustrative, not a personal account**. It shows the shape of a strong answer.
Use your own experience: presenting someone else's story as your own is detectable in follow-up
questions and is a disqualifying answer, not a risky one.

**Situation.** Two engineers on a four-person service team disagreed on how to fix an endpoint that
had grown to a two-second response time. One wanted a caching layer in front of it; the other wanted
to fix the query pattern first. Both had estimates, neither had measurements, and the sprint had
capacity for one.

**Task.** As the second engineer, produce a decision the team would actually execute, within two days,
without turning a technical question into a standoff.

**Action.** Stated the shared goal first, that the endpoint be reliably under 300 ms, and got explicit
agreement that this, and not the choice of approach, was what they were both arguing for. Proposed a
single measurement to decide between them: instrument one request end to end and see where the two
seconds sat. Agreed in advance, in writing, what each outcome would imply, so neither could reinterpret
the result afterwards. The measurement showed most of the time in repeated queries rather than in the
work per query, which favoured fixing the query pattern; it also showed a slow third-party call that
neither approach addressed, and that the cache would in fact have helped.

**Result.** The query fix landed that sprint and took the endpoint to roughly 400 ms, which is a
large improvement but still short of the 300 ms goal we had agreed on; said so openly rather than
declaring the ticket done. The caching proposal was kept for the third-party call and implemented
later by the engineer who had proposed it, which is what finally closed the gap.
The instrumentation stayed in place and settled two later arguments without a meeting.

**Reflection.** The measurement should have come before the argument. The team adopted a small rule
afterwards: a performance disagreement lasting more than one conversation gets instrumented rather
than continued, and the measurement is agreed by both sides before it is run.

## Follow-up prompts

- Tell me about a disagreement you lost. What did you do once the decision was made?
- What did the other person think the trade-off was? Put their case as strongly as they would.
- How would you have handled it if there had been no way to measure the difference?
- What was your part in the disagreement lasting as long as it did?
- Has the decision been revisited since? What would make you reopen it?
- How does this change when the other person is more senior than you, or is your report?

## Evaluation guide

### Expected signals

- Describes the other position accurately and in its strongest form, not as a mistake to be corrected.
- Names a concrete mechanism used to settle it: evidence agreed on in advance, a bounded experiment,
  a written comparison, or escalation to the decision owner.
- States the outcome plainly, including when the decision went against them, and what they did next.
- Separates observation from conclusion when recounting the conflict, rather than reporting inferred
  motives as facts.
- Shows some cost to themselves: time spent, a position revised, a concession made.

### Red flags

- Every disagreement in the story is resolved by the candidate being right.
- The colleague is portrayed as incompetent, junior or irrational; no version of their reasoning is
  offered.
- The resolution is authority alone: "I escalated to the manager", with no attempt before that.
- Committed to the decision in words and worked around it in practice.
- Cannot name what would have changed their mind, either then or now.

### Level-up follow-up

Ask for a disagreement they lost and still believe they were right about, and what they did with that
belief. The strong answer distinguishes disagreeing with a decision from undermining it, and can point
to what evidence would reopen the question and under what conditions raising it again would be
appropriate.

## Sources

<!-- generated from frontmatter -->
