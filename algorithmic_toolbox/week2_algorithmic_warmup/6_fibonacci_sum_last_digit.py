# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    _sum     = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) %10
        _sum += current 
        _sum = _sum % 10

    return _sum % 10


def pisanoPeriod(m):
    previous, current = 0, 1
    _sum = 1
    for i in range(0, m * m):
        previous, current \
        = current, (previous + current) % m
        _sum += current
        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return _sum, i + 1

def get_fibonacci_huge_efficient(n, m=10):
    one_iter_sum, pp = pisanoPeriod(m)
    n = n%pp
    _sum = 1
    if n > pp:
        _sum = one_iter_sum * n

    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) %10
        _sum += current

    return _sum % m

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_huge_efficient(n))
