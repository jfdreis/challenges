"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?

https://leetcode.com/problems/linked-list-cycle/description/
"""
from typing import Optional 


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        # Edge case: empty list
        if not head:
            return False

        # Initialize two pointers, slow and fast
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False



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


def make_cycle(head: Optional[ListNode], pos: int) -> Optional[ListNode]:
    if not head or pos < 0:
        return head
    # Find the node at position `pos`
    cycle_node = head
    index = 0
    while index < pos and cycle_node:
        cycle_node = cycle_node.next
        index += 1

    if not cycle_node:
        return head

    # Find the last node
    tail = head
    while tail.next:
        tail = tail.next

    # Create the cycle
    tail.next = cycle_node
    return head


def main():
    examples = [
        ([3,2,0,-4], 1),  # cycle connecting tail to node at index 1
        ([1,2], 0),       # cycle connecting tail to node at index 0
        ([1], -1),        # no cycle
        ([], -1),         # empty list
    ]

    solution = Solution()

    for arr, pos in examples:
        head = build_linked_list(arr)
        head = make_cycle(head, pos)
        result = solution.has_cycle(head)
        print("Input:", arr, "Cycle pos:", pos)
        print("Has cycle:", result)
        print("-" * 30)


if __name__ == "__main__":
    main()


