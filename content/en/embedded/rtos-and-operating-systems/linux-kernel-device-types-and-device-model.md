---
id: emb-fund-0022
title: "Which device types exist in the Linux kernel, and how are they represented by the device model?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: ldd3-ch01-device-classes
    title: "Linux Device Drivers, 3rd Edition, Chapter 1: An Introduction to Device Drivers"
    url: https://static.lwn.net/images/pdf/LDD3/ch01.pdf
  - source_id: linux-allocated-devices
    title: "The Linux Kernel: Linux allocated devices"
    url: https://docs.kernel.org/admin-guide/devices.html
  - source_id: linux-driver-infrastructure
    title: "The Linux Kernel: Device drivers infrastructure"
    url: https://docs.kernel.org/driver-api/infrastructure.html
  - source_id: linux-driver-binding
    title: "The Linux Kernel: Driver Binding"
    url: https://docs.kernel.org/driver-api/driver-model/binding.html
  - source_id: linux-sysfs
    title: "The Linux Kernel: sysfs - The filesystem for exporting kernel objects"
    url: https://docs.kernel.org/filesystems/sysfs.html
  - source_id: linux-platform-devices
    title: "The Linux Kernel: Platform Devices and Drivers"
    url: https://docs.kernel.org/driver-api/driver-model/platform.html
  - source_id: linux-devicetree-usage-model
    title: "The Linux Kernel: Linux and the Devicetree"
    url: https://docs.kernel.org/devicetree/usage-model.html
---

## Short answer

Linux has **character**, **block**, **network**, platform, and bus-specific devices, among others. The device model represents them through `struct device`, bus, driver, class, and sysfs nodes. For embedded, platform devices, devicetree/ACPI hardware description, and driver binding to compatible/resource data are important.[^dou-embedded-interview]

## Detailed explanation

TODO
