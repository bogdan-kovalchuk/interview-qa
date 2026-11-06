---
id: emb-eldig-0015
title: "How are rise time, fall time, and propagation delay measured on a timing diagram?"
track: electronics
section: digital-logic
sources:
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd. Digital Fundamentals, 11th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003295
  - source_id: sedra-smith-microelectronic-circuits
    title: "Adel S. Sedra, Kenneth C. Smith. Microelectronic Circuits, 7th Edition"
    url: https://global.oup.com/ushe/product/microelectronic-circuits-9780199339143
  - source_id: ti-input-output-characteristics
    title: "Texas Instruments. Designing with Logic: Input and Output Characteristics"
    url: https://www.ti.com/lit/an/sdya010/sdya010.pdf
---

## Short answer

Rise time `t_r` is measured between 20% and 80% (or 10% and 90%) of signal amplitude, while fall time `t_f` is measured between 80% and 20% (or 90% and 10%). Propagation delay between input and output edges is measured between their 50% voltage points. Using the 50% threshold provides a consistent, standardized timing reference regardless of edge transition rates.[^floyd-digital-fundamentals]

## Detailed explanation

TODO
