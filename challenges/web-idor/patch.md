# Patch — IDOR

## Vulnerable Code
user_id = request.args.get("id")
# goes straight to DB query — no authorization check

## Patched Code
user_id = request.args.get("id")
if int(user_id) != session["user_id"]:
    return "Forbidden", 403

## Why This Works
The server already knows who the logged-in user is via the session.
Comparing the requested id against the session id ensures users can
only access their own profiles. Never trust client-supplied identifiers
for authorization decisions.
