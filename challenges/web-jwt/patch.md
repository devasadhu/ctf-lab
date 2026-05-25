# Patch — JWT None Algorithm

## Vulnerable Code
decoded = jwt.decode(token, options={"verify_signature": False})

## Fixed Code
decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

## Why This Works
The server now explicitly specifies which algorithm is acceptable.
The attacker cannot override this by modifying the token header.
Signature verification is always enforced.
