def is_power_of_two(n):
    # Check if the number is a positive integer
    if n <= 0 or not isinstance(n, int):
        return False

    # Check if the number can be expressed as 2^k for some non-negative integer k
    return (n & (n - 1)) == 0

# Example usage:
number = int(input("Enter a number: "))
result = is_power_of_two(number)

if result:
    print(f"{number} is a power of 2.")
else:
    print(f"{number} is not a power of 2.")
