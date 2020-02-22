# Given a sorted linked list, delete all duplicates such that each element appear only once.

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        # Base case
        if (head == None):
            return head
        
        nodePtr = head
        prevNode = head
        while nodePtr.next != None:
            nodePtr = nodePtr.next
            if (prevNode.val == nodePtr.val):
                prevNode.next = nodePtr.next
            else:
                prevNode = nodePtr
    
        return head

def main():
    # Created a linked list (1 -> 1 -> 2)
    head = ListNode(1)
    next = ListNode(1)
    nextNext = ListNode(2)
    head.next = next
    next.next = nextNext

    nodePtr = head
    i = 0
    while i < 3:
        print(str(nodePtr.val), str(nodePtr.next))
        nodePtr = nodePtr.next
        i += 1

    solution = Solution()
    solution.deleteDuplicates(head)
    
    print()
    nodePtr = head
    i = 0
    while i < 3:
        if (nodePtr == None):
            break
        print(str(nodePtr.val), str(nodePtr.next))
        nodePtr = nodePtr.next
        i += 1

if __name__ == "__main__":
    main()