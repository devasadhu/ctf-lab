# Challenge 6 — SSRF (Server-Side Request Forgery)

## Category
Web

## Difficulty
Intermediate

## Description
A Flask app has a /fetch endpoint that takes a URL and fetches it
server-side. An internal /internal/admin endpoint is protected and
not accessible directly. Use SSRF to reach it.

## Vulnerability
The /fetch endpoint accepted any URL with no restrictions, allowing
an attacker to make the server fetch internal endpoints on their behalf.

## Attack Steps
1. Try to access /internal/admin directly — blocked
2. Pass http://localhost:5000/internal/admin as the url parameter to /fetch
3. Server fetches it internally, adding the required internal header
4. Server returns the response — flag retrieved

## Root Cause
The server made outbound requests based on attacker-controlled input
with no validation of the target URL.

## Fix
Whitelist allowed domains. Reject any URL that doesn't match a known
safe domain. Never let user input control where the server makes requests.

## Real World
Capital One breach 2019 — attacker used SSRF to hit the AWS metadata
endpoint (169.254.169.254) and steal IAM credentials. 100 million
customer records exposed.
