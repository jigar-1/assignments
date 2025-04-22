print("a b pow(a, b)")
for a, b in zip([1,2,3,4,5], [2,3,4,5,6]):
    result = 1
    for _ in range(b):
        result *= a
    print(f"{a} {b} {result}")