import random

def random_number_generator(n, low, high):
    for _ in range(n):
        yield random.randint(low, high)

# Test generator
n = int(input("Enter the number of random numbers: "))
low = int(input("Enter the low number: "))
high = int(input("Enter the high number: "))

print("Random numbers:")
for num in random_number_generator(n, low, high):
    print(num)