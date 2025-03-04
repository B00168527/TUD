# Method to calcuate the values
def fermat(p, n):
    return (n**(p-1)) % p

# Test the value to get the flag
p = 65537
n = 273246787654

flag = fermat(p, n)
print("flag = " + str(flag))
