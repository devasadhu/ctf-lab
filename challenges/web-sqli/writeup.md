# Challenge 1: Blind SQL Injection

## Vulnerability
The login endpoint constructs SQL queries by concatenating user input directly
into the query string, allowing an attacker to modify the query's logic.

## Impact
An attacker can extract data from any table in the database without 
authentication, including tables the login query never references.

## Exploit Steps
1. Confirm injection point by testing `' OR '1'='1` as username
2. Use subqueries with `substr()` to test flag characters one at a time
3. Automate with a script that sends one request per character per position
4. Reconstruct the flag from boolean responses ("Welcome back" vs "Invalid")

## Root Cause
This is because it is interpreted as sql query and not as pure data, the query is run answer returned as 1 so its
taken as user response is correct, without even taking username password seperately.

## Patch
Changed to parameterized queries: `c.execute(query, (username,))`

## Why The Patch Works
Because the username is passed as a tuple separately from the query, SQLite treats it as a literal value and never
interprets it as SQL code, so injected logic like OR '1'='1 has no effect on the query structure.

## Real World Reference
This vulnerability class was used in the 2009 Heartland Payment Systems breach
— 130 million credit card numbers stolen via SQL injection.
