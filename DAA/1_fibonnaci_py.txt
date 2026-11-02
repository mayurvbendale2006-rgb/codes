# Recursive Function
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Non-Recursive Function
def fibonacci_non_recursive(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c


# Main Program
n = int(input("Enter number of terms: "))

if n < 0:
    print("Invalid input")
else:
    print("Fibonacci using Recursion:")
    for i in range(n):
        print(fibonacci_recursive(i), end=" ")

    print("\nFibonacci using Non-Recursion:")
    fibonacci_non_recursive(n)
