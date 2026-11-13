---
id: emb-elee-0186
title: "What should you check if the measured noise changes when you move the probe?"
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
  - source_id: tektronix-abcs-probes
    title: "Tektronix: ABCs of Probes Primer"
    url: https://download.tek.com/document/02_ABCs-of-Probes-Primer.pdf
---

## Short answer

Check the probe ground lead loop geometry: a long alligator ground lead acts as a single-turn loop antenna and picks up radiated noise from nearby fast-switching signals. Test whether the observed noise waveform changes when moving the lead; use a short ground spring contact near the test point and compare results under identical oscilloscope settings.[^tektronix-abcs-probes]

## Detailed explanation

If the noise changes when the probe is moved while the signal at the measurement point itself does not change, interference is being coupled into the probe circuit. The ground lead connects the oscilloscope ground to a ground point on the circuit near the probe tip. Together with the probe tip, it forms a single-turn loop, effectively an antenna. Such a loop is especially sensitive to electromagnetic interference from logic circuits and fast-switching signals on neighboring traces, and the induced voltage adds to the signal at the probe tip.[^tektronix-abcs-probes]

Testing separates interference picked up by the lead from the real signal. Move the ground lead around the board: if the noise level changes, the interference is being induced in the lead itself. Checking the cable works similarly: a properly grounded probe does not respond to the position of the cable or to touching it. If ringing changes frequency when shortening the lead, it is caused by the probe grounding; if the frequency does not change, the source is likely in the circuit itself.[^tektronix-abcs-probes]

The cause lies in the inductance of a long wire. A shorter wire has lower inductance, shifting ringing to a higher frequency that may fall outside the oscilloscope bandwidth (making ringing invisible) and reducing induced pickup. The best option is a short ground spring contact directly next to the measurement point or an adapter with a ground collar near the probe tip. Extending the wire or grounding it via a separate lead is ill-advised: inductance increases and ringing can appear.[^tektronix-abcs-probes]

A distinct case is a ground loop between the oscilloscope and the circuit when they are powered from different building ground points. Current circulating in such a loop produces a voltage drop across the probe ground lead, appearing as 50 Hz or 60 Hz noise or spikes from mains equipment like air conditioners. It can be mitigated by powering the oscilloscope and circuit from the same outlet branch, as well as by using a differential or optically isolated probe.[^tektronix-abcs-probes]

**Common mistakes:**
- Assuming that a change in noise when moving the probe indicates a circuit problem: first check the lead itself.
- Extending the ground lead or connecting it to an alternate ground point: ringing appears that is easily mistaken for a signal.[^tektronix-abcs-probes]
- Comparing noise under different oscilloscope settings: changing bandwidth or scale alters what is displayed.
