from sympy.ntheory.modular import crt

# Given values
mods = [5, 11, 17]
remainders = [2, 3, 5]

# Solve using Chinese Remainder Theorem from sympy
x, mod = crt(mods, remainders)

print(x)
