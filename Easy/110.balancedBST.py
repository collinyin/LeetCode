# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# - a binary tree in which the left and right subtrees of every node 
#     differ in height by no more than 1.

# Example 1:

# Given the following tree [3,9,20,null,null,15,7]:

#     3
#    / \
#   9  20
#     /  \
#    15   7

from typing import List
from TreeNode import TreeNode

class Solution:
    def height(self, root: TreeNode) -> int:
        if root != None:
            leftTree = self.height(root.left) + 1
            rightTree = self.height(root.right) + 1
            if leftTree > rightTree:
                return leftTree
            return rightTree
        else:
            return 0
    
    def DFS(self, root: TreeNode, check: List[bool]):
        if root:
            left = self.height(root.left)
            right = self.height(root.right)
            if abs(left-right) > 1:
                check.append(False)
            else:
                self.DFS(root.left, check)
                self.DFS(root.right, check)
        check.append(True)
    
    def isBalanced(self, root: TreeNode) -> bool:
        check = []
        self.DFS(root, check)
        for c in check:
            if c == False:
                return False
        return True
        
        # Slightly faster solution

        # if root:
        #     left = self.height(root.left)
        #     right = self.height(root.right)
        #     return (abs(left-right) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)
        # else:
        #     return True

