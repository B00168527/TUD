# Import the library from sympy
from sympy.ntheory import factorint

# Set the value given in the challenge
n = 510143758735509025530880200653196460532653147

# Run the factorint function from sympy on the number
factors = factorint(n)

print("Prime factors:")
for prime, exp in factors.items():
    # Print the primes
    print(f"{prime}")
