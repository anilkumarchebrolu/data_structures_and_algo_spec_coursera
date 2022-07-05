# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

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
        previous, current = current, (previous + current) % m
        _sum += current

    return _sum % m

def fibonacci_partial_sum_efficient(from_, to):
    from_sum = get_fibonacci_huge_efficient(from_ - 1, m=10)
    to_sum = get_fibonacci_huge_efficient(to, m=100)
    return (to_sum - from_sum) % 10

if __name__ == '__main__':
    # input = sys.stdin.read();
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_efficient(from_, to))
