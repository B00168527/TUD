p = 29
for a in range(p):
    i = a**2
    if i > p:
        residue = i % p
        print("Residue for " + str(i) + " is " +  str(residue))
