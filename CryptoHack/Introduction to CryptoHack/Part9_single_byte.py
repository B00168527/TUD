from Crypto.Util.number import *
from pwn import *

# Cipher in hex given
cipher = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

# Conver to bytes from hex
cipher_in_bytes = bytes.fromhex(cipher)

# Loop through all bytes and xor with cipher. Print values to inspect.
for i in range(256):
    print(xor(cipher_in_bytes, i))
