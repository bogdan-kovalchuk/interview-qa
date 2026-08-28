---
id: eng-cicd-0002
title: "When should you choose rolling, blue-green, or canary deployment, based on blast radius, traffic control, and rollback speed?"
description: "When should you choose rolling, blue-green, or canary deployment, based on blast radius, traffic control, and rollback speed?"
track: engineering
section: ci-cd
level: middle
type: comparison
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: git-git-merge
    title: "Git docs: Git Merge"
    url: https://git-scm.com/docs/git-merge
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official Git documentation."
  - source_id: git-git-rebase
    title: "Git docs: Git Rebase"
    url: https://git-scm.com/docs/git-rebase
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official Git documentation."
  - source_id: git-git-revert
    title: "Git docs: Git Revert"
    url: https://git-scm.com/docs/git-revert
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official Git documentation."
  - source_id: git-git-reset
    title: "Git docs: Git Reset"
    url: https://git-scm.com/docs/git-reset
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official Git documentation."
  - source_id: git-git-reflog
    title: "Git docs: Git Reflog"
    url: https://git-scm.com/docs/git-reflog
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official Git documentation."
  - source_id: github-continuous-integration
    title: "GitHub Docs: Continuous Integration"
    url: https://docs.github.com/en/actions/get-started/continuous-integration
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official GitHub documentation."
  - source_id: gcloud-deployment-strategies
    title: "Google Cloud docs: Deployment Strategies"
    url: https://docs.cloud.google.com/deploy/docs/deployment-strategies
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official Google Cloud documentation."
  - source_id: google-standard
    title: "Google Engineering Practices: Standard"
    url: https://google.github.io/eng-practices/review/reviewer/standard.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official Google Engineering Practices material."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/development/ci_cd.md#L61-L95
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Rolling – gradual instance updates with no downtime, a simple but slow rollback; blue-green –
two full environments with an instant rollback via a traffic switch; canary – the smallest blast
radius through progressively growing the share of traffic sent to the new version.**
[^git-git-merge] Rolling fits ordinary releases where simplicity and zero downtime are what
matter. Blue-green fits cases where rollback speed is critical (a load-balancer switch in seconds)
and there are resources for a fully duplicated environment. Canary fits risky changes (for example,
payment logic), where the new version must first be checked against a small slice of users before
the traffic is grown further.

## Detailed explanation

A deployment strategy determines how a new version of a service replaces the old one in
production, and how much traffic reaches each version at the same time during the
rollout.[^gcloud-deployment-strategies]

Rolling deployment sequentially replaces old instances with new ones, in small batches, until the
whole fleet is updated. There is no downtime, because some instances always keep serving traffic,
but rollback requires the same gradual process in reverse, so it is slow, and for a while the old
and the new code run side by side.

Blue-green keeps two fully identical environments (blue – the current one, green – the new one)
and switches all traffic in one atomic step at the load-balancer or DNS level. Rollback is the same
switch in reverse, so it takes seconds, but the price is double the resources for the whole
duration of the rollout.

Canary first routes a small percentage of traffic to the new version (for example, 1-5%), watches
error and latency metrics, and only then grows the share gradually. The blast radius is the
smallest of the three approaches, because a bug in the new version affects a small slice of users
before it is caught and rolled back.

An example of a canary configuration that routes 5% of traffic to the new version:

```yaml
# istio VirtualService: 95% to stable, 5% to canary
http:
  - route:
      - destination: {host: svc, subset: stable}
        weight: 95
      - destination: {host: svc, subset: canary}
        weight: 5
```

**Common mistakes when choosing a deployment strategy:**
- choosing blue-green for a service where doubling resource cost is unacceptable;
- running a canary without real metrics and alerts – without observability, progressively growing
  the traffic share gives no advantage over rolling;
- treating rolling deployment as safe for database schema changes, even though the old and the new
  code run against the same database at the same time for a while.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
