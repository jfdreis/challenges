'''
AYou are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
'''

    
class Solution:
    def counter_usage(self,N,A):
        counter_usage = [0] * N
        max_value=0
        for value in A:
            if 1<= value <= N:
                counter_usage[value-1] += 1
            else:
                counter_usage = [max_value]*N
            max_value = max(counter_usage)
        return counter_usage
    def counter_usage_optimized(self,N,A):
        counter_usage = [0] * N
        current_max = 0
        last_max_used = 0
        for value in A:
            if 1<= value <= N:
                if counter_usage[value-1] < last_max_used:
                    counter_usage[value-1] = last_max_used
                counter_usage[value-1] += 1
                current_max = max(current_max, counter_usage[value-1])
            else:
                last_max_used = current_max
        for i in range(N):
            if counter_usage[i]< last_max_used:
                counter_usage[i] = last_max_used
        return counter_usage


def main():
    arr = [(5,[3,4,4,6,1,4,4])]

    for value in arr:
        print(f'The solution is {Solution().counter_usage_optimized(value[0],value[1])}')

if __name__ == "__main__":
    main()