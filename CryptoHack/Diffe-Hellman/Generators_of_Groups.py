# Value given in the challenge
p = 28151

# Function to find the smallest primitive number
def is_primitive(g, p):
    # Checks all numbers up to p-1 (except 1)
    for i in range(1, p - 1):
        if pow(g, i, p) == 1:
            return False
    return True

# Loop through all numbers from 2 to p
for g in range(2, p):
    if is_primitive(g, p):
        # Print value and break as it's the smallest
        print(g)
        break
