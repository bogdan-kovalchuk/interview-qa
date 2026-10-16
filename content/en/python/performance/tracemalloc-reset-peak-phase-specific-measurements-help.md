---
id: py-perf-0010
title: "How do `tracemalloc.reset_peak()` and phase-specific measurements help tell a temporary allocation spike apart from retained memory growth?"
track: python
section: performance
sources:
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
  - source_id: py314-library-tracemalloc-reset-peak
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html#tracemalloc.reset_peak
  - source_id: py314-library-tracemalloc-get-traced-memory
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html#tracemalloc.get_traced_memory
  - source_id: py314-library-tracemalloc-record-current-peak
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html#record-the-current-and-peak-size-of-all-traced-memory-blocks
  - source_id: py314-library-tracemalloc-snapshot-compare-to
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html#tracemalloc.Snapshot.compare_to
---

## Short answer

**`tracemalloc.reset_peak()` sets the peak to the current size without clearing the traces, so the peak can be measured separately for each phase.**[^py314-library-tracemalloc-reset-peak] Call `reset_peak()` at the start of a phase, then read `get_traced_memory()`, which returns `(current, peak)`.[^py314-library-tracemalloc-get-traced-memory] A peak well above current, and current back at its baseline, is a temporary spike. Current that keeps growing from phase to phase indicates retained growth: the objects have not been freed (or are waiting for garbage collection). To find the line that allocates, compare snapshots with `Snapshot.compare_to`.[^py314-library-tracemalloc-snapshot-compare-to]

## Detailed explanation

`tracemalloc` traces most memory blocks allocated by Python, starting from the `tracemalloc.start()` call.[^py314-library-tracemalloc] `get_traced_memory()` returns a pair `(current, peak)`: the current size of the traced blocks and their maximum.[^py314-library-tracemalloc-get-traced-memory] Without a reset, the peak is a maximum since `start()`: in the documentation example, the second peak stays at the large value from the earlier phase until the peak is reset.[^py314-library-tracemalloc-record-current-peak] `reset_peak()` (added in 3.9) sets the peak to the current size and does not modify any traces, and snapshots taken before and after the call can be compared.[^py314-library-tracemalloc-reset-peak]

The following example measures two phases separately. The output is the same on CPython 3.13 and 3.14:

```python
import tracemalloc

MiB = 1024 * 1024

tracemalloc.start()
baseline, _ = tracemalloc.get_traced_memory()

# Phase 1: temporary spike, allocated and then freed
data = [0] * 1_000_000
total = sum(data)
del data
current, peak = tracemalloc.get_traced_memory()
print(f"spike: current={(current - baseline) / MiB:.1f} MiB, peak={(peak - baseline) / MiB:.1f} MiB")
# spike: current=0.0 MiB, peak=7.6 MiB

tracemalloc.reset_peak()  # measure phase 2's peak from the current size

# Phase 2: retained growth, each step keeps a reference
retained = []
for step in range(1, 4):
    retained.append(bytearray(MiB))
    current, peak = tracemalloc.get_traced_memory()
    print(f"step {step}: current={(current - baseline) / MiB:.1f} MiB, peak={(peak - baseline) / MiB:.1f} MiB")
# step 1: current=1.0 MiB, peak=1.0 MiB
# step 2: current=2.0 MiB, peak=2.0 MiB
# step 3: current=3.0 MiB, peak=3.0 MiB

tracemalloc.stop()
```

In the first phase the peak is 7.6 MiB, and after `del data` the current returns to 0.0 MiB: a temporary spike. In the second phase the current grows by 1 MiB per step, because the `retained` list keeps a reference to every buffer, and after `reset_peak()` the peak equals the current: retained growth. Without `reset_peak()`, every line of the second phase would show the 7.6 MiB peak and hide that behaviour.[^py314-library-tracemalloc-record-current-peak]

One measurement does not prove retained growth, because it shows the state at a single point. The pattern appears when the same phase is repeated: if the current keeps growing after each iteration, the blocks have not been freed (or are waiting for garbage collection in reference cycles); if the current returns to its baseline after the phase, the memory was freed. To find the line that allocates, take a snapshot before and after the phase and call `Snapshot.compare_to()`, which computes the differences between the two snapshots.[^py314-library-tracemalloc-snapshot-compare-to]

Limits of the method: `tracemalloc` does not show all process memory. The documentation speaks of "most memory blocks allocated by Python",[^py314-library-tracemalloc] so memory that C extensions allocate outside Python's allocator may be missing from these numbers, and `get_traced_memory()` is not the process RSS. Calling `reset_peak()` while tracing is off does nothing.[^py314-library-tracemalloc-reset-peak] Without `start()`, `get_traced_memory()` returns `(0, 0)`:

```python
import tracemalloc

print(tracemalloc.get_traced_memory())  # (0, 0) on CPython 3.13 and 3.14 while tracing is off
```

**Common mistakes:**
- reading the peak without `reset_peak()` and attributing it to the last phase;
- taking one measurement and calling it retained growth, when the phase must be repeated;
- treating traced memory as the process RSS;
- calling `reset_peak()` without `tracemalloc.start()` and expecting an effect.
