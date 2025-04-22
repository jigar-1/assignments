class NonIntResultException(Exception):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        super().__init__(f"{numerator} divided by {denominator} is not an integer")

def divide(numerator, denominator):
    result = numerator / denominator
    if not result.is_integer():
        raise NonIntResultException(numerator, denominator)
    return int(result)

# Test code
try:
    print(divide(10, 2))  # Should print 5
    print(divide(7, 2))   # Should raise an exception
except NonIntResultException as e:
    print(e)