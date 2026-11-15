
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)


def fib_nonrecursive(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


n = int(input("Enter number of terms: "))

print("Non-recursive Fibonacci:", end=" ")
for i in range(n):
    print(fib_nonrecursive(i), end=" ")

print("\nRecursive Fibonacci:", end=" ")
for i in range(n):
    print(fib_recursive(i), end=" ")
