'''
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

    
class Solution:
    def missing(self, A: list[int]) -> int:
        N = len(A)
        missing_list = [False] * N
        for value in A:
            if 0 < value <= N:
                missing_list[value-1] = True
        for (i,value) in enumerate(missing_list):
            if not value:
                return i+1
        return N+1

def main():
    arr = [[1, 3, 6, 4, 1, 2],
           [1, 2, 3],
           [-1, -3]]

    for value in arr:
        print(f'The smallest missing positive integer in {value} is {Solution().missing(value)}')  

if __name__ == "__main__":
    main()