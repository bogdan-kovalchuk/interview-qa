---
id: emb-boot-0007
title: "Що таке OTA update і які ризики треба закрити: power loss, signature verification, rollback і version compatibility?"
track: embedded
section: safety-security-and-reliability
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: mcuboot-design
    title: "MCUboot design documentation"
    url: https://docs.mcuboot.com/design.html
---

## Short answer

**OTA** - оновлення firmware через мережу без фізичного доступу до пристрою. Потрібні atomic install, image integrity, signature verification, anti-rollback policy, version compatibility з config/protocol і recovery після power loss. <span class="warn">Без rollback або safe boot OTA може перетворити remote device на недоступний brick.</span>[^dou-embedded-interview]

## Detailed explanation

OTA update – це доставка та встановлення нового firmware на пристрій через мережу (Wi-Fi, cellular, Ethernet) без фізичного доступу. Основні ризики та їх mitigation:

**Power loss під час install.** Якщо firmware записується в той самий flash, де працює поточна версія, втрата живлення призведе до bricking. Рішення: dual-bank або A/B схема з atomic install – новий image записується в окремий банк, і лише після успішного запису та verification відбувається переключення. Якщо power loss станеться під час запису, старий image залишається valid.

**Signature verification.** Image може бути пошкоджений під час передачі або підроблений. Рішення: cryptographic hash (SHA-256) для integrity check та asymmetric signature (ECDSA, Ed25519) для authenticity. Bootloader перевіряє signature перед виконанням нового image.[^mcuboot-design]

**Anti-rollback policy.** Зловмисник може спробувати відкотити пристрій на стару версію з відомими вразливостями. Рішення: monotonic version counter у secure storage (eFuse, secure flash), і bootloader відмовляється запускати image з меншим version number.

**Version compatibility.** Новий firmware може бути несумісний з config, protocol або hardware abstraction layer. Рішення: version metadata у image manifest, migration scripts для config, та staged rollout для виявлення проблем на малий відсоток пристроїв перед масовим deployment.

**Recovery після power loss.** Навіть з dual-bank, потрібен механізм визначення, який банк boot-ити. Рішення: boot counter та watchdog timer. Якщо новий image не проходить health check протягом N boot attempts, bootloader автоматично перемикається на попередній valid image.[^mcuboot-design]

Update package зазвичай включає: image binary, version metadata, target device identifier, dependencies (якщо є), changelog, та cryptographic signature. Deployment платформа повинна підтримувати: device authentication, staged rollout (canary deployment), audit log, та fleet-wide rollback.

### Очікувані сигнали

- Розуміє, що power loss під час install – це основний ризик, і dual-bank/A/B є стандартним рішенням
- Згадує signature verification як обов’язкову для security
- Розуміє anti-rollback policy та її зв’язок з security vulnerabilities
- Згадує staged rollout як спосіб мінімізації ризику version incompatibility
- Розуміє, що recovery механізм (boot counter, watchdog) потрібен навіть з dual-bank

### Червоні прапорці

- Вважає, що OTA не потребує rollback механізму
- Не згадує signature verification або вважає її опціональною
- Плутає integrity check (hash) з authenticity check (signature)
- Не розуміє різниці між dual-bank та A/B схемами
- Вважає, що power loss не є проблемою для OTA

### Питання на підвищення рівня

- Як реалізувати anti-rollback policy, і чому вона може бути controversial?
- Як забезпечити secure key storage на пристрої з обмеженим hardware security module?
