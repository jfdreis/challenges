'''A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

content_copy
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

def solution(A)
content_copy

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

content_copy
the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].
'''
class Solution:
    def max_slice_sum(self, A):
        n = len(A)
        if n < 3:
            return 0  # no valid double slice

        # Step 1: compute max subarray sum ending at each position (from the left)
        max_end = [0] * n
        for i in range(1, n - 1):
            max_end[i] = max(0, max_end[i - 1] + A[i])

        # Step 2: compute max subarray sum starting at each position (from the right)
        max_start = [0] * n
        for i in range(n - 2, 0, -1):
            max_start[i] = max(0, max_start[i + 1] + A[i])

        # Step 3: find the best place to "cut" the middle element (Y)
        max_double_slice = 0
        for Y in range(1, n - 1):
            # A[Y] is excluded from both sides
            current_sum = max_end[Y - 1] + max_start[Y + 1]
            max_double_slice = max(max_double_slice, current_sum)

        return max_double_slice

def main():
    arr = [[3,2,6,-1,4,5,-1,2]]
    for value in arr:
        print(f'The maximum sum of slice is {Solution().max_slice_sum(value)}')

if __name__ == "__main__":
    main()

