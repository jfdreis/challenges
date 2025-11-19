"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104

https://leetcode.com/problems/subtree-of-another-tree/
"""

from collections import deque
from typing import Optional, Tuple

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

def equal_trees(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if root is None and subRoot is None:
        return True
    if root and subRoot and root.val == subRoot.val:
        left_equal = equal_trees(root.left, subRoot.left)
        right_equal = equal_trees(root.right, subRoot.right)
        return left_equal and right_equal
    return False

def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if subRoot is None:
        return True
    if root is None:
        return False
    if equal_trees(root, subRoot):
        return True
    left_subtree = isSubtree(root.left, subRoot)
    right_subtree = isSubtree(root.right, subRoot)
    return left_subtree or right_subtree



def main():
    examples = [
        ([3,4,5,1,2], [4,1,2]),                       # true
        ([3,4,5,1,2,None,None,None,None,0],[4,1,2])   # false
    ]

    for arr in examples:
        root = build_tree(arr[0])
        subroot = build_tree(arr[1])
        ans = isSubtree(root,subroot)
        print("Input:", arr, ". subtree:", ans)
        print("-" * 30)


if __name__ == "__main__":
    main()