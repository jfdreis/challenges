"""
Given an array of integers and an integer target, find a subarray that sums to target and return the start and end indices of the subarray.

Input: arr: 1 -20 -3 30 5 4 target: 7

Output: 1 4

Explanation: -20 - 3 + 30 = 7. The indices for subarray [-20,-3,30] is 1 and 4 (right exclusive).
"""


def prefix_sum_array_target(arr: list[int],target: int) -> list[int]:
    # Idea, we sum all values up to a given index
    # Say that we are at index j and have value_j
    # If there was a previous index i with value_i such that
    # value_j-value_i = target then we want the indices between i and j.
    prefix_sums = {0: 0} # key = summed value up to position i (including i), value = i 
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        complement = cur_sum - target
        if complement in prefix_sums:
            return [prefix_sums[complement], i + 1]
        prefix_sums[cur_sum] = i + 1
    return []

def main():
    examples = [
        ([1, -20, -3, 30, 5, 4],7),
    ]

    for arr in examples:
        print(f"The start and end indices of a subarray that sums {arr[1]} are:\n {prefix_sum_array_target(arr[0],arr[1])}")
        print("-" * 60)

if __name__ == "__main__":
    main()
