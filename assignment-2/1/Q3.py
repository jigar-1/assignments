numbers = []
while True:
    inp = input("Enter an integer (blank to stop): ")
    if inp == "":
        break
    numbers.append(int(inp))

negatives = [num for num in numbers if num < 0]
zeros = [num for num in numbers if num == 0]
positives = [num for num in numbers if num > 0]

for num in negatives + zeros + positives:
    print(num)