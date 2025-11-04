"""
An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given

    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given

    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""

def binary_rep(value: int) -> str:
    return bin(value)[2:]
    
class Solution:
    def rotate(self, A: list[int], K: int) -> list[int]:
        rotate_A= [0]* len(A)
        n = len(A)
        for i in range(n):
            rotate_A[(i+K)% n]= A[i]
        return rotate_A
    def rotate_optimized(self,A: list[int], K: int) -> list[int]:
    # Implement your solution here
        n = len(A)
        if n <= 1:
            return A
        K = K % n
        A = A[-K:] + A[:-K]
        return A

def main():
    arr = [([529,20,15,32,1041,32],2)]
    for value in arr:
        print(f'The origial array is {value[0]}')
        print(f"The rotation is {Solution().rotate(value[0],value[1])}")
        print(f"The rotation is {Solution().rotate_optimized(value[0],value[1])}")

if __name__ == "__main__":
    main()