# Challenge 3 — XOR Cipher

## Vulnerability
The flag is encrypted with a single-byte repeating XOR key.
A single-byte key has only 256 possible values — small enough to brute force.

## Exploitation
1. Take the ciphertext (provided as hex)
2. Try all 256 possible keys
3. XOR the ciphertext with each key
4. Check which result contains "CTF{"
5. That result is the flag

## Flag
CTF{xor_is_not_secure_with_short_keys}

## Real World
The Vigenere cipher (repeating key XOR on text) was considered unbreakable
for centuries until frequency analysis defeated it. Single-byte XOR is even
weaker — modern encryption like AES uses keys that are 128 or 256 bits,
making brute force computationally impossible.
