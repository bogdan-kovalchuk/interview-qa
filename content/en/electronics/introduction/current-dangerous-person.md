---
id: emb-elintro-0047
title: "What current is dangerous to a person?"
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
  - source_id: osha-electricity-safety
    title: "OSHA: Basic Electricity Safety"
    url: https://www.osha.gov/sites/default/files/2019-04/Basic_Electricity_Materials.pdf
---

## Short answer

Dangerous current does not have a single exact threshold: around `10 mA` can already cause strong muscle contractions and loss of control, while a current on the order of tens of milliamperes through the chest can be lethal. The risk depends on the current path, duration, frequency, and contact condition, so these figures do not represent a sharp safety boundary.[^osha-electricity-safety]

## Detailed explanation

The consequences of electric shock are determined by the current that actually passes through the body, rather than merely the source voltage. Current depends on voltage and the total path impedance, including skin and contact points; wet skin or damaged contact can reduce resistance. Duration, AC frequency, and the trajectory through the body are also critical, particularly if the path passes through the chest.[^osha-electricity-safety]

One cannot name a single figure below which current is guaranteed to be safe for every individual. OSHA materials note that a current of around `10 mA` can already cause muscle contractions and loss of voluntary muscle control in the hand; in their table, the range `50–150 mA` is associated with severe pain, respiratory arrest, and possible death. These are reference points for understanding danger rather than sharp biological limits: human sensitivity and contact conditions vary.[^osha-electricity-safety]

The statement "100 mA stops the heart" is overly categorical. Such a current can cause ventricular fibrillation along certain paths and durations, but safe current cannot be derived from a single number; even lower levels can prevent letting go of a conductor, prolonging the shock. In practical work, safety is never checked by touch, and work is not performed on exposed energized parts.

**Example:** if a multimeter is set to current measurement mode, its inputs have very low resistance. Connecting such a meter in parallel across a power source can create a low-resistance short-circuit path and damage the instrument or circuit; to measure voltage, one selects voltage mode and connects the meter in parallel across the circuit branch under test.
