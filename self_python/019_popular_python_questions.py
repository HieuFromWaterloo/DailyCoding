# fibonacci >>>>>>

# Recursion


def fib(n):
    if n < 0:
        print("fuck no")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(9))

# dynamic:


def fib(n):
    a, b = 0, 1
    if n < 0:
        print("fuck no")
    elif n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


print(fib(9))

### DP ####

# Longest Common Sub Sequence
"""
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
"""

arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        print(j)
