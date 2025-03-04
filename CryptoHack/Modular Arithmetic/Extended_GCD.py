# Function to find Extended Euclidean
def extended(num1, num2):
    # Return when num1 is 0
    if num1 == 0:
        return[num2, 0, 1]
    else:
        # Calulcate num2 mod num1
        num2_mod_num1 = num2 % num1
        # Use recurison until num1 == 0
        gcd, num1A, num2B = extended(num2_mod_num1, num1)
        # Return GCD, u and v
        return [gcd, num2B - (num2 // num1) * num1A, num1A]

print(extended(26513, 32321))
