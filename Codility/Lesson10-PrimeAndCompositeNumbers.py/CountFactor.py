"""
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

class Solution { public int solution(int N); }
content_copy

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
"""
 
class Solution:
    def count_factors(self, N):
        i=1
        count=0
        while i*i < N:
            if N % i == 0:
                count+=2
            i+=1
        if i*i ==N:
            count+=1
        return count


def main():
    arr = [24]
    for value in arr:
        print(f'{value} has {Solution().count_factors(value)} divisors')

if __name__ == "__main__":
    main()