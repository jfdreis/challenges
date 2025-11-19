"""
Minimum Consecutive Cards to Pick Up

You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.



Example 1:

Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.
Example 2:

Input: cards = [1,0,5,3]
Output: -1
Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.
 

Constraints:

1 <= cards.length <= 105
0 <= cards[i] <= 106


"""



from collections import Counter

def repeated_cards(a: Counter) -> bool:
    """Return True if there every element in 'a' has count >= 2."""
    return any( v > 1 for _, v in a.items())

def shortest_substring(arr: list[int]) -> str:
    n = len(arr)
    ans = n+1
    if n<=1:
        return -1
    left = 0
    count_cards_window = Counter()
    for right in range(n):
        count_cards_window[arr[right]] += 1
        #while there are cards counted multiple times, try to shrink the window
        while repeated_cards(count_cards_window):
            current_len = right - left + 1
            if current_len < ans:
                ans = current_len
            if current_len ==2:
                return 2
            count_cards_window[arr[left]] -= 1
            if count_cards_window[arr[left]] == 0:
                del count_cards_window[arr[left]]
            left += 1    
    return -1 if ans==n+1 else ans

def shortest_substring_optimized(arr: list[int]) -> str:
    last_seen = {}
    min_len = float('inf')

    for i, x in enumerate(arr):
        if x in last_seen:
            current_len = i - last_seen[x] + 1
            min_len = min(current_len, min_len)
        last_seen[x] = i
    return -1 if min_len==float('inf') else min_len




def main():
    examples = [
        [3,4,2,3,4,7], 
        [1,0,5,3], 

    ]

    for arr in examples:
        print(f"The shortest str is:\n {shortest_substring_optimized(arr)}")
        print("-" * 60)

if __name__ == "__main__":
    main()