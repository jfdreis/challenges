"""Valid Palindrome
Determine whether a string is a palindrome, ignoring non-alphanumeric characters and case. Examples:

Input: Do geese see God? Output: True

Input: Was it a car or a cat I saw? Output: True

Input: A brown fox jumping over Output: False"""


def valid_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    # how do I check if a character is alphanumeric? I mean a letter or a number
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
    

def main():
    examples = [
        "Do geese see God?", # True
        "Was it a car or a cat I saw?", # True
        "A brown fox jumping over", # False
        "", # True
        "a", # True
        "aa", # True
    ]

    for arr in examples:
        print(f"The array after moving zeros to the end is {valid_palindrome(arr)}")
        print("-" * 30)

if __name__ == "__main__":
    main()