"""
A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbors. More precisely, it is an index P such that 0 < P < N − 1,  A[P − 1] < A[P] and A[P] > A[P + 1].

For example, the following array A:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
has exactly three peaks: 3, 5, 10.

We want to divide this array into blocks containing the same number of elements. More precisely, we want to choose a number K that will yield the following blocks:

A[0], A[1], ..., A[K − 1],
A[K], A[K + 1], ..., A[2K − 1],
...
A[N − K], A[N − K + 1], ..., A[N − 1].
What's more, every block should contain at least one peak. Notice that extreme elements of the blocks (for example A[K − 1] or A[K]) can also be peaks, but only if they have both neighbors (including one in an adjacent blocks).

The goal is to find the maximum number of blocks into which the array A can be divided.

Array A can be divided into blocks as follows:

one block (1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2). This block contains three peaks.
two blocks (1, 2, 3, 4, 3, 4) and (1, 2, 3, 4, 6, 2). Every block has a peak.
three blocks (1, 2, 3, 4), (3, 4, 1, 2), (3, 4, 6, 2). Every block has a peak. Notice in particular that the first block (1, 2, 3, 4) has a peak at A[3], because A[2] < A[3] > A[4], even though A[4] is in the adjacent block.
However, array A cannot be divided into four blocks, (1, 2, 3), (4, 3, 4), (1, 2, 3) and (4, 6, 2), because the (1, 2, 3) blocks do not contain a peak. Notice in particular that the (4, 3, 4) block contains two peaks: A[3] and A[5].

The maximum number of blocks that array A can be divided into is three.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximum number of blocks into which A can be divided.

If A cannot be divided into some number of blocks, the function should return 0.

For example, given:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000].
"""
 
class Solution:
    # Implement your solution here
    #find peaks
    def find_peaks(self,A):
        n = len(A)
        peaks=[]
        for i in range(1,n-1):
            if A[i-1]< A[i] and A[i] > A[i+1]:
                peaks.append(i)
        return peaks
    
    #find divisors (the blocks have the same lenghts)
    def find_divisors(self,N):
        divisors = [] 
        divisors_right = [] 
        i=1
        while i * i < N:
            if N % i ==0:
                divisors.append(i)
                divisors_right.append(N//i)
            i+=1
        if i * i == N:
            divisors.append(i)
        m = len(divisors_right)
        for i in range(m-1,-1,-1):
            divisors.append(divisors_right[i])
        return divisors
    
    #aux function that return true if we have a peak in each block
    def aux_f(self,peaks,num_blocks,n):
        if n%num_blocks !=0 or len(peaks)< num_blocks:
            return False        
        has_peaks=[False] * num_blocks
        block_size = n //num_blocks
        for p in peaks:
            block_num_p = p // block_size
            if block_num_p < num_blocks:
                   has_peaks[block_num_p]=True
        return all(has_peaks)
    
    def max_num_block(self,A):
        n = len(A)
        if n < 3:
            return 0

        peaks = Solution().find_peaks(A)
        if not peaks:
            return 0

        divisors = Solution().find_divisors(n)
        for d in reversed(divisors):  # check largest first
            if Solution().aux_f(peaks, d, n):
                return d
        return 0

def main():
    arr = [[1,2,3,4,3,4,1,2,3,4,6,2]]
    for value in arr:
        print(f'One divide in {Solution().max_num_block(value)} blocks with all block having a peak')

if __name__ == "__main__":
    main()