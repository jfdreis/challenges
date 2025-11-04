"""
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
"""
import math
class Solution:
    def missing(self, A: list[int]) -> int:
        n=len(A)
        expected_sum = (n+1)*(n+2)/2
        actual_sum = sum(A)
        return int(expected_sum - actual_sum)

def main():
    arr = [[1,2,4,5],[1,2,3,4,6]]
    for value in arr:
        print(f'The number missing in {value} is {Solution().missing(value)}')

if __name__ == "__main__":
    main()