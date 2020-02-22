# Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
# such that adding up all the values along the path equals the given sum.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

from TreeNode import TreeNode

def hasPathSum(root: TreeNode, sum: int) -> bool:
    if root:
        if root.left == None and root.right == None and sum - root.val == 0:
            return True
        
        return hasPathSum(root.left, sum - root.val) or hasPathSum(root.right, sum - root.val)
    else:
        return False