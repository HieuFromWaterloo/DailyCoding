# Using pointers are not very applicable here because its an integer
# soln: get the the last digit at every iteration then iterate through backwards using modulo

def reverse_integer(n):
    """
    remainder = 1234 % 10 = 4
    n = 1234//10 = 123
    reverse = 0*10 + 4 = 4
    """

    reversed_integer = 0

    while n > 0:
        # n = 1234 -> n mod 10 = remainder = 4
        remainder = n % 10
        reversed_integer = reversed_integer * 10 + remainder
        # take a whole number
        n = n // 10 # // integer division

    return reversed_integer


if __name__ == '__main__':
    print(6 % 4)  # 2
    print(4 % 5)  # 4
    print(4 % 3)  # 1
    print(1234 % 10)  # 4
    print(1234 // 10)  # 123
    print(1 // 10)  # 0
    print(reverse_integer(12345678))
