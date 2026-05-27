# Challenge 10 — Format String Vulnerability

## Vulnerability
`printf(input)` passes user input directly as the format string.
The attacker controls format specifiers like `%p`, `%x`, `%s`, `%n`.

## Exploit
1. Used `%p` repeated 40 times to dump raw stack values safely
2. Scanned output for flag bytes (`CTF{` = `0x43544600`)
3. Found flag across stack positions 14-18
4. Decoded each 8-byte chunk with little-endian byte order

## Key Concepts
- `%p` prints raw stack values — no pointer dereference, no crash
- `%s` dereferences the stack value as a pointer — crashes on invalid addresses
- `%n` writes to memory — turns read primitive into arbitrary write
- Little-endian: bytes stored least-significant-byte first, must reverse to decode

## Flag
CTF{format_string_reads_and_writes_memory}
