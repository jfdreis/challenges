"""
A string S consisting of N characters is called properly nested if:

S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000,000];
string S is made only of the characters '(' and/or ')'.
"""
 
class Solution:
    def brackets(self, S):
        open_parenteses =[]
        for ch in S:
            if ch == '(':
                open_parenteses.append('(')
            else:
                if open_parenteses == []:
                    return 0
                else:
                    open_parenteses.pop()
        if len(open_parenteses) > 0:
            return 0
        return 1


def main():
    arr = ['(()(())())','())']
    for value in arr:
        if Solution().brackets(value) == 1:
            print(f'The brackets in {value} are well placed')
        else:
            print(f'The brackets in {value} are NOT well placed')

if __name__ == "__main__":
    main()