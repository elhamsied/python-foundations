# Python Foundations
# Author: Elham Seid Ahmed

import time

# -------------------------------
# LEVEL 1: Optimized Prime Checker
# -------------------------------

def is_prime_optimized(n):
    """Efficient prime check using sqrt optimization."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# -------------------------------
# LEVEL 2: Fibonacci (Naive vs Optimized)
# -------------------------------

def fib_naive(n):
    """Recursive Fibonacci (slow)."""
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)


memo = {}

def fib_memo(n):
    """Memoized Fibonacci (fast)."""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]


def compare_fibonacci(n):
    print(f"\nComparing Fibonacci for n={n}")

    start = time.time()
    naive_result = fib_naive(n)
    naive_time = time.time() - start

    start = time.time()
    memo_result = fib_memo(n)
    memo_time = time.time() - start

    print(f"Naive Result: {naive_result} | Time: {naive_time:.6f}s")
    print(f"Memo Result: {memo_result} | Time: {memo_time:.6f}s")


# -------------------------------
# LEVEL 3: Advanced CLI Calculator
# -------------------------------

history = []

def calculate():
    while True:
        print("\n--- Advanced Calculator ---")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. View History\n6. Exit")

        choice = input("Choose option: ")

        if choice == '6':
            print("Exiting calculator...")
            break

        if choice == '5':
            print("\n--- History ---")
            for h in history:
                print(h)
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers.")
            continue

        if choice == '1':
            result = num1 + num2
            operation = "+"
        elif choice == '2':
            result = num1 - num2
            operation = "-"
        elif choice == '3':
            result = num1 * num2
            operation = "*"
        elif choice == '4':
            if num2 == 0:
                print("Cannot divide by zero!")
                continue
            result = num1 / num2
            operation = "/"
        else:
            print("Invalid choice!")
            continue

        output = f"{num1} {operation} {num2} = {result}"
        print("Result:", result)
        history.append(output)


# -------------------------------
# MAIN PROGRAM
# -------------------------------

if __name__ == "__main__":
    print("=== Advanced Python Assignment ===")

    # Level 1
    num = int(input("\nEnter number to check prime: "))
    print("Is Prime?", is_prime_optimized(num))

    # Level 2
    n = int(input("\nEnter n for Fibonacci comparison: "))
    compare_fibonacci(n)

    # Level 3
    calculate()
