"""
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

content_copy
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

def solution(A)
content_copy

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

content_copy
the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
"""
 
class Solution:
    def dominator(self, A):
        candidate = []
        n = len(A)
        for i in range(n):
            if candidate == []:
                candidate.append(A[i])
            else:
                if A[i]!= candidate[-1]:
                    candidate.pop()
                else:
                    candidate.append(A[i])
        count = 0
        index = -1
        for i in range(n):
            if A[i]==candidate[0]:
                index = i
                count +=1
        return index if (count > n/2) else -1
    
    # do similar to previous one, but avoid  storing stuff
    
    def dominator_optimized(A):
        candidate = None
        count = 0
        n = len(A)
        #find a candidate
        for i in range(n):
            if count == 0:
                candidate = A[i]
                count += 1
            else:
                if A[i]!= candidate:
                    count -=1
                else:
                    count += 1
        count = 0
        for i in range(n):
            if A[i] == candidate:
                count +=1
        if (count <= n/2):
            return -1
        for i in range(n):
            if A[i] == candidate:
                return i
        return -1

def main():
    arr = [3,4,3,2,3,-1,3,3]
    for value in arr:
        if Solution().dominator(value) != -1:
            print(f'The dominator is in index {Solution().dominator(value)} of the array {value}.')
        else:
            print(f'There is no dominator in {value}.')

if __name__ == "__main__":
    main()