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



def isValidBST(root: Optional[TreeNode]) -> bool:
    if root is None:
        return True
    root_value = root.val
    max_value = float('inf')   # positive infinity
    min_value = float('-inf')  # negative infinity
    def dfs(root: Optional[TreeNode],min_value: int, max_value: int) -> bool:
        if root is None:
            return True
        if root.val >= max_value:
            return False
        if root.val <= min_value:
            return False
        left = dfs(root.left, min_value, root.val)
        right = dfs(root.right, root.val, max_value)
        return left and right
    
    left = dfs(root.left, min_value, root.val)
    right = dfs(root.right, root.val , max_value)
    
    return left and right



def main():
    examples = [ 
        [2,1,3], # true
        [5,1,4,None,None,3,6], # false
        [5,4,6,None,None,3,7], # false
    ]

    for arr in examples:
        root = build_tree(arr)
        ans = isValidBST(root)
        print(f"The binary tree is valid for binary search?\n {ans}")
        print("-" * 30)


if __name__ == "__main__":
    main()

