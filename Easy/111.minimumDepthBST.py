# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest 
# path from the root node down to the nearest leaf node.

from TreeNode import TreeNode

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root:
            leftTree = self.minDepth(root.left) + 1
            rightTree = self.minDepth(root.right) + 1
            if leftTree == 1 and rightTree > leftTree:
                return rightTree
            elif rightTree == 1 and leftTree > rightTree:
                return leftTree
            else:
                if leftTree > rightTree:
                    return rightTree
                return leftTree
            
        else:
            return 0