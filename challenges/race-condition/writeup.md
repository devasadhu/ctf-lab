# Challenge 11 — Race Condition (TOCTOU)

## Vulnerability
The /redeem endpoint checks balance then deducts in two separate steps
with a 100ms gap between them. With threaded=True, multiple requests
run concurrently and all pass the check before any deduction happens.

## Exploit
Fired 50 simultaneous requests using Python ThreadPoolExecutor.
All 50 hit the check while balance=1, all passed, all got the flag.
One token redeemed 50 times.

## Key Concepts
- TOCTOU: Time of Check to Time of Use — gap between check and use
- threaded=True: Flask handles each request in a separate thread
- Race window: the 100ms sleep is enough for all threads to pass the check
- Double-spend: same principle behind crypto exchange exploits

## Flag
CTF{race_conditions_break_atomicity}
