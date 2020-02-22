# Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
# (ie, from left to right, level by level from leaf to root).

from typing import List
import TreeNode

def dfs(root: TreeNode, level: int, result: List[int]) -> None:
    if root:
        if len(result) < level + 1:
            result.insert(0, [])
        result[len(result) - 1 - level].append(root.val)
        dfs(root.left, level + 1, result)
        dfs(root.right, level + 1, result)

def levelTraversal(root: TreeNode) -> List[List[int]]:
    result = []
    dfs(root, 0,result)
    return result