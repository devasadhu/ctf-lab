# Fix — Race Condition

## Vulnerable Code
if balances.get(user, 0) < 1:
    return 403
time.sleep(0.1)
balances[user] -= 1

## Fixed Code
import threading
lock = threading.Lock()

with lock:
    if balances.get(user, 0) < 1:
        return jsonify({"error": "not enough tokens"}), 403
    balances[user] -= 1

## Why It Works
The lock makes check and deduction atomic — only one thread can
execute that block at a time. All other threads wait at the lock.
The race window is eliminated.

## Real World
Use database transactions with row-level locking:
SELECT balance FOR UPDATE — locks the row until transaction completes.
