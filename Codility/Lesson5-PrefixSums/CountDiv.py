'''
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
'''

    
class Solution:
    def counting_divisibles(self,A,B,K):
        count_divisibles = 0
        left = A
        while left <= B:
            if left % K ==0:
                left = left + K
                count_divisibles +=1
            else:
                left += 1
        return count_divisibles 
    def counting_divisibles_optimized(self,A,B,K):
        divisbles_up_to_A_minus_1 = (A-1) // K
        divisbles_up_to_B = B // K
        return divisbles_up_to_B - divisbles_up_to_A_minus_1


def main():
    arr = [[0,1,0,1,1],
           [1,0,0,1,1]]

    for value in arr:
        print(f'There are {Solution().passing_cars(value)} pairs of passing cars')
        print(f'Optimized version: There are {Solution().passing_cars_optimized(value)} pairs of passing cars')



if __name__ == "__main__":
    main()