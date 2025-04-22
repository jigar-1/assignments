numbers = []
while True:
    num = int(input("Enter an integer (0 to stop): "))
    if num == 0:
        break
    numbers.append(num)

numbers.sort()
for num in numbers:
    print(num)