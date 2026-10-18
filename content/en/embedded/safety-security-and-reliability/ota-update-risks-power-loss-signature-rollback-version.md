---
id: emb-boot-0007
title: "What is OTA update and what risks must be covered: power loss, signature verification, rollback, and version compatibility?"
track: embedded
section: safety-security-and-reliability
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: mcuboot-design
    title: "MCUboot design documentation"
    url: https://docs.mcuboot.com/design.html
---

## Short answer

**OTA** – firmware update over a network without physical access to the device. Requires atomic install, image integrity, signature verification, anti-rollback policy, version compatibility with config/protocol, and recovery after power loss. <span class="warn">Without rollback or safe boot, OTA can turn a remote device into an inaccessible brick.</span>[^dou-embedded-interview]

## Detailed explanation

OTA update is the delivery and installation of new firmware on a device over a network (Wi-Fi, cellular, Ethernet) without physical access. Key risks and their mitigations:

**Power loss during install.** If firmware is written to the same flash where the current version runs, power loss leads to bricking. Solution: dual-bank or A/B scheme with atomic install – the new image is written to a separate bank, and switching happens only after successful write and verification. If power loss occurs during write, the old image remains valid.

**Signature verification.** The image can be corrupted during transfer or forged. Solution: cryptographic hash (SHA-256) for integrity check and asymmetric signature (ECDSA, Ed25519) for authenticity. The bootloader verifies the signature before executing the new image.[^mcuboot-design]

**Anti-rollback policy.** An attacker may try to downgrade the device to an old version with known vulnerabilities. Solution: monotonic version counter in secure storage (eFuse, secure flash), and the bootloader refuses to run an image with a lower version number.

**Version compatibility.** New firmware may be incompatible with config, protocol, or hardware abstraction layer. Solution: version metadata in the image manifest, migration scripts for config, and staged rollout to detect issues on a small percentage of devices before mass deployment.

**Recovery after power loss.** Even with dual-bank, a mechanism is needed to determine which bank to boot. Solution: boot counter and watchdog timer. If the new image fails health check within N boot attempts, the bootloader automatically switches back to the previous valid image.[^mcuboot-design]

The update package typically includes: image binary, version metadata, target device identifier, dependencies (if any), changelog, and cryptographic signature. The deployment platform must support: device authentication, staged rollout (canary deployment), audit log, and fleet-wide rollback.

### Expected signals

- Understands that power loss during install is the primary risk, and dual-bank/A/B is the standard solution
- Mentions signature verification as mandatory for security
- Understands anti-rollback policy and its connection to security vulnerabilities
- Mentions staged rollout as a way to minimize version incompatibility risk
- Understands that a recovery mechanism (boot counter, watchdog) is needed even with dual-bank

### Red flags

- Believes OTA does not need a rollback mechanism
- Does not mention signature verification or considers it optional
- Confuses integrity check (hash) with authenticity check (signature)
- Cannot distinguish dual-bank from A/B schemes
- Believes power loss is not a problem for OTA

### Level-up follow-up

- How to implement anti-rollback policy, and why can it be controversial?
- How to ensure secure key storage on a device with limited hardware security module?
