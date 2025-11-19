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
    def find_leader(subarray):
        candidate = None
        count = 0
        n = len(subarray)
        #find a candidate
        for i in range(n):
            if count == 0:
                candidate = subarray[i]
                count += 1
            else:
                if subarray[i]!= candidate:
                    count -=1
                else:
                    count += 1
        count = 0
        for i in range(n):
            if subarray[i] == candidate:
                count +=1
        if (count <= n/2):
            return None
        return candidate  

    def find_equi_leader(self, A):
        equi_leaders = 0
        n = len(A)
        for i in range(n - 1):
            left = A[:i+1]
            right = A[i+1:]

            leader_left = Solution().find_leader(left)
            leader_right = Solution().find_leader(right)

            if leader_left is not None and leader_left == leader_right:
                equi_leaders += 1

        return equi_leaders
    def find_equi_leader_optimized(self, A):
        global_leader = Solution().find_leader(A)
        if global_leader == None:
            return 0
        count_leader = [0]
        n=len(A)
        #count the number of times the leader appear before entry i
        for i in range(n):
            if A[i] == global_leader:
                count_leader.append(count_leader[-1]+1)
            else:
                count_leader.append(count_leader[-1])
        equi_leaders = 0
        for i in range(n-1):
            # check if the leader appears on the left subarray more than half the length of A[:i+1] = i
            #and check if the leader appears on the right subarray more than half the length A[i+1:] = n-1-i of the right subarray
            if count_leader[i+1] > (i+1)/2 and count_leader[-1]-count_leader[i+1] > (n-1-i)/2:
                equi_leaders +=1

        return equi_leaders
    
    # We need to optimize the code above

def main():
    arr = [4,3,4,4,4,2]
    for value in arr:
        print(f'There are ')

if __name__ == "__main__":
    main()