def max_pairwise_product_naive(list_of_nums):
    result = 0
    for i in range(len(list_of_nums)):
        for j in range(i+1, len(list_of_nums)):
            prod = list_of_nums[i] * list_of_nums[j]
            if prod > result:
                result = prod
    return result

def find_maximum_value_in_list(list_of_nums, skip_index=None):
    max_value = 0
    max_idx = 0
    for idx, num in enumerate(list_of_nums):
        if type(skip_index) == int:
            if skip_index == idx:
                continue
        if num > max_value:
            max_value = num
            max_idx = idx
    return max_value, max_idx


def max_pairwise_product(list_of_nums):
    max_value, max_idx = find_maximum_value_in_list(list_of_nums)
    second_max_value,  second_max_idx = find_maximum_value_in_list(list_of_nums, skip_index=max_idx)
    return max_value * second_max_value

if __name__ == '__main__':
    # num_elements = input("number of elements: ")
    # numbers = input("Elements in a single line separated by spaces: ")
    # print(f"Result is: {max_pairwise_product_naive(list(map(int, numbers.split())))}")
    # print(f"Result is: {max_pairwise_product(list(map(int, numbers.split())))}")

    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
    