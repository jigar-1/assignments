class NonBinaryStringException(Exception):
    pass

def binaryToDecimal(binaryString):
    if not all(c in '01' for c in binaryString):
        raise NonBinaryStringException("The string is not a binary string")
    return int(binaryString, 2)

# Test code
try:
    print(binaryToDecimal("1010"))  # Should print 10
    print(binaryToDecimal("1020"))  # Should raise an exception
except NonBinaryStringException as e:
    print(e)