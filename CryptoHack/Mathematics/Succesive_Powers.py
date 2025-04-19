from sympy import isprime

# Values given in the challenge
values = [588,665,216,113,642,4,836,114,851,492,819,237]
# Get number of values for looping
values_len = len(values)

# Get all 3 digit primes
primes = [n for n in range(100,1000) if isprime(n)]

# Print all the 3 digit primes
print(primes)

# Loop through each prime
for p in primes:
    # Loop through each number from 1 to the prime value
    for n in range(1, p):

        for i, power in enumerate(values):
            # Check if all values have been checked
            if i == (values_len - 1):
                print(p)
                print(n)
                exit()
            # Check the next value matches
            elif not (n * power) % p == values[i + 1]:
                break
