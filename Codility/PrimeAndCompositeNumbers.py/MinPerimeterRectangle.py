'''
An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

(1, 30), with a perimeter of 62,
(2, 15), with a perimeter of 34,
(3, 10), with a perimeter of 26,
(5, 6), with a perimeter of 22.
Write a function:

def solution(N)

that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000,000].
'''

class Solution:
    def count_factors(self, N):
    #first step: get the divisor up to sqrt(N)
        i = 1
        divisors = []
        while i*i < N:
            if N % i == 0:
                divisors.append(i)
            i+=1
        if i*i==N:
            divisors.append(i)
        min_perimeter = 2 * (divisors[0] + N/divisors[0])
        
        l = len(divisors)
        for i in range(1,l):
            min_perimeter=min(min_perimeter,2 * (divisors[i] + N/divisors[i]))
        return int(min_perimeter)


def main():
    arr = [30]
    for value in arr:
        print(f'The rectangle with area {value} has {Solution().count_factors(value)} as the minimum possible perimeter')

if __name__ == "__main__":
    main()