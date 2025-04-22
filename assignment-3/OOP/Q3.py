class PrimeIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.end:
            if self.is_prime(self.start):
                prime = self.start
                self.start += 1
                return prime
            self.start += 1
        raise StopIteration

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

# Test iterator
n1 = int(input("Enter the start number: "))
n2 = int(input("Enter the end number: "))

print("Prime numbers using iterator:")
for prime in PrimeIterator(n1, n2):
    print(prime)



def prime_generator(start, end):
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                yield num

# Test generator
n1 = int(input("Enter the start number: "))
n2 = int(input("Enter the end number: "))

print("Prime numbers using generator:")
for prime in prime_generator(n1, n2):
    print(prime)