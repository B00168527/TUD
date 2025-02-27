# Greatest Common Divisor

# Method to calc GCD using the Euclidean algorithm
def calc_GCD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# Test values provided
a = 12
b = 8

# Print result of the GCD method call
print(calc_GCD(a, b))

# flag numbers
a = 66528
b = 52920

# Print result of the GCD method call
print(calc_GCD(a, b))
