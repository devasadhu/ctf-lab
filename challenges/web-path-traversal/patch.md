# Patch — Path Traversal

## Vulnerable Code
filepath = os.path.join(BASE_DIR, filename)

## Fixed Code
filepath = os.path.realpath(os.path.join(BASE_DIR, filename))
if not filepath.startswith(BASE_DIR):
    return "Access denied", 403

## Why This Works
os.path.realpath() resolves all ../ sequences to an absolute path.
The startswith check ensures the final path is inside the allowed folder.
No matter how many ../ the attacker adds, they cannot escape BASE_DIR.
