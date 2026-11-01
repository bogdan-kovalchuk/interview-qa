---
id: emb-elintro-0063
title: "Why should batteries in a series string have the same capacity and state of charge?"
track: electronics
section: introduction
sources:
  - source_id: victron-series
    title: "Victron Lithium Battery Smart – Installation"
    url: https://www.victronenergy.com/media/pg/Lithium_Battery_Smart/en/installation.html
  - source_id: panasonic-mixing
    title: "Panasonic eneloop FAQ"
    url: https://www.panasonic.com/global/energy/products/eneloop/en/faq.html
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

In a series string, the same current flows through each battery, so total voltage adds up, while capacity in Ah does not add up: it is limited by the battery with the lowest available capacity.[^victron-series] Differing states of charge or capacities cause imbalance, so manufacturers typically require matched batteries and compliance with system-specific guidelines.[^panasonic-mixing]

## Detailed explanation

In a series connection, the positive terminal of one battery is connected to the negative terminal of the next. Current is identical through all cells, and the battery voltages add up. Capacity in ampere-hours does not add up because each cell must pass the same charge; when the smallest cell exhausts its available capacity, discharging the entire string must stop.[^victron-series]

**Example:** if a 50 Ah battery and a 100 Ah battery are connected in series, the entire string is theoretically limited to about 50 Ah, not 150 Ah. In a real system, the outcome may be worse: parameter differences cause imbalance, and the weaker cell reaches its charge or discharge limit first.[^victron-series]

Identical initial state of charge alone does not make batteries interchangeable. Their actual capacity depends on chemistry, age, temperature, operating history, and load profile. Victron recommends batteries of the same capacity and model for series systems; Panasonic warns against mixing types, capacities, brands, and ages in devices, as discrepancies can lead to overdischarge and leakage.[^victron-series] [^panasonic-mixing]

During charging, the issue is equally critical: cells in the string receive the same current, but their voltages do not rise uniformly. One cell may reach its upper voltage limit earlier while another is not yet fully charged; battery packs therefore require a manufacturer-specified charger and, where designed, a BMS or balancing circuitry.[^victron-series]

**Common mistake:** confusing series and parallel connections. Series increases total voltage but does not add Ah; parallel maintains voltage and can increase Ah with compatible batteries and manufacturer approval.

Before assembling a pack, verify chemistry, rated capacity, model, and manufacturer requirements. Do not mix new and degraded cells simply because their voltages match right now: open-circuit voltage does not indicate equal available capacity.
