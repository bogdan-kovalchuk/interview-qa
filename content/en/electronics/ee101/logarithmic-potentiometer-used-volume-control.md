---
id: emb-elee-0014
title: "Why is a logarithmic potentiometer used for volume control?"
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
  - source_id: analog-devices-taper
    title: "Analog Devices: Taper"
    url: https://www.analog.com/en/resources/glossary/logarithmic_linear_taper.html
---

## Short answer

Human perception of loudness is approximately logarithmic, so an audio taper adjusts signal levels more gradually at lower settings and more rapidly at higher settings. This typically yields subjectively smoother volume adjustment, although exact performance depends on the potentiometer curve and audio circuit topology.[^analog-devices-taper]

## Detailed explanation

A logarithmic potentiometer is used for volume control so that knob rotation better matches human perception of sound level changes. Human perception is non-linear: an identical absolute change in amplitude is not perceived identically at quiet versus loud listening levels. An audio taper creates a non-linear relationship between resistance and angle, resulting in a non-linear signal change at the divider output.[^analog-devices-taper]

In a typical audio taper, signal adjustment across the lower portion of travel is more gradual, enabling finer control at low volume; higher up, the level changes more rapidly. This makes the control more user-friendly, but it does not mean the mechanical angle directly determines perceived loudness: the outcome is influenced by potentiometer loading, amplifier input impedance, circuit topology, and acoustic conditions.[^analog-devices-taper]

In a physical component, the logarithmic curve is an approximation and may be composed of several piecewise linear segments. Therefore, the center position of the knob corresponds to neither half the output voltage nor half the subjective loudness. When precise decibel control or tight stereo tracking is required, one should check the specific model curve or use an active or digital attenuator.[^analog-devices-taper]

Example: in a voltage divider, a linear taper potentiometer produces an output voltage approximately proportional to rotation angle, whereas an audio taper intentionally alters this relationship so the knob response feels more natural to the ear. In an actual audio signal path, loading will modify the curve shape, so the expected behavior should be verified in circuit.[^analog-devices-taper]

**Common mistake:** claiming that the human ear is perfectly logarithmic or that a logarithmic potentiometer guarantees a linear sensation of volume. It is a practical approximation rather than an exact psychoacoustic law.[^analog-devices-taper]
