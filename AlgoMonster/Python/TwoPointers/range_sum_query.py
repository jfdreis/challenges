"""
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= left <= right < nums.length
At most 104 calls will be made to sumRange.

https://leetcode.com/problems/range-sum-query-immutable/description/

"""

class NumArray:

    def __init__(self, nums: list[int]):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        self.nums = prefix_sum

    def sumRange(self, left: int, right: int) -> int:
        left_sum = self.nums[left]
        right_sum = self.nums[right+1]
        return right_sum - left_sum

class NumArray_trivial:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        # We are assum left <= right
        current_sum =0
        while left <= right:
            current_sum += self.nums[left]
            left+=1
        return current_sum

def main():
    if __name__ == "__main__":
        nums = [-2, 0, 3, -5, 2, -1]
        numArray = NumArray(nums)

        # list of (left, right) pairs
        ranges = [(0, 2), (2, 5), (0, 5)]

        # run all queries
        for left, right in ranges:
            val = numArray.sumRange(left, right)
            print(f"sumRange({left}, {right}) = {val}")

if __name__ == "__main__":
    main()