"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 
Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

https://leetcode.com/problems/minimum-size-subarray-sum/description/

"""

def minimum_size_array(arr: list[int], target: int) -> int:
    if sum(arr)< target:
        return 0
    ans = len(arr)
    pointer_2 = 0
    current_sum = 0
    pointer_1=0
    while pointer_1 <= pointer_2 and pointer_2 < len(arr):
        while pointer_2 < len(arr):
            current_sum = current_sum + arr[pointer_2]
            print(f"i={pointer_1}, j={pointer_2}, sum={current_sum}, ans = {ans}")
            if current_sum < target:
                pointer_2 += 1
            elif pointer_2 - pointer_1 + 1 < ans:
                ans = pointer_2 - pointer_1 + 1
                current_sum = current_sum - arr[pointer_1]-arr[pointer_2]
                pointer_1 += 1
            else:
                current_sum = current_sum - arr[pointer_1] - arr[pointer_2]
                pointer_1 += 1
    return ans


def minimum_size_array_optimized(arr: list[int], target: int) -> int:
    n= len(arr)
    ans = float('inf')
    left = 0
    current_sum = 0
    for right in range(n):
        current_sum += arr[right]
        while current_sum >= target:
            ans = min(ans, right - left + 1)
            if ans == 1:
                return ans
            current_sum = current_sum - arr[left]
            left += 1
    return 0 if ans == float('inf') else ans
                

def main():
    examples = [
        ([2,3,1,2,4,3], 7),
        ([1,4,4], 4),
        ([1,1,1,1,1,1,1,1], 11)
    ]

    for arr in examples:
        print(f"The min length  {minimum_size_array_optimized(arr[0],arr[1])}")
        print("-" * 60)

if __name__ == "__main__":
    main()