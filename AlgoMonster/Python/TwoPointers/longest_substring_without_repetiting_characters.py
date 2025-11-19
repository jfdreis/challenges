"""
Find the length of the longest substring of a given string without repeating characters.

Input: abccabcabcc

Output: 3

Explanation: The longest substrings are abc and cab, both of length 3.

Input: aaaabaaa

Output: 2

Explanation: ab is the longest substring, with a length of 2.
"""

def longest_string_without_repeting_characters(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    max_length = 0
    last_index = {}
    left = 0 
    for right in range(n):
        char = s[right]
        if char in last_index:
            left = max(left, last_index[char] + 1)
            last_index[char] = right
        else:
            last_index[char] = right
        max_length = max(max_length, right - left + 1)
        
    return max_length



def main():
    examples = [
        "abccabcabcc",
        "aaaabaaa",
    ]
    for s in examples:
        print(f"The longest window has length {longest_string_without_repeting_characters(s)}")
        print("-" * 30)

if __name__ == "__main__":
    main()
