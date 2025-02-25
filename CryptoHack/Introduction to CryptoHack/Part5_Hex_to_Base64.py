import base64

# Convert from hex and print
bytesVal = bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")
print(bytesVal)

# Print the base64 value
print(base64.b64encode(bytesVal))
