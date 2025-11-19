"""
Given a string original and a string check, find the starting index of all substrings of original that is an anagram of check. The output must be sorted in ascending order.

Parameters
original: A string
check: A string
Result
A list of integers representing the starting indices of all anagrams of check.
Examples
Example 1
Input: original = "cbaebabacd", check = "abc"

Output: [0, 6]

Explanation: The substring from 0 to 2, "cba", is an anagram of "abc", and so is the substring from 6 to 8, "bac".

Example 2
Input: original = "abab", check = "ab"

Output: [0, 1, 2]

Explanation: All substrings with length 2 from "abab" are anagrams of "ab".

Constraints
1 <= len(original), len(check) <= 10^5
Each string consists of only lowercase characters in the standard English alphabet.
"""
from collections import Counter

def find_anagram(s: str, t: str) -> list[int]:
    if len(s) < len(t):
        return []
    n = len(s)
    m = len(t)
    char_count_t = Counter(t)
    positions = []
    for left in range(n-m+1):
        right = left + m
        partial_char_count_s = Counter(s[left:right])
        if partial_char_count_s == char_count_t:
            positions.append(left)
    return positions


def main():
    examples = [
        ("cbaebabacd", "cba"), # [0,6]
        ("abab", "ab"), # [0,1,2]

    ]

    for arr in examples:
        print(f"The anagram are in positions {find_anagram(arr[0],arr[1])}")
        print("-" * 60)

if __name__ == "__main__":
    main()
    
 




