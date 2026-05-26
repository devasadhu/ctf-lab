# Patch — Buffer Overflow Fix

## Vulnerable Code
gets(buffer);

## Fixed Code
fgets(buffer, 32, stdin);

## Why This Works
fgets() takes a size argument and stops reading at that limit.
No matter how much input the attacker sends, only 32 bytes are written.
The return address is never reached.

## Defence in Depth
- Use fgets() or scanf() with length limits, never gets()
- Compile with stack canaries: -fstack-protector
- Enable PIE: -pie (randomizes memory addresses)
- Enable NX: marks stack non-executable
- These protections make exploitation significantly harder
