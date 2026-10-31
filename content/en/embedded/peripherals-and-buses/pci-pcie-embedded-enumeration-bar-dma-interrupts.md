---
id: emb-periph-0021
title: "When can PCI/PCIe be an embedded topic and what basic concepts are needed: enumeration, BAR, DMA, interrupts?"
track: embedded
section: peripherals-and-buses
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
  - source_id: linux-kernel-pci
    title: "The Linux Kernel documentation: PCI Subsystem"
    url: https://docs.kernel.org/driver-api/pci/index.html
  - source_id: linux-pci-driver-guide
    title: "The Linux Kernel: How To Write Linux PCI Drivers"
    url: https://docs.kernel.org/PCI/pci.html
  - source_id: linux-pci-msi-howto
    title: "The Linux Kernel: The MSI Driver Guide HOWTO"
    url: https://docs.kernel.org/PCI/msi-howto.html
  - source_id: linux-pci-regs
    title: "Linux source: include/uapi/linux/pci_regs.h"
    url: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/include/uapi/linux/pci_regs.h
---

## Short answer

PCI/PCIe becomes an embedded topic on SoCs, industrial computers, FPGA cards, high-speed peripherals, or Linux-based controllers. You need to know **enumeration**, config space, `BAR` regions for MMIO, bus mastering DMA, and interrupts: MSI/MSI-X or legacy INTx. <span class="warn">The driver must map BARs properly, manage DMA buffers, and handle IOMMU/cache coherency.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
