"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
"""

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root



def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    left_max_val = maxDepth(root.left)
    right_max_val = maxDepth(root.right)
    return max(left_max_val, right_max_val)+1
    

def main():
    examples = [
        [3, 9, 20, None, None, 15, 7],  # depth = 3
        [1, 2],                         # depth = 2
        [1],                            # depth = 1
        [None]                          # depth = 0
    ]

    for arr in examples:
        root = build_tree(arr)
        depth = maxDepth(root)
        print("Input:", arr, ". Depth:", depth)
        print("-" * 30)


if __name__ == "__main__":
    main()


