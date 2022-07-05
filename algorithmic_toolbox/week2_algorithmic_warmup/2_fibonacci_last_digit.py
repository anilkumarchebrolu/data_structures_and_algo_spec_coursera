def calc_fibonacci_for_last_digit(n):
    my_fib_list = []
    my_fib_list.append(0)
    my_fib_list.append(1)
    for idx in range(2, n+1):
        my_fib_list.append((my_fib_list[idx-1] + my_fib_list[idx-2]) %10)
        my_fib_list[idx-2] = my_fib_list[idx-2] 
    return my_fib_list[n] % 10



def calc_efficient_fibonacci_last_digit(n):
    num1 = 0
    num2 = 1
    for idx in range(2, n+1):
        num3 = (num1 + num2)%10
        num1 = num2
        num2 = num3
    return num3

if __name__ == '__main__':
    n = int(input())
    print(calc_efficient_fibonacci_last_digit(n))