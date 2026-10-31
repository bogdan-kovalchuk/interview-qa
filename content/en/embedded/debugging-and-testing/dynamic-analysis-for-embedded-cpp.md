---
id: emb-testemb-0008
title: "Which dynamic-analysis approaches are possible for embedded C/C++: host sanitizers, Valgrind, tracing, and fault injection?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
  - source_id: clang-asan
    title: "Clang documentation: AddressSanitizer"
    url: https://clang.llvm.org/docs/AddressSanitizer.html
  - source_id: clang-ubsan
    title: "Clang documentation: UndefinedBehaviorSanitizer"
    url: https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html
  - source_id: clang-tsan
    title: "Clang documentation: ThreadSanitizer"
    url: https://clang.llvm.org/docs/ThreadSanitizer.html
  - source_id: zephyr-native-sim
    title: "Zephyr Project documentation: Native simulator - native_sim"
    url: https://docs.zephyrproject.org/latest/boards/native/native_sim/doc/index.html
  - source_id: valgrind-memcheck
    title: "Valgrind User Manual: Memcheck, a memory error detector"
    url: https://valgrind.org/docs/manual/mc-manual.html
  - source_id: gcc-instrumentation-options
    title: "GCC manual: Program Instrumentation Options"
    url: https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html
  - source_id: zephyr-thread-analyzer
    title: "Zephyr Project documentation: Thread analyzer"
    url: https://docs.zephyrproject.org/latest/services/debugging/thread-analyzer.html
  - source_id: gdb-set-watchpoints
    title: "Debugging with GDB: Setting Watchpoints"
    url: https://sourceware.org/gdb/current/onlinedocs/gdb.html/Set-Watchpoints.html
  - source_id: zephyr-coverage
    title: "Zephyr Project documentation: Generating coverage reports"
    url: https://docs.zephyrproject.org/latest/develop/test/coverage.html
  - source_id: zephyr-kconfig-init-stacks
    title: "Zephyr Project documentation: Kconfig CONFIG_INIT_STACKS"
    url: https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INIT_STACKS
---

## Short answer

On the host, you can run **ASan/UBSan/TSan** for logic without hardware dependencies, and `Valgrind` is useful for Linux-target or host scenarios. On target, trace, coverage, watchpoints, stack watermarking, fault injection, bus/error simulation, and HIL tests are more common. <span class="warn">A sanitizer on a PC does not prove correctness of ISRs, DMA cache coherency, or real timing.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
