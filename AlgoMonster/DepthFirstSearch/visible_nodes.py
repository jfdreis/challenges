"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:



Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:



Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].

https://leetcode.com/problems/count-good-nodes-in-binary-tree/
"""


from collections import deque
from typing import Optional

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



def visible_nodes(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    max_value = root.val
    def dfs(node: TreeNode, floor_value: int) -> int:
        if node is None:
            return 0
        count = 0
        if node.val >= floor_value:
            count += 1
            floor_value = node.val
        count_left = dfs(node.left,floor_value)
        count_right= dfs(node.right,floor_value)
        return count + count_left + count_right     
    return dfs(root,max_value)
    

def main():
    examples = [
        [3, 1, 4, 3, None, 1, 5],              # count = 4
        [3, 3, None, 4, 2],                    # count = 3
        [1],                                   # count = 1
        [2, None, 4, 10, 8, None, None, 4],    # count = 
        [None]                                 # count = 4
    ]

    for arr in examples:
        root = build_tree(arr)
        depth = visible_nodes(root)
        print("Input:", arr, ". Depth:", depth)
        print("-" * 30)


if __name__ == "__main__":
    main()


