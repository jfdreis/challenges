"""Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

https://leetcode.com/problems/invert-binary-tree/description/
"""


from collections import deque
from typing import Optional, Tuple

from subtree import equal_trees

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
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

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return root
    root.left , root.right = root.right , root.left 
    root.left = invertTree(root.left)
    root.right = invertTree(root.right)
    return root



def main():
    examples = [ # (input, expected output)
        ([4,2,7,1,3,6,9], [4,7,2,9,6,3,1]),
        ([2,1,3],[2,3,1]),
        ([1,2], [1,None,2]),
        ([],[])
    ]

    for arr in examples:
        root = build_tree(arr[0])
        expected = build_tree(arr[1])
        ans = invertTree(root)
        print(f"The inversion was well made? {equal_trees(expected,ans)}")
        print("-" * 30)


if __name__ == "__main__":
    main()

