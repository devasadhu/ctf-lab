# Challenge 5 — JWT None Algorithm Attack

## Category
Web

## Difficulty
Beginner-Intermediate

## Description
A Flask app issues JWT tokens on login. The /admin route is protected
by role — only admin can access it. You log in as guest.

## Vulnerability
The server accepted "none" as a valid algorithm in the JWT header.
This disabled signature verification entirely, allowing anyone to
forge a token with any role.

## Attack Steps
1. Log in as guest — receive a valid JWT
2. Decode the header and payload (just base64)
3. Modify payload: change role from "user" to "admin"
4. Change header: set alg to "none"
5. Remove the signature — keep the trailing dot
6. Send the forged token to /admin — server accepts it

## Root Cause
Server trusted the alg field from the token itself (attacker-controlled input)
to decide whether to verify the signature.

## Fix
Hardcode the allowed algorithm on the server side:
jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
Never accept "none" as a valid algorithm.

## Real World
CVE-2015-9235 — affected jsonwebtoken, the most popular JWT library
for Node.js. Millions of applications were vulnerable.
