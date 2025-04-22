def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

start = int(input("Start: "))
end = int(input("End: "))
primes = [str(n) for n in range(start, end+1) if is_prime(n)]
print("Primes:", ' '.join(primes))