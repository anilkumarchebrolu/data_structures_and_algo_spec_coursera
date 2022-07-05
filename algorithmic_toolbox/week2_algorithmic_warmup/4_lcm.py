# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd_efficient(a, b):
    first_digit = max(a, b)
    second_digit = min(a, b)
    if first_digit % second_digit == 0:
        return second_digit
    return gcd_efficient(min(first_digit, second_digit), (first_digit % second_digit))

def lcm_efficient(a, b):
    gcd_value = gcd_efficient(a, b)
    lcm = (a * b)/gcd_value
    return int(lcm)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(lcm_naive(a, b))
    print(lcm_efficient(a, b))

