def fakt(n):
    if n == 1:
        return 1
    else:
        return n * fakt(n-1)


def multiply1(a, b):
    if (b == 0):
        return 0

    if (b > 0):
        return (a + multiply1(a, b - 1))

    if (b < 0):
        return -multiply1(a, -b)


print(fakt(5))
print(multiply1(5, 3))
