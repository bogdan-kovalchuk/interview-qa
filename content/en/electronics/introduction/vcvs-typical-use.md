---
id: emb-elintro-0081
title: "What is a VCVS and what is its typical use?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: aac-dependent-sources
    title: "All About Circuits: Nodal Analysis and Dependent Sources"
    url: https://www.allaboutcircuits.com/technical-articles/nodal-analysis-and-dependent-sources/
---
## Short answer

A VCVS (Voltage-Controlled Voltage Source) is an idealized dependent source in which the output voltage is proportional to a control voltage: `V_out = A_v*V_control`. An op-amp model is often represented as a VCVS with a large open-loop gain, but a real op-amp is a complex circuit, not the ideal source itself.[^aac-dependent-sources]

## Detailed explanation

A VCVS belongs to dependent sources: in a schematic, its output voltage is not set by a constant battery, but is determined by another voltage in the circuit. For a linear model, the relationship is written as `V_out = A_v*V_control`, where `A_v` is a dimensionless transfer coefficient and `V_control` is measured between specified control nodes. The polarity of the source and the sign of the coefficient determine whether the output tracks the control voltage or inverts it.[^aac-dependent-sources]

A VCVS is useful in circuit analysis because it allows describing amplification without modeling every transistor. For example, in SPICE it can approximate an op-amp's output relationship: a large open-loop gain multiplies the voltage difference at the inputs. This is an idealization; the source in a simple model may lack the power supply limits, output current limits, bandwidth, or slew rate present in a real component.[^aac-dependent-sources]

In feedback, a negative signal from the output is returned to the input to reduce the difference between the control inputs. Resistors or other elements set the fraction of the output voltage that is returned, and the high open-loop gain forces the closed-loop circuit to maintain a small error as long as it operates in the linear region. If the output hits a supply rail or the load demands excessive current, this condition is no longer satisfied, and the simple gain formula no longer describes the result.[^aac-dependent-sources]

Example: for `A_v = 10` and a control voltage `V_control = 0.2 V`, the ideal model yields `V_out = 2 V`. This does not guarantee that a real op-amp can output 2 V: you check its power supply, permissible input and output ranges, and load. Common mistake – calling any op-amp a VCVS; it is more accurate to say that a VCVS is a useful model of its amplifying behavior.[^aac-dependent-sources]
