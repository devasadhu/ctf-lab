y# challenge.py
flag = b"CTF{repeating_key_xor_falls_to_frequency_analysis}"
key = b"mysecret"

ciphertext = bytes([flag[i] ^ key[i % len(key)] for i in range(len(flag))])
print(ciphertext.hex())
