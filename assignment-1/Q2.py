
def my_floor(n):
    integer_part = int(n)
    return integer_part if n >= 0 or n == integer_part else integer_part - 1

def my_ceil(n):
    integer_part = int(n)
    return integer_part if n <= integer_part else integer_part + 1

# Example usage:
value = 2.7
print(f"Floor of {value}:", my_floor(value))
print(f"Ceil of {value}:", my_ceil(value))
