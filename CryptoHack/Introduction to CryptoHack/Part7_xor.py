from Crypto.Util.number import *
from pwn import *

# Set the values mentioned in the challenge
sampleString = "label"
sampleInt = 13

# Xor the two values using the method mentioned
flag = xor(sampleString, sampleInt)

# print the flag
print(flag)
