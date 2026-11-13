---
id: emb-elcirc-0005
title: "How do you test a potentiometer with a multimeter?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-ohmmeter-usage
    title: "All About Circuits: How to Use an Ohmmeter to Measure Resistance"
    url: https://www.allaboutcircuits.com/textbook/experiments/chpt-2/ohmmeter-usage/
  - source_id: aac-potentiometer-rheostat
    title: "All About Circuits: DC Lab – Potentiometer as a Rheostat"
    url: https://www.allaboutcircuits.com/TEXTBOOK/experiments/chpt-3/potentiometer-rheostat/
---

## Short answer

Turn off power and measure the resistance between the two outer terminals: it should remain constant and match the nominal value within tolerance.[^aac-ohmmeter-usage] [^aac-potentiometer-rheostat] Next, measure between the wiper and each end terminal while sweeping the control smoothly; the readings should vary inversely, and sudden jumps or open circuits reveal wiper contact wear or contamination.[^aac-potentiometer-rheostat]

## Detailed explanation

To measure resistance, switch the multimeter to resistance mode (Ω) and connect the test leads across the two terminals of interest. First, remove all power from the circuit: an ohmmeter supplies its own small test current, so resistance must never be measured on an energized circuit. If the potentiometer is soldered into a board, parallel components provide alternate current paths that distort readings; for a dependable measurement, disconnect at least one terminal from the circuit.[^aac-ohmmeter-usage]

Measuring across the two end terminals of the resistive track yields its full nominal resistance, which should not vary noticeably with wiper position. The reading will not necessarily match the marked nominal value exactly: account for component manufacturing tolerance, meter accuracy, and test lead resistance. If the meter displays an open circuit (`OL`) or a value far outside tolerance, verify probe contact, correct meter range, and component markings before concluding that the part is defective.[^aac-potentiometer-rheostat]

Next, measure resistance between the wiper and one end terminal. As you slowly turn the shaft or slide the actuator from one end to the other, you should observe a smooth, continuous transition from near zero to nearly the full track resistance. Measuring between the wiper and the opposite end terminal shows the inverse progression: as one resistance increases, the other decreases. Near travel limits, a small residual contact resistance is normal due to wiper terminal construction.[^aac-potentiometer-rheostat]

Sweep the control slowly and observe the display across the entire sweep rather than checking only the end stops. A momentary `OL`, dead spots, or sudden jumps that recur at the same mechanical position suggest track contamination, resistive film wear, or erratic wiper contact. A single isolated spike may simply be caused by probe slipping, so ensure stable probe contact and repeat the test. While this check identifies electrical open circuits and wiper degradation, it does not evaluate mechanical play or rotational lifecycle wear.[^aac-potentiometer-rheostat]

**Common mistakes:**

- Measuring resistance while the circuit is powered.
- Expecting a varying resistance reading between the two end terminals rather than the full track resistance.
- Treating any deviation from marked nominal resistance as a defect without accounting for component tolerance and parallel in-circuit paths.
