---
id: emb-elintro-0002
title: What is the key difference between an analog and a digital signal?
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
  - source_id: ti-pam4
    title: "TI SNAA325A: PAM-4 signaling"
    url: https://www.ti.com/lit/an/snaa325a/snaa325a.pdf
---

## Short answer

An analog signal represents information through a continuously varying quantity; a digital signal uses a discrete set of symbols. Binary logic commonly uses LOW and HIGH, but digital signaling can use more than two levels: PAM-4 uses four levels carrying two bits per symbol. [^ti-pam4]

## Detailed explanation

The distinction concerns how information is represented and interpreted. An analog voltage may encode a measured temperature over a continuous range. A digital receiver assigns the received waveform to one of a finite set of symbols. The electrical voltage itself still changes continuously during transitions; it does not become a physically discrete quantity.

In binary signaling, two recognized states encode 0 and 1. PAM-4 is a counterexample to the rule that every digital signal has only two voltage levels: four symbol levels encode two bits per symbol. Thus “digital” is broader than “binary.” [^ti-pam4]

A signal can also be discrete in time without being binary in amplitude. Sampling chooses observation times; quantization chooses representable amplitude values. Keep these two operations separate when explaining an ADC. A digital representation enables processing of symbols, but does not by itself guarantee immunity to electrical noise.
