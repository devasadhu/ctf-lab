# Patch — XSS Fix

## The Fix
Remove `| safe` from the template. Use plain `{{ msg }}` instead.

Change:
    {{ msg | safe }}

To:
    {{ msg }}

## Why It Works
Jinja2 escapes HTML characters by default. `<script>` becomes `&lt;script&gt;`
which the browser displays as text and never executes.

## Defence in Depth
- Never use `| safe` on user input
- Set SESSION_COOKIE_HTTPONLY = True so cookies can't be read by JavaScript
- Implement Content Security Policy (CSP) headers to restrict script execution
