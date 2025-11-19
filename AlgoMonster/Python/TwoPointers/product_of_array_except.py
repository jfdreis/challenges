"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

[ 1, 2, 3, 4, 5, 6]

[ 1, 1, 2, 6, 24, 120 ]

https://leetcode.com/problems/product-of-array-except-self/description/

"""

from collections import deque

def productExceptSelf_simple(self, nums: list[int]) -> list[int]:
    n = len(nums)
    prefix_product = deque([1])
    sufix_product = deque([1])

    for i in range(n-1):
        prefix_product.append(prefix_product[-1]*nums[i])
    for i in range(n-1,0,-1):
        sufix_product.appendleft(sufix_product[0]*nums[i])
    ans=[]
    for i in range(n):
        ans.append(prefix_product[i]*sufix_product[i])
    return ans

def productExceptSelf_optimized(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [1] * n

    # Compute prefix products in ans
    prefix = 1
    for i in range(n):
        ans[i] = prefix
        prefix *= nums[i]

    # Multiply by suffix products directly
    suffix = 1
    for i in range(n-1, -1, -1):
        ans[i] *= suffix
        suffix *= nums[i]

    return ans



        


def main():
    examples = [
        [1, 2, 3, 4],
        [-1, 1, 0, -3, 3],
        [5, 6, 2],
        [1, 1, 1, 1]
    ]

    for nums in examples:
        result = productExceptSelf_optimized(nums)
        print(f"Input: {nums}")
        print(f"Output: {result}")
        print("-" * 60)

if __name__ == "__main__":
    main()
