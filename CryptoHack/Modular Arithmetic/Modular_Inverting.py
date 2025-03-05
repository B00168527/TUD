# Given the formula 3 ⋅ d ≡ 1 mod 13

# loop through all ints up to 1000 to find the answer
for d in range (1000):
    if ((3 * d) % 13) == 1:
        print("Answer is: " + str(d))
        break
