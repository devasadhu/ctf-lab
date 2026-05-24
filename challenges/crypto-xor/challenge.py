flag = b"CTF{xor_is_not_secure_with_short_keys}"
key = 42

ciphertext = bytes([b ^ key for b in flag])
print(ciphertext.hex())
