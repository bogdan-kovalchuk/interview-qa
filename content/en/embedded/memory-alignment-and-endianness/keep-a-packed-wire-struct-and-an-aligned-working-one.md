---
id: emb-align-0010
title: "What is the recommended pattern for working with a packed wire format?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-type-attributes
    title: "Common Type Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Type-Attributes.html
  - source_id: learncpp-struct-miscellany
    title: "Struct miscellany"
    url: https://www.learncpp.com/cpp-tutorial/struct-miscellany/
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
---

## Short answer

**Keep the external byte representation separate from the regular aligned type used by the program.**

```c
struct __attribute__((packed)) WireReading {
    uint8_t timestamp_le[4];
    uint8_t value_le[2];
    uint8_t id;
};

struct Reading {
    uint32_t timestamp;
    uint16_t value;
    uint8_t id;
};
```

Decode each byte field into the aligned object, explicitly applying the format's byte order. Then use the aligned object in the rest of the program.

Rule: a packed type describes storage layout; it does not by itself define serialization, byte order, or safe native access.[^embeddedinterviewlab]

## Detailed explanation

The two representations have different jobs:

- `WireReading` matches a seven-byte external record. Its multibyte values are byte arrays, so reading the record never creates a misaligned `uint16_t` or `uint32_t` lvalue.
- `Reading` holds native integer objects with the alignment and byte order expected by the target. Normal code should work with this type.

For a little-endian wire format, decoding can be explicit:

```c
static uint16_t load_le16(const uint8_t p[2]) {
    return (uint16_t)p[0] | ((uint16_t)p[1] << 8);
}

static uint32_t load_le32(const uint8_t p[4]) {
    return (uint32_t)p[0]
         | ((uint32_t)p[1] << 8)
         | ((uint32_t)p[2] << 16)
         | ((uint32_t)p[3] << 24);
}

static struct Reading decode(const struct WireReading *wire) {
    return (struct Reading) {
        .timestamp = load_le32(wire->timestamp_le),
        .value = load_le16(wire->value_le),
        .id = wire->id,
    };
}
```

This boundary conversion makes alignment and endianness visible and testable. A packed structure that instead contains native multibyte members can place those members at addresses unsuitable for ordinary typed access; GCC also warns that taking the address of such a field can produce an invalid pointer.[^gcc-type-attributes] Packing removes selected padding, but it does not make a compiler's complete object representation a portable protocol.

For a fixed format, verify its size and offsets at compile time, test known byte vectors, and perform the reverse conversion when encoding. Struct-padding tutorials help explain why the aligned working type may be larger than the wire record,[^learncpp-struct-miscellany] while the aCode roadmap is useful for placing this systems topic in a broader C and C++ learning plan.[^acode-cpp-next]
