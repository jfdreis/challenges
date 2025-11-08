"""
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:

A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0
the function should return 5 because:

(3, 4) is a slice of A that has sum 4,
(2, 2) is a slice of A that has sum −6,
(0, 1) is a slice of A that has sum 5,
no other slice of A has sum greater than (0, 1).
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [−1,000,000..1,000,000];
the result will be an integer within the range [−2,147,483,648..2,147,483,647].
"""
 
class Solution:
    def max_slice_sum(self, A):
        max_sum_of_subarray = A[0] #maximum sum of a subarray until current position
        max_sum_found = A[0] #maximum sum of found up to this point
        n = len(A)
        for i in range(1,n):
            max_sum_of_subarray = max(A[i], max_sum_of_subarray + A[i]) # maximum sum up to position i (important when the maximum sum of a subarray is negative, or A[i] is negative)
            max_sum_found = max(max_sum_of_subarray, max_sum_found)
        return max_sum_found

def main():
    arr = [[3, 2, -6, 4, 0],[-2,-10]]
    for value in arr:
        print(f'The maximum sum of slice is {Solution().max_slice_sum(value)}')

if __name__ == "__main__":
    main()