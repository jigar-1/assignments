n = int(input("Enter a number: "))
reversed_n = int(str(n)[::-1]) if n >=0 else -int(str(-n)[::-1])
print(reversed_n)