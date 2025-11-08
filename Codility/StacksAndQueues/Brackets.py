"""
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S is made only of the following characters: '(', '{', '[', ']', '}' and/or ')'.
"""
 
class Solution:
    def brackets(self, S):
        T = ''
        for i in S:
            # if it opening, we can added it to the string T
            # print(f'Begining of the iteration: For caracter {i} we have {T}')
            if i in ('(', '{', '['):
                T = T + i
            # it is closing, so it must be the opposite of the last caractes in T
            elif T == '':
                return 0
            elif (T[-1], i) in {('(', ')'), ('[', ']'), ('{', '}')}:
                T = T[:-1] # we can delete the last element of T
            else:
                return 0
            # print(f'end of iteration For caracter {i} we have {T}')
        if T == '':
            return 1
        return 0
    
    def brackets_optimized(S):
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for ch in S:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return 0
                stack.pop()

        return 1 if not stack else 0


def main():
    arr = ['{[()()]}','([)()]']
    for value in arr:
        if Solution().brackets(value) == 1:
            print(f'The brackets in {value} are well placed')
        else:
            print(f'The brackets in {value} are NOT well placed')

if __name__ == "__main__":
    main()