"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
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

def constructTree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        split_at = inorder.index(root_val)

        left_inorder = inorder[:split_at]
        right_inorder = inorder[split_at + 1:]

        left_preorder = preorder[1:1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder):]

        root.left = constructTree(left_preorder, left_inorder)
        root.right = constructTree(right_preorder, right_inorder)

        return root




def main():
    examples = [ # (preorder, inorder, levelorder)
        ([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7],[1, 2, 3, 4, 5, 6, 7]),                     # true
    ]

    for arr in examples:
        expected = build_tree(arr[2])
        ans = constructTree(arr[0],arr[1])
        print(f"The construction was well made? {equal_trees(expected,ans)}")
        print("-" * 30)


if __name__ == "__main__":
    main()