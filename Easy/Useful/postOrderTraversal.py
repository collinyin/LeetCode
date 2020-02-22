# post order traversal of tree (left, right, root)
from typing import List
import TreeNode

def postOrder(root: TreeNode):
    if root != None:
        postOrder(root.left)
        postOrder(root.right)
        print(root.val)