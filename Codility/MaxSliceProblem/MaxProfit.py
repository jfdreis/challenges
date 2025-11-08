"""
An array A consisting of N integers is given. It contains daily prices of a stock share for a period of N consecutive days. If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such transaction is equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].

For example, consider the following array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because A[2] − A[0] = 21123 − 23171 = −2048. If a share was bought on day 4 and sold on day 5, a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354. Maximum possible profit was 356. It would occur if a share was bought on day 1 and sold on day 5.

Write a function,

def solution(A)

that, given an array A consisting of N integers containing daily prices of a stock share for a period of N consecutive days, returns the maximum possible profit from one transaction during this period. The function should return 0 if it was impossible to gain any profit.

For example, given array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
the function should return 356, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..400,000];
each element of array A is an integer within the range [0..200,000].
"""
 
class Solution:
    def profit(self, A):
        n = len(A)
        if n ==1:
            return 0
        min_price_so_far = A[0]
        max_profit = 0
        for i in range(n):
            todays_profit = A[i] - min_price_so_far
            if A[i] < min_price_so_far:
                min_price_so_far = A[i]
            if todays_profit > max_profit:
                max_profit = todays_profit
        
        return max_profit
    def profit_optimized(self, A):
        n = len(A)
        if n ==1:
            return 0
        min_price_so_far = A[0]
        max_profit = 0
        for i in range(n):
            if A[i] < min_price_so_far:
                min_price_so_far = A[i]
            elif A[i] - min_price_so_far > max_profit:
                max_profit = A[i] - min_price_so_far
        
        return max_profit

def main():
    arr = [[23171,21011,21123,21366,21013,21367]]
    for value in arr:
        print(f'The maximum profit is {Solution().profit_optimized(value)}')

if __name__ == "__main__":
    main()