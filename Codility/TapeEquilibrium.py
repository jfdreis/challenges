"""
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
"""
import math
class Solution:
    # This has O(n^2) complexity
    def minimal_diff(self, A: list[int]) -> int:
        min_value = float('inf')
        n = len(A)
        for i in range(1,n):
            diff = abs(sum(A[:i])-sum(A[i:]))
            min_value = min(min_value,diff)
        return int(min_value)
    # This has O(n) complexity
    def minimal_diff_optimized(self, A: list[int]) -> int:
        min_value = float('inf')
        n = len(A)
        if n == 0:
            return 0
        total_sum=sum(A)
        left_sum=0
        for i in range(n-1):
            left_sum += A[i]
            right_sum = total_sum - left_sum
            diff = abs(left_sum-right_sum)
            min_value = min(min_value,diff)
        return int(min_value)

def main():
    arr = [[3,1,2,4,3]]
    for value in arr:
        print(f'''The minimum difference between the 
              left_sum and the righ_sum in {value} is {Solution().minimal_diff_optimized(value)}''')

if __name__ == "__main__":
    main()