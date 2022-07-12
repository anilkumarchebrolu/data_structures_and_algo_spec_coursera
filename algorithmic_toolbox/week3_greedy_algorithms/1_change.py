# Uses python3
import sys

def get_change(m):
    num_coins = 0
    if m <=0:
        return num_coins
    while m > 0:
        if m >= 10:
            m -= 10
        elif m >= 5:
            m-=5
        elif m<=4:
            m-=1
        num_coins += 1
    return num_coins

if __name__ == '__main__':
    # m = int(sys.stdin.read())
    m = int(input())
    print(get_change(m))
