# Challenge 9 — Repeating-Key XOR

## Vulnerability
Flag encrypted with multi-byte repeating key using XOR. Single-byte brute
force is impossible (2^64 keyspace for 8-byte key), but the repeating
structure leaks information.

## Attack Steps
1. **Index of Coincidence** — test key lengths 1-20, correct length produces
   groups with English-like byte distribution (high IC)
2. **Crib attack** — XOR known plaintext (CTF{) against ciphertext to recover
   first 4 key bytes: myse
3. **Frequency analysis** — crack remaining key bytes by finding which single
   byte produces most printable ASCII per group
4. **Read partial plaintext** — IC and freq analysis failed (only 6 bytes per
   group, need 100+), but partial decryption revealed readable words, allowing
   full key recovery: mysecret

## Flag
CTF{repeating_key_xor_falls_to_frequency_analysis}

## Real World Link
RC4 used in WEP WiFi encryption — broken by key reuse patterns.
WEP crackable in under 60 seconds.
