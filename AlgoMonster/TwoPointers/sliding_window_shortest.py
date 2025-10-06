"""
Given two strings, original and check, return the minimum substring of original such that each character in check, including duplicates, are included in this substring. By "minimum", I mean the shortest substring. If two substrings that satisfy the condition have the same length, the one that comes lexicographically first is smaller.

Parameters
original: The original string.
check: The string to check if a window contains it.
Result
The smallest substring of original that satisfies the condition.
Examples
Example 1
Input: original = "cdbaebaecd", check = "abc"

Output: baec

Explanation: baec is the shortest substring of original that contains all of a, b, and c.

Constraints
1 <= len(check), len(original) <= 10^5
original and check both contain only uppercase and lowercase characters in English. The characters are case sensitive.

https://leetcode.com/problems/minimum-window-substring/description/
"""

from collections import Counter

def is_counter_contained(a: Counter, b: Counter) -> bool:
    """Return True if every element in a has count <= in b."""
    return all(b[k] >= v for k, v in a.items())


def shortest_substring(s: str, t: str) -> str:
    n = len(s)
    m = len(t)
    char_count_t = Counter(t)
    if is_counter_contained(char_count_t, Counter(s))==False:
        return ""
    ans = s
    min_len = n
    left = 0
    char_count_window = Counter()
    for right in range(n):
        char_count_window[s[right]] += 1
        # while current window contains all required chars, try to shrink
        while is_counter_contained(char_count_t,char_count_window):
            current_len = right - left + 1
            current_window = s[left:right+1]
            # update answer if shorter
            if current_len < min_len:
                ans = current_window
                min_len = current_len
            char_count_window[s[left]] -= 1
            if char_count_window[s[left]] == 0:
                del char_count_window[s[left]]
            left += 1
    return ans


def main():
    examples = [
        ("ADOBECODEBANC", "ABC"), 
        ("ab", "a"), 

    ]

    for arr in examples:
        print(f"The shortest str is:\n {shortest_substring(arr[0],arr[1])}")
        print("-" * 60)

if __name__ == "__main__":
    main()
    
 

        #  while is_counter_contained(char_count_t, char_count_window):
        #     if right - left + 1 < len(ans):
        #         ans = s[left:right+1]
        #     char_count_window[s[left]] -= 1
        #     if char_count_window[s[left]] == 0:
        #         del char_count_window[s[left]]
        #     left += 1





