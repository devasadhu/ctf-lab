# XSS — Cross-Site Scripting

## Vulnerability
The message board renders user input as raw HTML using Jinja2's `| safe` filter.
This allows any user to inject JavaScript that executes in every visitor's browser.

## Steps to Exploit
1. Visit /admin to plant the flag in the session cookie
2. Post this payload in the message board:
   <script>alert(document.cookie)</script>
3. The page renders the script tag as HTML
4. Browser executes it and displays the session cookie containing the flag

## Why It Works
The app uses `{{ msg | safe }}` in the template which disables Jinja2's
automatic HTML escaping. User input is dropped directly into the page as HTML.

## Real World Link
XSS is OWASP Top 10. The British Airways breach (2018) used XSS to steal
payment details from 380,000 customers via injected JavaScript on the checkout page.
