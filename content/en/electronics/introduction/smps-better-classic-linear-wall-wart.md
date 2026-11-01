---
id: emb-elintro-0179
title: "Why is an `SMPS` better than a classic linear wall-wart?"
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
  - source_id: adi-linear-switching
    title: "Analog Devices: Basic Concepts of Linear Regulator and Switching Mode Power Supplies"
    url: https://www.analog.com/en/resources/app-notes/2020/05/12/19/12/an-140.html
---

## Short answer

An `SMPS` switches power transistors, so it typically has lower losses and can be more compact than a linear supply of the same power rating. However, efficiency, size, noise, and input voltage range depend on the specific design; none of the quoted figures is universal.[^adi-linear-switching]

## Detailed explanation

An `SMPS` (switch-mode power supply) regulates voltage by rapidly switching a power transistor and transferring energy through inductive and capacitive elements. When the transistor is on, the voltage drop across it is small; when it is off, the current through it is small. Because voltage or current is simultaneously small in these states, losses can be lower than in a linear regulator, where excess voltage is converted into heat.[^adi-linear-switching]

High switching frequency allows using smaller magnetic components, so many SMPS adapters are lighter and more compact than older transformer-based linear adapters of comparable power. This does not mean every SMPS is better than every linear supply: a linear design is often simpler and can have lower high-frequency noise, while efficiency depends on the ratio of input to output voltage, the load, and the implementation.[^adi-linear-switching]

Ranges cited in older flashcards such as `85–90%` for an SMPS and `50–70%` for a linear wall-wart cannot be treated as general characteristics of the classes. For a specific adapter, check the datasheet specifications and efficiency-versus-load curves. Likewise, compatibility with a `100–240 V` mains must be explicitly stated on the label; it does not follow merely from the supply being switch-mode.[^adi-linear-switching]

**Example:** for a linear regulator dropping `12 V` to `3.3 V` at the same current, approximate efficiency ignoring quiescent consumption is limited by the ratio `3.3/12`, or `27.5%`. In the Analog Devices example, a synchronous buck converter under the same voltages can exceed `90%`; this illustrates topology and operating conditions, not a specification for any wall adapter.[^adi-linear-switching]

**Common mistake:** comparing categories using fixed percentages or automatically attributing a universal input to an SMPS. One compares specific models by efficiency at the required load, noise, regulation, safety, and input marking.[^adi-linear-switching]
