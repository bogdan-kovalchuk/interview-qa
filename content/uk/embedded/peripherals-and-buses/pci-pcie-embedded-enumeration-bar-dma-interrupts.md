---
id: emb-periph-0021
title: "Коли PCI/PCIe може бути embedded-темою і які базові поняття треба знати: enumeration, BAR, DMA, interrupts?"
track: embedded
section: peripherals-and-buses
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
  - source_id: linux-kernel-pci
    title: "The Linux Kernel documentation: PCI Subsystem"
    url: https://docs.kernel.org/driver-api/pci/index.html
---

## Short answer

PCI/PCIe стає embedded-темою на SoC, industrial computers, FPGA cards, high-speed peripherals або Linux-based controllers. Потрібно знати **enumeration**, config space, `BAR` regions для MMIO, bus mastering DMA і interrupts MSI/MSI-X або legacy INTx. <span class="warn">Driver має правильно мапити BAR, керувати DMA buffers і враховувати IOMMU/cache coherency.</span>[^dou-embedded-interview]

## Detailed explanation

### Контекст застосування PCIe у Embedded-системах
Традиційно шина PCI Express (PCIe) асоціюється із серверами та персональними комп’ютерами. Проте у сучасній розробці вбудованих систем (Embedded Systems) PCIe є ключовим інтерфейсом у таких сферах [^linux-kernel-pci][^zephyr-peripherals]:
- **Високопродуктивні SoC (System-on-Chip)**: платформи NXP i.MX8, TI Sitara AM6x, NVIDIA Jetson, Raspberry Pi Compute Module 4/5, STM32MP2, де PCIe з’єднує процесор із швидкісними периферійними контролерами.
- **Модулі розширення та NVMe**: підключення високошвидкісних твердотільних накопичувачів NVMe SSD, модулів стільникового зв’язку 5G, Wi-Fi 6/7, Ethernet-контролерів (10GbE) або нейроприскорювачів (NPU / TPU).
- **Зв’язок CPU із FPGA**: високошвидкісний обмін даними (гігабайти на секунду) між процесорною системою під керуванням Embedded Linux та ПЛІС/FPGA, що реалізує апаратну обробку сигналів радіолокації, відеопотоків або збір даних від сенсорів.

### Базові фундаментальні концепції PCI Express
На відміну від паралельної шини Classic PCI, шина PCIe є пакетною мережею типу «точка-точка» (Point-to-Point serial links), де передача здійснюється диференційними лініями (Lanes: x1, x2, x4, x8, x16) через структуру комутаторів (Root Complex, PCIe Switches та Endpoints).

1. **Конфігураційний простір (PCI Configuration Space)**:
   Кожен PCIe-пристрій містить апаратний блок конфігураційних регістрів (розміром 256 байтів для сумісності з PCI та до 4 КБ для розширеного PCIe). Він включає унікальні ідентифікатори виробника та пристрою (`Vendor ID`, `Device ID`), клас пристрою (`Class Code`), регістри керування команд (`Command Register`) та регістри базових адрес (`BAR0`–`BAR5`).

2. **Процес перелічення шини (Bus Enumeration)**:
   Під час завантаження ядра (BIOS/UEFI або Linux Kernel PCI core) хост-процесор виконує рекурсивний обхід дерева шин (DFS – Depth-First Search) [^linux-kernel-pci]:
   - Скануються координати `Bus:Device.Function` (BDF).
   - Для кожного виявленого пристрою визначаються його ресурси та вимоги до пам’яті.
   - Дерево шин отримує унікальні номери, а мости та кінцеві пристрої конфігуруються для коректної маршрутизації транзакцій TLP (Transaction Layer Packet).

3. **Регістри базових адрес (Base Address Registers, BAR)**:
   BAR визначає, скільки пам’яті (або простору I/O) потрібно пристрою для відображення його внутрішніх регістрів або буферів в адресний простір CPU (Memory-Mapped I/O, MMIO) [^linux-kernel-pci]:
   - **Алгоритм зондування розміру BAR**: хост записує в регістр BAR значення `0xFFFFFFFF`, а потім зчитує його назад. Недоступні для запису молодші нульові біти вказують на потрібний розмір блоку пам’яті (наприклад, якщо зчитано `0xFFFE0000`, пристрою потрібен блок розміром 128 КБ).
   - **Призначення адреси**: операційна система виділяє вільний діапазон у системному адресному просторі MMIO і записує базову адресу у BAR.
   - **Мапування драйвером**: драйвер пристрою викликає функцію ядра (наприклад, `pci_iomap()` або `ioremap()`), отримуючи віртуальний покажчик для прямого доступу до регістрів апаратного блоку.

### Прямий доступ до пам’яті (Bus Mastering DMA)
Для досягнення високої пропускної здатності PCIe-пристрій виступає ініціатором транзакцій на шині (Bus Master):
- Кінцевий пристрій (Endpoint, наприклад FPGA) генерує транзакції читання/запису пам’яті (Memory Read / Memory Write TLP) безпосередньо в системну оперативну пам’ять процесора.
- Для керування потоком зазвичай використовується схема кільцевих буферів дескрипторів (Ring Buffer of DMA Descriptors), де дескриптор містить фізичну адресу пам’яті хоста, довжину блоку та прапорці завершення.
- **Когерентність та IOMMU**: на прикладних процесорах доступ DMA координується через системний IOMMU (Input-Output Memory Management Unit) для трансляції адрес і захисту пам’яті, а також кеш-когерентні інтерфейси шини (наприклад, CCI/CMN в ARM), що усуває необхідність ручного скидання L1/L2 кешу при наявності апаратного snoop-контролера [^linux-kernel-pci].

### Механізми переривань (Interrupts: INTx vs MSI/MSI-X)
1. **Legacy INTx**: емуляція віртуальних ліній переривань (INTA#, INTB#, INTC#, INTD#) через спеціальні повідомлення `Assert_INTx` / `Deassert_INTx`. Мають високу латентність і вимагають спільного використання лінії (shared interrupts) між різними пристроями.
2. **MSI (Message Signaled Interrupts)**:
   Переривання формується як звичайна операція запису (Memory Write TLP) 32-бітного спеціального значення за фіксованою адресою в контролері переривань процесора (наприклад, ARM GIC ITS або x86 APIC) [^linux-kernel-pci]. Підтримує до 32 векторів.
3. **MSI-X**:
   Розширена версія, що підтримує до 2048 незалежних векторів переривань із власною таблицею адресації в пам’яті пристрою. Дозволяє прив’язати кожну чергу DMA або ядро CPU до власного ізольованого вектора переривання, мінімізуючи джиттер та блокування у багатоядерних системах.
