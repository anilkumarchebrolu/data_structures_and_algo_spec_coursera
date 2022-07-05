# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_efficient(a, b):
    first_digit = max(a, b)
    second_digit = min(a, b)
    if first_digit % second_digit == 0:
        return second_digit
    return gcd_efficient(min(first_digit, second_digit), (first_digit % second_digit))

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_efficient(a, b))
