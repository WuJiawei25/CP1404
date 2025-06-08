import random

print(random.randint(5, 20))  # line 1
# Random integer between 5 and 20
# Smallest = 5, Largest = 20

print(random.randrange(3, 10, 2))  # line 2
# 3, 5, 7, 9
# Smallest = 3, Largest = 9
# could not produce a 4

print(random.uniform(2.5, 5.5))  # line 3
# Random float between 2.5 and 5.5
# Smallest ≈ 2.5, Largest ≈ 5.5

random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")