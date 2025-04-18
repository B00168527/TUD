import math

total_hashes = 2048
probability_no_collision = 0.5

# Use the formula: (1 - 1/N)^k = 0.5  ⇒  k = log(0.5) / log((N-1)/N)
k = math.log(1 - probability_no_collision) / math.log((total_hashes - 1) / total_hashes)
print(k)
