#Uses python3

import sys

def is_greater_or_equal(result, x):
    num1 = int(str(result) + str(x))
    num2 = int(str(x) + str(result))
    return num1 > num2


def largest_number(a):
    #write your code here
    res = ""
    my_list = list(map(int, a.copy()))
    output_list = []
    for _ in a:
        max_digit = 0
        for digit in my_list:
            if not is_greater_or_equal(max_digit, digit):
                max_digit = digit
        output_list.append(max_digit)
        my_list.pop(my_list.index(max_digit))
    res = "".join([str(val) for val in output_list])
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
