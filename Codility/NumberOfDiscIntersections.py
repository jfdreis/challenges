'''
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0


There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].
'''

    
class Solution:
    def num_intersections(self,A):
        left = []
        right = []
        n=len(A)
        for i in range(n):
            left.append(i-A[i])
            right.append(i+A[i])
        left.sort()
        right.sort()

        open_discs = 0
        num_intersections = 0
        j=0 # pointer

        for i in range(n):  
            # process discs in order of starting points
            #we are at left[i] we need to close all disc that 
            while j<n and right[j] < left[i]:
                open_discs -= 1
                j+=1 # to check the next point where a disc gets closed

            num_intersections += open_discs
            if num_intersections > 10_000_000:
                return -1
            open_discs+=1

        return num_intersections

def main():
    arr = [[1,5,2,1,4,0]]

    for value in arr:
        print(f'The number of disc intersection in {value} is {Solution().num_intersections(value)}')

if __name__ == "__main__":
    main()