# Challenge 8 — Buffer Overflow (ret2win)

## Category
Pwn (Binary Exploitation)

## Difficulty
Intermediate-Hard

## Vulnerability
The login() function uses gets() which reads input with no length limit.
The buffer is 32 bytes but gets() will write as many bytes as you give it,
overflowing into adjacent stack memory including the return address.

## Attack Steps
1. Find the address of win() using objdump
2. Generate a cyclic pattern to find the exact offset to the return address
3. Craft payload: 40 bytes padding + address of win() in little-endian
4. Send payload — when login() returns, CPU jumps to win() instead of main()

## Key Concepts
- Stack stores local variables and return address in sequence
- Overwriting return address = controlling where the program goes next
- p64() converts address to little-endian bytes the CPU expects
- Offset must be measured after every recompile

## Fix
Replace gets() with fgets(buffer, 32, stdin) to enforce a length limit.

## Real World
CVE-2021-3156 — sudo heap buffer overflow affecting Linux systems for 10 years.
Buffer overflows in C remain one of the most exploited vulnerability classes.
