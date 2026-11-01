---
id: emb-elintro-0162
title: "What is the depletion region of a P-N junction?"
track: electronics
section: introduction
sources:
  - source_id: aac-pn-junction
    title: "All About Circuits: The P-N Junction"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-2/the-p-n-junction/
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

The depletion region of a P-N junction is the zone near the interface where recombination has reduced the concentration of mobile majority carriers. Immobile ionized impurities remain in it, creating an internal electric field. For silicon, there is no single fixed threshold of 0.7 V: forward current rises smoothly, and the forward voltage drop depends on current, temperature, and the specific diode.[^aac-pn-junction]

## Detailed explanation

A depletion region arises when P and N regions meet in a single crystal. Due to the concentration difference, electrons diffuse from the N region to the P region, and holes diffuse in the opposite direction. Near the boundary they recombine, so fewer mobile majority carriers remain there. This is not a void or an insulator layer, but part of the crystal with immobile charged impurity atoms.[^aac-pn-junction]

After recombination, positively charged donor ions remain on the N side near the boundary, while negatively charged acceptor ions remain on the P side. Their field opposes further diffusion and forms a potential barrier. In thermal equilibrium, diffusion motion and carrier drift in this field balance each other; thus, the junction is not an ideal open circuit.[^aac-pn-junction]

External forward bias reduces the barrier and narrows the depletion region, so significant current can flow through the junction. Reverse bias increases the barrier and widens this region; a small minority carrier current remains until breakdown occurs. The thickness of the region depends on the material, doping level, and applied voltage, rather than being an immutable geometric quantity.[^aac-pn-junction]

A figure of about 0.6–0.7 V is often cited as a guide for the forward voltage drop of a silicon diode at a certain operating current. It does not mean that current is zero below this value and conduction appears instantaneously above it. Likewise, the built-in potential of the junction should not be equated with a universal turn-on voltage: the actual current-voltage characteristic is continuous.[^aac-pn-junction]

**Common mistakes:**
- Calling the depletion region completely charge-free: mobile carriers are scarce there, but fixed ions create a field.
- Considering 0.7 V an exact threshold for all silicon junctions.
- Claiming that reverse bias gives absolutely zero current: a leakage current exists until breakdown.[^aac-pn-junction]

Visualizing a cross-section of the junction under forward bias helps explain why the region narrows, and under reverse bias – why it widens. But the exact width and current require parameters of the specific material and diode.[^aac-pn-junction]
