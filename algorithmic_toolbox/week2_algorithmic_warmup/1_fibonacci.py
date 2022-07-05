def calc_naive_fibonacci(n):
    if n <=1:
        return n
    
    return calc_naive_fibonacci(n - 1) + calc_naive_fibonacci(n -2)

def calc_efficient_fibonacci(n):
    my_fib_list = []
    my_fib_list.append(0)
    my_fib_list.append(1)
    for idx in range(2, n+1):
        my_fib_list.append(my_fib_list[idx-1] + my_fib_list[idx-2])
    
    return my_fib_list[n]


if __name__ == '__main__':
    n = int(input())
    # print(calc_naive_fibonacci(n))
    print(calc_efficient_fibonacci(n))