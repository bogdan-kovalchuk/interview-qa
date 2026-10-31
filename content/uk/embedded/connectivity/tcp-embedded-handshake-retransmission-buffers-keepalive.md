---
id: emb-conn-0009
title: "Як працює TCP у контексті обмеженого embedded-пристрою: handshake, retransmission, buffers і keepalive?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: rfc-9293-tcp
    title: "RFC 9293: Transmission Control Protocol (TCP)"
    url: https://www.rfc-editor.org/rfc/rfc9293.html
  - source_id: lwip-opts-tcp
    title: "lwIP 2.1.0: TCP options (lwipopts.h)"
    url: https://www.nongnu.org/lwip/2_1_x/group__lwip__opts__tcp.html
  - source_id: rfc-6298-tcp-rto
    title: "RFC 6298: Computing TCP's Retransmission Timer"
    url: https://www.rfc-editor.org/rfc/rfc6298.html
  - source_id: linux-man-tcp
    title: "tcp(7) – Linux manual page"
    url: https://man7.org/linux/man-pages/man7/tcp.7.html
  - source_id: posix-send
    title: "POSIX.1-2024: send()"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/send.html
  - source_id: lwip-tcp-raw-api
    title: "lwIP 2.1.0: TCP raw API"
    url: https://www.nongnu.org/lwip/2_1_x/group__tcp__raw.html
---

## Short answer

TCP починається з **three-way handshake**, потім гарантує ordered byte stream через ACK, retransmission, windowing і congestion control. На embedded важливі RAM buffers, timeout/reconnect logic, partial writes/reads і backpressure від network stack. <span class="warn">Keepalive не замінює application-level heartbeat, якщо треба швидко виявляти завислий peer.</span>[^dou-embedded-interview]

## Detailed explanation

### Handshake і ціна одного з’єднання

З’єднання відкривається three-way handshake: SYN, SYN-ACK, ACK. Головна причина саме трьох кроків – не дати старим дублікатам SYN створити хибне з’єднання.[^rfc-9293-tcp] Під час handshake сторони обмінюються опцією MSS; якщо її немає, відправник мусить припустити 536 байтів для IPv4.[^rfc-9293-tcp] У lwIP `TCP_MSS` за замовчуванням теж 536[^lwip-opts-tcp], тоді як у звичайному Ethernet із MTU 1500 за мінімальних заголовків IPv4 і TCP (по 20 байтів) у сегмент вміщується 1460 байтів. Для пристрою, що передає багато даних, це майже потрійна різниця в кількості сегментів.

Кожне з’єднання – це control block у RAM, а на MCU control blocks зазвичай беруться з фіксованого пулу. Сторона, що закриває з’єднання першою, тримає його в стані TIME-WAIT протягом 2MSL[^rfc-9293-tcp], тож firmware, яка в циклі відкриває і закриває з’єднання на кшталт «HTTP-запит раз на секунду», може вичерпати пул швидше, ніж очікувалося. Довготривале з’єднання (MQTT, WebSocket) для таких пристроїв зазвичай дешевше.

### Retransmission: чому помилка приходить так пізно

Тайм-аут перепередачі (RTO) обчислюється динамічно за RFC 6298 з алгоритмом Карна.[^rfc-9293-tcp] До першого виміру RTT він дорівнює 1 s, а при повторних втратах експоненційно збільшується.[^rfc-6298-tcp-rto] RFC 9293 описує два пороги: після R1 (щонайменше 3 перепередачі) TCP лише повідомляє нижчі рівні про проблему, а після R2 (щонайменше 100 s) закриває з’єднання; для SYN R2 має покривати щонайменше 3 хвилини.[^rfc-9293-tcp]

Реалізації обирають власні значення. У Linux `tcp_retries2` за замовчуванням 15, що відповідає приблизно 13–30 хвилинам до розриву встановленого з’єднання; опція `TCP_USER_TIMEOUT` обмежує час, протягом якого передані дані можуть лишатися непідтвердженими.[^linux-man-tcp] У lwIP за замовчуванням `TCP_MAXRTX` 12 для даних і `TCP_SYNMAXRTX` 6 для SYN.[^lwip-opts-tcp] Практичний висновок: якщо Wi-Fi зник, `send()` ще довго буде «успішним», бо успіх означає лише, що дані лягли в буфер; POSIX прямо каже, що успішне завершення `send()` не гарантує доставки.[^posix-send] Firmware потребує власного тайм-ауту на рівні операції.

### Буфери, вікно і backpressure

