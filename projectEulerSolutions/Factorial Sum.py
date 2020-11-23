# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
    return factorial

def factorial_sum(n):
    fact = factorial(n)
    first_step = [int(d) for d in str(fact)]
    ans = 0
    for i in first_step:
        ans = ans + i
    return ans

print(factorial_sum(100))