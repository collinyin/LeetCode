# Given a binary tree, find its maximum depth.

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def maxDepth(root: TreeNode) -> int:
    if root == None:
        return 0
    
    leftDepth = maxDepth(root.left)
    rightDepth = maxDepth(root.right)

    if leftDepth > rightDepth:
        return leftDepth + 1
    else:
        return rightDepth + 1
    