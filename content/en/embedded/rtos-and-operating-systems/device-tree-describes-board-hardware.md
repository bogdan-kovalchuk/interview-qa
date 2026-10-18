---
id: emb-boot-0001
title: "What is a device tree?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: mcuboot-design
    title: "MCUboot design documentation"
    url: https://docs.mcuboot.com/design.html
  - source_id: devicetree-spec
    title: "Devicetree Specification v0.4"
    url: https://github.com/devicetree-org/devicetree-specification/releases/tag/v0.4
---

## Short answer

**Device Tree** is a data structure that describes board hardware (CPU, memory, peripherals, interrupts, buses) in a kernel-code-independent form.[^dou-embedded-interview] It allows a single Linux kernel image to support different boards.

Files: `.dts` (Device Tree Source, text) is compiled by `dtc` into `.dtb` (Device Tree Blob, binary). The bootloader (U-Boot) passes the DTB address to the kernel at boot.

Example node: describes UART1 – base register address, interrupt number, clocking; the kernel driver reads these parameters through the DT API.

## Detailed explanation

A Device Tree is a hierarchical data structure that describes hardware as nodes and properties. Each node represents a device or a group of devices; properties hold parameters (register addresses, interrupt numbers, clock rates, `compatible` strings). The root node contains system-wide information (memory size, machine type); child nodes describe peripherals (UART, SPI, I2C, GPIO controllers, etc.).

A `.dts` file (human-readable text) is compiled by the `dtc` (Device Tree Compiler) utility into a binary `.dtb`. The bootloader (e.g. U-Boot) loads the `.dtb` into memory and passes its address to the kernel through a CPU register (r2 on 32-bit ARM, or via ATAGS/EFI on other architectures).

During initialization the kernel parses the tree: it reads root node properties (`#address-cells`, `#size-cells`, `memory`) to determine memory size and machine type, then walks the device nodes. For each node the kernel matches the `compatible` property against drivers registered in the subsystem (platform bus, I2C bus, SPI bus, etc.) and binds the matching driver. The driver then reads configuration data from the node: `reg` (register address and size), `interrupts` (number and type), `clock-frequency`, `status` ("okay" / "disabled"), etc.[^devicetree-spec]

This approach decouples the hardware description from kernel code: a single kernel image can run on different boards; only the `.dtb` changes. It eliminated the need for board-specific `machine_desc` structures and separate kernel builds per board.
