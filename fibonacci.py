""""
Fibonacci series:
he sum of two elements defines the next
"""
a, b = 0, 1

while b < 100:
    print b
    a, b = b, a + b


# No shadow variables
def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    x, y = 0, 1
    while x < n:
        result.append(x)
        x, y = y, x + y
    return result


f100 = fib2(100)
print f100
