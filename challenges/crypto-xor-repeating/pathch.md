# Fix — Repeating-Key XOR

## Why It's Broken
- Short repeating key means each key byte encrypts multiple plaintext bytes
- XOR with repeating key preserves statistical structure of plaintext
- Known plaintext (CTF{ prefix) directly reveals key bytes

## The Fix
Never use XOR with a short repeating key for encryption. Use:
- AES-CTR or AES-GCM (stream cipher mode with proper key schedule)
- Each key must be: long, random, never reused
- Key reuse is catastrophic — two ciphertexts XORed together cancels the key

## Rule
Stream ciphers must never reuse a key. One key = one message, ever.
