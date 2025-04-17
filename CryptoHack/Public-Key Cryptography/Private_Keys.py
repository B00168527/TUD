# Given values
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

# Compute φ(N) = (p - 1)(q - 1)
phi_n = (p - 1) * (q - 1)

# Compute modular inverse of e mod φ(N)
d = pow(e, -1, phi_n)

print(d)
