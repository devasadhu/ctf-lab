# Challenge 2 — IDOR (Insecure Direct Object Reference)

## Vulnerability
The profile page at `/user?id=N` fetches user data based on a client-supplied
id parameter. The server never checks whether the logged-in user is authorized
to view the requested profile.

## Exploitation
1. Log in as guest (guest:guest)
2. Observe the URL: /user?id=3
3. Change id to 1 in the browser URL bar
4. Server returns admin profile containing the flag

No tools required. The browser is the exploit.

## Flag
CTF{idor_means_trust_no_client_input}

## Real World
Facebook exposed private photos and friend lists via IDOR vulnerabilities.
IDOR is consistently listed in the OWASP Top 10 as a critical access control flaw.
