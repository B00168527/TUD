# Given values
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

# Compute modulus and φ(N)
N = p * q
phi_n = (p - 1) * (q - 1)

# Compute private key exponent
d = pow(e, -1, phi_n)

ciphertext = 77578995801157823671636298847186723593814843845525223303932  # Example only

# Decrypt the ciphertext
plaintext = pow(ciphertext, d, N)
print(plaintext)
