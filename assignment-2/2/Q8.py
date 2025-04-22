numbers = [45, 22, 14, 65, 97, 72]
result = []

for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        result.append("fizzbuzz")
    elif num % 3 == 0:
        result.append("fizz")
    elif num % 5 == 0:
        result.append("buzz")
    else:
        result.append(num)

print(result)