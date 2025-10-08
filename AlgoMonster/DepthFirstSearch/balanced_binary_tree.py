"""
A binary tree is considered balanced if, for every node in the tree, the difference in the height (or depth) of its left and right subtrees is at most 1.

In other words, the depth of the two subtrees for every node in the tree differs by no more than one.

The height (or depth) of a tree is defined as the number of edges on the longest path from the root node to any leaf node.

Note: An empty tree is considered balanced by definition.

In that case, given a binary tree, determine if it is balanced.

Parameter
tree: A binary tree.
Result
A boolean representing whether the tree given is balanced.
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

def depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    left_max_val = depth(root.left)
    right_max_val = depth(root.right)
    return max(left_max_val, right_max_val)+1

def balanced_binary_tree(root: Optional[TreeNode]) -> int:
    if root is None:
        return True
    left_depth = depth(root.left)
    right_depth = depth(root.right)

    if abs(left_depth - right_depth) > 1:
        return False
    
    if not balanced_binary_tree(root.left):
        return False
    if not balanced_binary_tree(root.right):
        return False
    return True

def balanced_binary_tree_efficient(root: Optional[TreeNode]) -> int:
    def check(node: Optional[TreeNode]) -> Tuple[int, bool]:
        if node is None:
            return (0, True)
        left_height, left_balanced = check(node.left)
        right_height, right_balanced = check(node.right)

        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        height = max(left_height, right_height) + 1

        return height, balanced
    
    _, is_balanced = check(root)

    return is_balanced

    
    

def main():
    examples = [
        [3,9,20,None,None,15,7],              # True
        [1,2,2,3,3,None,None,4,4],            # False
        [0],                                  # True
        [1,2,2,3,None,None,3,4,None,None,4]  # False
    ]

    for arr in examples:
        root = build_tree(arr)
        depth = balanced_binary_tree_efficient(root)
        print("Input:", arr, ". Balanced?", depth)
        print("-" * 30)


if __name__ == "__main__":
    main()


