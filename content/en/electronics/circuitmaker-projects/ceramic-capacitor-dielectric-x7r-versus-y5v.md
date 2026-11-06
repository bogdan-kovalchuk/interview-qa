---
id: emb-elcmproj-0013
title: "Why is X7R ceramic significantly better than cheap Y5V dielectric in frequency-determining circuits?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: tdk-mlcc-characteristics
    title: "TDK Corporation. Technical Note: DC Bias Characteristics and Temperature Characteristics of Ceramic Chip Capacitors"
    url: https://product.tdk.com/en/contact/faq/capacitors-0010.html
  - source_id: kemet-dielectric-classes
    title: "KEMET Electronics. Ceramic Chip Capacitors: Understanding EIA Class I, II, and III Dielectrics"
    url: https://www.kemet.com/en/us/technical-resources.html
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill. The Art of Electronics, 3rd Edition, Cambridge University Press"
    url: https://artofelectronics.net/
---

## Short answer

X7R ceramic dielectric maintains capacitance stability within `±15%` across temperatures from `-55 °C` to `+125 °C`. In contrast, inexpensive Y5V capacitors can lose up to `80%` of their rated capacitance over temperature or under DC voltage bias. This capacitance collapse causes frequency drift and severe timing instability in oscillator circuits.[^tdk-mlcc-characteristics]

## Detailed explanation

TODO
