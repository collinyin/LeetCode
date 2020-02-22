# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
from typing import List

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

def postOrder(root: TreeNode, treeList: List[TreeNode]) -> None:
    if root == None:
        treeList.append(None)
    else:
        postOrder(root.left, treeList)
        postOrder(root.right, treeList)
        treeList.append(root.val)
    
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    pList = []
    qList = []

    postOrder(p, pList)
    postOrder(q, qList)

    if (pList != qList):
        return False
    
    return True