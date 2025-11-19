"""
Find the middle node of a linked list.

Input: 0 1 2 3 4

Output: 2

If the number of nodes is even, then return the second middle node.

Input: 0 1 2 3 4 5

Output: 3
"""
from typing import Optional 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: empty list
        if not head:
            return None

        # Initialize two pointers, slow and fast
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
# Helper to build a linked list from a Python list
def build_linked_list(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for i in range(1, len(values)):
        curr.next = ListNode(values[i])
        curr = curr.next
    return head

def main():
    examples = [
        [0, 1, 2, 3, 4],      # odd length -> middle is 2
        [0, 1, 2, 3, 4, 5],   # even length -> second middle is 3
        [],                   # empty list
        [1],                  # single element
    ]

    for arr in examples:
        head = build_linked_list(arr)
        mid = Solution().middleNode(head)
        print("Input:", arr)
        if mid:
            print("Middle node value:", mid.val)
        else:
            print("Middle node: None (empty list)")
        print("-" * 30)


if __name__ == "__main__":
    main()