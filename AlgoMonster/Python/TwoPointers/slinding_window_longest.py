"""sliding window – longest

given a string s and an integer k, find the length of the longest substring that contains at most k distinct characters.

parameters

s: a string

k: an integer

result

an integer representing the length of the longest substring with at most k distinct characters.

examples

input:

s = "eceba", k = 2


output:

3


explanation: the substring "ece" has 2 distinct characters and is the longest.

input:

s = "aa", k = 1


output:

2


explanation: the substring "aa" has 1 distinct character and is the longest.

constraints

1 <= len(s) <= 10^5

s consists of lowercase letters only

1 <= k <= 26

https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
"""


def longest_string(s: str,k: int) -> int:
    n = len(s)
    if n == 0:
        return 0
    max_length = 0
    char_count = {}
    left = 0 
    for right in range(n):
        char = s[right]
        char_count[char] = char_count.get(char,0) + 1
        while len(char_count) > k:
            c = s[left]
            char_count[c]-=1
            if char_count[c] == 0:
                del char_count[c]
            left += 1 

        max_length = max(max_length, right - left + 1)
        
    return max_length



def main():
    examples = [
        ("eceba", 2),
        ("aa", 1),
    ]
    for arr in examples:
        print(f"The longest window has length {longest_string(arr[0],arr[1])}")
        print("-" * 30)

if __name__ == "__main__":
    main()