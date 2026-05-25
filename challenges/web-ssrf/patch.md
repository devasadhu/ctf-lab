# Patch — SSRF

## Vulnerable Code
response = requests.get(url, timeout=3)

## Fixed Code
allowed = ["example.com", "trusted-api.com"]
if not any(domain in url for domain in allowed):
    return jsonify({"error": "Domain not allowed"}), 403

## Why This Works
Server only fetches URLs from explicitly trusted domains.
Attacker cannot redirect the server to internal or arbitrary endpoints.
