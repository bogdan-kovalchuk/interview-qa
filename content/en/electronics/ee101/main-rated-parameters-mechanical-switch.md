---
id: emb-elee-0010
title: "What are the main rated parameters of a mechanical switch?"
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
  - source_id: omron-basic-switch-terms
    title: "OMRON: Basic Switches, Explanation of Terms"
    url: https://www.ia.omron.com/support/guide/29/explanation_of_terms.html
  - source_id: omron-basic-switch-spec
    title: "OMRON: X General-purpose Basic Switch, Specifications"
    url: https://www.ia.omron.com/products/family/291/specification.html
---

## Short answer

The primary switch parameters include rated voltage and current for specified load types, initial contact resistance, insulation resistance, dielectric strength, and mechanical and electrical endurance. Values depend on the specific model and test conditions; there are no universal limits such as "under 50 mΩ" or a fixed cycle lifespan.[^omron-basic-switch-terms]

## Detailed explanation

Rated switch parameters describe what circuit it can switch and how its insulation and contacts behave under defined conditions. Rated voltage and current must always be evaluated together: the manufacturer specifies them for a particular load type, such as resistive, and may list separate ratings for AC and DC. Inductive or lamp loads involve different inrush currents and arcing upon opening, so matching the operating voltage and current numbers printed on the package does not by itself guarantee suitability.[^omron-basic-switch-terms]

Contact resistance characterizes closed contacts and influences voltage drop and heating; its value is typically quoted as an initial value under specified test conditions. Insulation resistance applies to open contacts or isolated conductive parts, while dielectric strength specifies the test voltage and duration that the insulation must withstand without breakdown. These are distinct characteristics: high insulation resistance does not replace dielectric strength verification.[^omron-basic-switch-terms]

Mechanical endurance counts operations of the mechanism, whereas electrical endurance counts switching cycles under a specified electrical load; the latter is often much lower. In the Omron catalog for a specific basic switch, the specifications list 1,000,000 mechanical operations and 100,000 electrical operations, 15 mΩ initial contact resistance, and a minimum of 100 MΩ insulation resistance at 500 VDC. This is an example of a single model, not a universal benchmark for all switches.[^omron-basic-switch-spec]

Selection example: when switching a motor, check the rating specifically for inductive loads, permissible inrush current, electrical endurance, and arc suppression methods. Exceeding the rating can cause contact welding or accelerated wear even if the switch continues to click mechanically.

**Common mistake:** comparing only maximum amps and volts and extrapolating contact resistance or endurance from one catalog example to all switches. One must check the specific model datasheet, load type, switching frequency, and the conditions under which values are specified.[^omron-basic-switch-spec]
