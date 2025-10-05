"""
Two Sum Sorted
Given an array of integers sorted in ascending order, find two numbers that add up to a given target. Return the indices of the two numbers in ascending order. You can assume elements in the array are unique and there is only one solution. Do this in O(n) time and with constant auxiliary space.

Input:

arr: a sorted integer array
target: the target sum we want to reach
Sample Input: [2, 3, 4, 5, 8, 11, 18], 8

Sample Output: 1 3

"""


def two_sum_sorted(arr: list[int], target: int) -> list[int]:
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]  # Return [-1, -1] if no solution is found

def main():
    examples = [
        ([2, 3, 4, 5, 8, 11, 18], 8),
        ([2,7,11,15], 9),
        ([1, 2, 3, 4, 6], 6),
        ([2, 5, 9, 11], 11),
        ([1, 2, 3, 4, 5], 10),  # No solution case
        ([], 5),                # Empty array case
        ([1], 1),               # Single element case
    ]

    for arr in examples:
        print(f"The array after moving zeros to the end is {two_sum_sorted(arr[0], arr[1])}")
        print("-" * 30)

if __name__ == "__main__":
    main()