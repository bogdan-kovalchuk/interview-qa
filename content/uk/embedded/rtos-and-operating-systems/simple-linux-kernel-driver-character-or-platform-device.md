---
id: emb-fund-0023
title: "Як підходити до написання простого Linux kernel driver для character device або platform device?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: linux-platform-devices
    title: "The Linux Kernel: Platform Devices and Drivers"
    url: https://docs.kernel.org/driver-api/driver-model/platform.html
  - source_id: linux-driver-model-driver
    title: "The Linux Kernel: Device Drivers (driver model)"
    url: https://docs.kernel.org/driver-api/driver-model/driver.html
  - source_id: linux-devres
    title: "The Linux Kernel: Devres – керовані ресурси пристрою"
    url: https://docs.kernel.org/driver-api/driver-model/devres.html
  - source_id: linux-driver-infrastructure
    title: "The Linux Kernel: Device drivers infrastructure"
    url: https://docs.kernel.org/driver-api/infrastructure.html
  - source_id: linux-kernel-api-char-devices
    title: "The Linux Kernel API: Char devices"
    url: https://docs.kernel.org/core-api/kernel-api.html
  - source_id: linux-misc-devices
    title: "The Linux Kernel: Miscellaneous Devices"
    url: https://docs.kernel.org/driver-api/misc_devices.html
  - source_id: linux-kernel-hacking-guide
    title: "The Linux Kernel: Unreliable Guide To Hacking The Linux Kernel"
    url: https://docs.kernel.org/kernel-hacking/hacking.html
  - source_id: linux-fs-api-summary
    title: "Linux Filesystems API summary (simple_read_from_buffer)"
    url: https://docs.kernel.org/filesystems/api-summary.html
---

## Short answer

Для character device визначають file operations: `open`, `read`, `write`, `ioctl`, плюс registration і lifetime cleanup. Для platform driver реалізують `probe`/`remove`, беруть resources з devicetree, маплять MMIO, реєструють IRQ і exposed interface. <span class="warn">У kernel driver не можна мислити як у user space: інші allocation rules, locking, sleep context і error handling.</span>[^dou-embedded-interview]

## Detailed explanation

Простий драйвер для embedded Linux майже завжди складається з двох незалежних половин: прив’язки до заліза (platform driver, який отримує ресурси від ядра) і інтерфейсу для user space (char device або вже наявна підсистема). Інтерв’юер зазвичай перевіряє, чи кандидат бачить цю межу, чи розуміє життєвий цикл `probe()`/`remove()` і чи знає обмеження kernel context.

### Перше рішення: чи потрібен власний драйвер

Перш ніж писати код, варто перевірити, чи не покриває задачу наявна підсистема (GPIO, IIO, hwmon, input, serial) або user-space інтерфейс на кшталт UIO чи `spidev`. Власний char device з довільним `ioctl` – найгнучкіший, але й найдорожчий у підтримці варіант; порівняння з user-space драйверами – у qid:emb-linemb-0001.

### Platform driver: прив’язка до заліза

Периферію SoC ядро бачить як `platform_device`: ім’я плюс список ресурсів (адреси регістрів, IRQ). Драйвер не шукає залізо сам: виявлення відбувається поза ним, а драйвер надає `probe()` і `remove()`. У сучасних ядрах `remove()` у `struct platform_driver` повертає `void`[^linux-platform-devices]; у старіших версіях (наприклад, 6.6) він повертав `int`. На платах із devicetree пристрій створюється з вузла дерева, а драйвер оголошує сумісні рядки в `of_match_table`.[^linux-driver-infrastructure]

`probe()` викликається в task context і має перевірити, що пристрій справді присутній і підтримується, виділити й ініціалізувати структури даних та ініціалізувати залізо. Якщо `probe()` повертає від’ємний errno, драйвер не прив’язується і мусить звільнити все, що встиг виділити. Окремий випадок – `-EPROBE_DEFER`: його повертають, коли ще не готовий потрібний ресурс (clock, regulator, GPIO іншого драйвера), і driver core повторить `probe()` пізніше. Повертати його треба якомога раніше, до створення дочірніх пристроїв.[^linux-driver-model-driver]

Ресурси беруть через helper-и: `devm_platform_ioremap_resource()` повертає вже відображену MMIO-область або `ERR_PTR()`, а `platform_get_irq()` – номер IRQ або від’ємну помилку, яку обов’язково треба перевірити до `request_irq()`.[^linux-driver-infrastructure] Префікс `devm_` означає devres: ресурс прив’язаний до `struct device` і звільняється автоматично при відв’язуванні драйвера або при невдалому `probe()`. Механізм з’явився саме тому, що шляхи помилок у `probe()` і `remove()` рідко тестуються й часто протікають; у списку керованих API є, зокрема, `devm_kzalloc()` і `devm_request_irq()`.[^linux-devres]

### Інтерфейс для user space: char device

Класичний шлях – `alloc_chrdev_region()` для динамічного major, потім `cdev_init()` і `cdev_add()`. Важливо, що `cdev_add()` робить пристрій «живим» одразу, тож до цього виклику все має бути ініціалізовано. Якщо `struct cdev` і `struct device` лежать в одній структурі, `cdev_device_add()` додає обидва й тримає посилання на батьківський пристрій, доки є посилання на cdev.[^linux-kernel-api-char-devices]

