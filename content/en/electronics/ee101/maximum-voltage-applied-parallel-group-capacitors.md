---
id: emb-elee-0028
title: "What is the maximum voltage that can be applied to a parallel group of 10 V and 25 V capacitors?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: aac-capacitors-series-parallel
    title: "All About Circuits textbook: Series and Parallel Capacitors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/series-and-parallel-capacitors/
---

## Short answer

For this capacitor pair, the maximum voltage applied across the group cannot exceed 10 V, because parallel components share identical voltage. This represents the component rating limit; practical circuits must also account for supply tolerances, ripple, transient surges, and voltage derating requirements.[^aac-capacitors-series-parallel]

## Detailed explanation

In a parallel connection, each capacitor is connected to the same pair of nodes; therefore, the voltage across each is identical.[^aac-capacitors-series-parallel]

For capacitors rated at 10 V and 25 V, the voltage across both will be the supply voltage. If the supply exceeds 10 V, the element with the lower rating will operate beyond its rated limits, even though the second capacitor is still operating within its 25 V limit. Based on these ratings alone, therefore, the upper limit for the group is 10 V, not 25 V and not the sum of the two values.[^aac-capacitors-series-parallel]

This does not mean that 10 V is always an appropriate operating setpoint. The component rating must be compared against the actual voltage, its ripple, and possible transient spikes; the margin is determined by capacitor chemistry, temperature, reliability goals, and manufacturer requirements. A polarized capacitor must also be connected with the correct polarity if that requirement applies to the chosen type. Group-level calculations do not waive the individual limits of the weakest element.[^aac-capacitors-series-parallel]

Example of verifying the supply:

```text
V_source_max = 9.0 V + 0.5 V ripple + 0.8 V transient
V_source_max = 10.3 V
```

Under such specified maximums, the 10-volt capacitor may already be overstressed; this arithmetic merely illustrates checking the aggregate worst case and does not dictate a universal derating margin. Before assembly, verify the allowable operating conditions of the specific component.[^aac-capacitors-series-parallel]

**Common mistake:** designing around the higher-rated capacitor or adding voltage ratings together. To avoid this, first establish the circuit topology, then compare the shared voltage against each component's rating, and check the peak source voltage.
