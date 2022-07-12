# Uses python3
import sys

def get_max_density_and_index(densities, skip_indices):
    max_idx = 0
    max_density = 0
    for idx, density in enumerate(densities):
        if idx in skip_indices:
            continue
        if density > max_density:
            max_idx = idx
            max_density = density
    return max_idx


def get_optimal_value(capacity, weights, values):
    densities =[value/weight for weight, value in zip(weights, values)]
    total_value = 0
    used_indices = []

    for _ in densities:
        max_idx = get_max_density_and_index(densities, used_indices)
        used_indices.append(max_idx)
        if capacity == 0:
            continue
        if capacity >= weights[max_idx]:
            capacity = capacity - weights[max_idx]
            total_value += densities[max_idx] * weights[max_idx]
        elif capacity<= weights[max_idx]:
            total_value += densities[max_idx] * capacity
            capacity = 0
    return total_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
