# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth 
# of the two subtrees of every node never differ by more than 1.

# Given the sorted array: [-10,-3,0,5,9],
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

#       0
#      / \
#    -3   9
#    /   /
#  -10  5

from typing import List
from TreeNode import TreeNode

def convertToBST(nums: List[int]) -> TreeNode:
    # Using divide and conquer.
    # Since the array is sorted we can set the middle value as the root,
    # then we use all the values to the left of the middle value as a new sub array called, left.
    # Similarly, we can use all the values to the right as another sub array called, right.
    # We then build the trees for left and right by recursively calling this method.
    # Base case -> if length of nums < 1: return None (i.e. nums is an empty array)

    if len(nums) < 1:       # base case (i.e. conquer)
        return None
    
    # how we recursively get to the base case
    mid = len(nums)//2      # divide
    root = TreeNode(nums[mid])      # set root as mid value
    left = nums[0:mid]
    right = nums[mid+1:len(nums)]

    root.left = convertToBST(left)
    root.right = convertToBST(right)

    return root



