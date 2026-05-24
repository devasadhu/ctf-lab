# Patch — XOR Cipher

## Vulnerable Approach
Using a single-byte key (256 possible values) makes brute force trivial.

## Secure Approach
1. Use a key as long as the message (one-time pad) — provably unbreakable
2. Or use a modern cipher like AES with a 128/256-bit key
3. Never reuse keys
4. Never use short, predictable keys

## Why Short Keys Fail
A brute force attack tries every possible key. With 256 possibilities,
a computer can try all of them instantly. AES-128 has 2^128 possible keys —
physically impossible to brute force.