Приймач оголошує вікно – скільки байтів він готовий прийняти. У lwIP `TCP_WND` за замовчуванням дорівнює `4 × TCP_MSS`, тобто 2144 байти, і документація радить не менше `2 × TCP_MSS`; буфер передавання `TCP_SND_BUF` – `2 × TCP_MSS`, тобто 1072 байти.[^lwip-opts-tcp] Вікно напряму обмежує пропускну здатність: не більше одного вікна за RTT. При вікні 2144 байти і RTT 100 ms це `2144 / 0,1 = 21 440 B/s`, приблизно 171 kbit/s, незалежно від швидкості каналу.

Якщо застосунок не встигає читати, вікно падає до нуля, і відправник лише періодично зондує його (zero-window probing обов’язковий); приймач має право тримати вікно закритим як завгодно довго.[^rfc-9293-tcp] Повільна задача на MCU таким чином гальмує відправника на іншому боці – це backpressure, а не помилка.

На стороні передавання raw API lwIP поводиться так: `tcp_write()` лише ставить дані в чергу і не відправляє їх одразу (для цього `tcp_output()`), а при перевищенні вільного місця в буфері або довжини черги сегментів повертає `ERR_MEM`. Правильне використання – писати не більше `tcp_sndbuf()` байтів і після `ERR_MEM` чекати, доки частину даних буде підтверджено.[^lwip-tcp-raw-api] У socket API те саме проявляється як блокування `send()` або, для неблокувального сокета, як помилка `EAGAIN`/`EWOULDBLOCK`; `send()` повертає кількість фактично надісланих байтів.[^posix-send] Тому надійна firmware завжди працює в циклі:

```c
#include <errno.h>
#include <stddef.h>
#include <sys/socket.h>
#include <sys/types.h>

/* Returns 0 when all len bytes were accepted by the stack, -1 on error. */
int send_all(int fd, const unsigned char *buf, size_t len)
{
    while (len > 0) {
        ssize_t n = send(fd, buf, len, 0);
        if (n < 0) {
            if (errno == EINTR)
                continue;
            return -1; /* EAGAIN on a non-blocking socket: wait in poll() first */
        }
        buf += (size_t)n;
        len -= (size_t)n;
    }
    return 0;
}
```

Симетрично на прийомі: межі сегментів не пов’язані з межами викликів застосунку[^rfc-9293-tcp], тож `recv()` може повернути половину повідомлення або півтора. Протокол поверх TCP мусить мати кадрування (довжина плюс дані), а парсер – накопичувати байти.

Окремо – алгоритм Nagle: поки є непідтверджені дані, TCP буферизує нові дрібні записи до підтвердження або до повного сегмента; реалізація зобов’язана дозволяти вимкнути його для окремого з’єднання.[^rfc-9293-tcp] Для коротких команд, де важлива затримка, його вимикають (`TCP_NODELAY` у Linux, `tcp_nagle_disable()` у lwIP).[^linux-man-tcp][^lwip-tcp-raw-api]

### Keepalive і чому його мало

TCP keepalive у RFC 9293 – необов’язкова можливість: якщо вона є, застосунок має вмикати її для кожного з’єднання окремо, за замовчуванням вона вимкнена, а інтервал простою перед зондуванням за замовчуванням не менший за дві години. Зонди надсилаються лише тоді, коли немає непідтверджених даних, і відсутність відповіді на один зонд не можна вважати мертвим з’єднанням, бо ACK без даних не доставляються надійно.[^rfc-9293-tcp] У Linux `tcp_keepalive_time` за замовчуванням 7200 s, і keepalive працює лише з `SO_KEEPALIVE`.[^linux-man-tcp]

Звідси чотири причини, чому keepalive не замінює прикладний heartbeat:

1. За замовчуванням він вимкнений, а якщо увімкнений – стартує через години.
2. Коли є непідтверджені дані, keepalive не працює зовсім; обрив визначає механізм перепередачі з його хвилинними порогами.
3. Відповідь на зонд доводить лише, що живий TCP-стек протилежного боку, а не що його застосунок обробляє повідомлення.
4. Таймери простою в NAT і проміжних вузлах можуть бути коротшими за інтервал keepalive.

Прикладний heartbeat, наприклад Keep Alive у MQTT (див. qid:emb-conn-0002), перевіряє саме те, що потрібно: протилежний застосунок відповідає вчасно. Вибір між TCP і UDP для різних типів трафіку розібрано в qid:emb-conn-0004.
