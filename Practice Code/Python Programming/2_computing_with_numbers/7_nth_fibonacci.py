"""
    # 7_nth_fibonacci.py
    # This program computes the nth Fibonacci number where n is a value input by the user.
    # Fibonacci sequence begins: 0, 1, 1, 2, 3, 5, 8, 13, if n = 6, then the result is 8.
    Created by: temikelani on: 1/25/20
"""


def nth_fib(n):
    # initialise the first fib number as curr_fib and a variable prev_fin to hold the previos fib values
    # the next fibonacci num is calculated be summing the current one and the previous one.
    prev_fib = 0
    curr_fib = 1

    for i in range(n - 1):
        fib = prev_fib + curr_fib
        prev_fib = curr_fib
        curr_fib = fib
        print(curr_fib, prev_fib)

    return curr_fib


def main():
    print("This program computes the nth Fibonacci number where n (>= 1) is a value input by the user.")
    n = int(input("Enter value of n here: "))
    print(" The", str(n) + "th fib number is:", nth_fib(n))

main()