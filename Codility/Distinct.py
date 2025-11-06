'''
Write a function

def solution(A)

that, given an array A consisting of N integers, returns the number of distinct values in array A.

For example, given array A consisting of six elements such that:

 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1
the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

    
class Solution:
    def count_distinct(self,A):
        A.sort()
        if len(A)==0:
            return 0
        ans = 1
        for i in range(1,len(A)):
            if A[i]!=A[i-1]:
                ans +=1
        return ans


def main():
    arr = [[2,1,1,2,3,1]]

    for value in arr:
        print(f'There are {Solution().count_distinct(value)} distinct values in {value}')

if __name__ == "__main__":
    main()