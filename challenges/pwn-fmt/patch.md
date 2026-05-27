# Fix — Format String Vulnerability

## Vulnerable Code
printf(input);

## Fixed Code
printf("%s", input);

## Why It Works
The format string is now hardcoded. User input is treated as
data only — printf never scans it for specifiers.

## Defence in Depth
- Enable compiler warnings: -Wformat -Wformat-security
- GCC already warns about this — treat warnings as errors in production