Для простих випадків зручніший misc device: `misc_register()` з `MISC_DYNAMIC_MINOR` сам виділяє minor, а під час `open()` встановлює `file->private_data` на зареєстровану `struct miscdevice`. Структура не може бути знищена, доки її не скасовано через `misc_deregister()`.[^linux-misc-devices]

Каркас, що поєднує обидві половини (регістр `DEMO_DATA` і рядок `compatible` умовні):

```c
#include <linux/module.h>
#include <linux/platform_device.h>
#include <linux/miscdevice.h>
#include <linux/fs.h>
#include <linux/io.h>
#include <linux/uaccess.h>
#include <linux/of.h>

#define DEMO_DATA 0x00   /* hypothetical data register offset */

struct demo {
	void __iomem *regs;
	struct miscdevice misc;
};

static ssize_t demo_read(struct file *f, char __user *buf,
			 size_t len, loff_t *off)
{
	/* misc core set private_data to &d->misc in open() */
	struct demo *d = container_of(f->private_data, struct demo, misc);
	u32 val = readl(d->regs + DEMO_DATA);

	/* advances *off; the next read returns 0 (EOF), so cat terminates */
	return simple_read_from_buffer(buf, len, off, &val, sizeof(val));
}

static const struct file_operations demo_fops = {
	.owner = THIS_MODULE,
	.read  = demo_read,
};

static int demo_probe(struct platform_device *pdev)
{
	struct demo *d = devm_kzalloc(&pdev->dev, sizeof(*d), GFP_KERNEL);

	if (!d)
		return -ENOMEM;
	d->regs = devm_platform_ioremap_resource(pdev, 0);
	if (IS_ERR(d->regs))
		return PTR_ERR(d->regs);

	d->misc.minor  = MISC_DYNAMIC_MINOR;
	d->misc.name   = "demo";
	d->misc.fops   = &demo_fops;
	d->misc.parent = &pdev->dev;
	platform_set_drvdata(pdev, d);
	return misc_register(&d->misc);   /* last step: node is live now */
}

static void demo_remove(struct platform_device *pdev)
{
	struct demo *d = platform_get_drvdata(pdev);

	misc_deregister(&d->misc);
}

static const struct of_device_id demo_of_match[] = {
	{ .compatible = "acme,demo" },
	{ }
};
MODULE_DEVICE_TABLE(of, demo_of_match);

static struct platform_driver demo_driver = {
	.probe  = demo_probe,
	.remove = demo_remove,
	.driver = {
		.name = "demo",
		.of_match_table = demo_of_match,
	},
};
module_platform_driver(demo_driver);
MODULE_LICENSE("GPL");
```

`read()` мусить просувати `*off`: `simple_read_from_buffer()` копіює дані в user space і збільшує позицію на кількість прочитаних байтів, тому після одного знімка регістра наступний виклик повертає 0, і `cat` завершується. Драйвер, який на кожен `read()` повертає ті самі 4 байти й не рухає `*off`, ніколи не віддає EOF.[^linux-fs-api-summary]

Каркас свідомо мінімальний. У реальному драйвері ще треба подумати про конкурентний доступ до регістрів з кількох відкритих файлів (mutex), про `poll()` для подій від IRQ і про те, що user space може тримати файл відкритим після unbind: пам’ять, звільнена через devres, не повинна бути доступна з `read()` після `remove()`.

### Правила kernel context

- **Сон дозволено лише в process context.** Системний виклик (`read`, `write`, `ioctl`) виконується в user context, де можна спати; обробник апаратного переривання – ні. `GFP_KERNEL` може спати, тому в IRQ-контексті потрібен `GFP_ATOMIC` із продуманою обробкою нестачі пам’яті.[^linux-kernel-hacking-guide]
- **Указівник з user space не можна розіменовувати.** Дані копіюють через `copy_to_user()`/`copy_from_user()` (вони повертають кількість нескопійованих байтів, 0 – успіх) або `get_user()`/`put_user()` (повертають 0 чи `-EFAULT`). Ці функції можуть спати.[^linux-kernel-hacking-guide]
- **Немає захисту пам’яті.** Пошкодження пам’яті в ядрі валить усю машину, а не один процес.[^linux-kernel-hacking-guide]
- **Малий стек і без FPU.** Стек ядра – приблизно 3–6 КБ на більшості 32-бітних архітектур і близько 14 КБ на 64-бітних, часто спільний з перериваннями; великі локальні масиви й глибока рекурсія заборонені. FPU-контекст не зберігається, тож замість floating point використовують fixed point.[^linux-kernel-hacking-guide]

### Типові помилки, які шукає інтерв’юер

- Реєстрація char device або IRQ до того, як ініціалізовано стан, який використовують `read()` чи обробник.
- Пропущена перевірка `platform_get_irq()` на від’ємне значення або `IS_ERR()` для `ioremap`.
- Ручне звільнення ресурсів, які вже керуються devres (подвійне звільнення), або навпаки – суміш devm і ручних викликів у неправильному порядку.
- Блокувальний виклик (`mutex_lock`, `GFP_KERNEL`, `copy_to_user`) під spinlock або в обробнику переривання.
- Hardcoded адреси регістрів чи номери IRQ у коді замість ресурсів з devicetree.
