# Challenge 7 — Path Traversal

## Category
Web

## Difficulty
Beginner-Intermediate

## Description
A Flask app serves files from a /files directory via a ?name= parameter.
A secret file sits outside that directory. Use path traversal to read it.

## Vulnerability
The server joined BASE_DIR with user-supplied filename directly,
without checking if the final path escaped the intended directory.

## Attack Steps
1. Normal request: /files?name=readme.txt — works as intended
2. Traversal: /files?name=../secret.txt
3. Server resolves path to secret.txt outside the files/ folder
4. File returned — flag retrieved

## Root Cause
os.path.join(BASE_DIR, filename) trusts user input.
../  is valid OS path syntax that climbs directory levels.
No check was done on the final resolved path.

## Fix
Use os.path.realpath() to resolve the full path first, then verify
it still starts with BASE_DIR before opening the file.

## Real World
CVE-2021-41773 — Apache HTTP Server path traversal. Attackers could
read files outside the web root on misconfigured servers.
Patched within days due to active exploitation in the wild.
