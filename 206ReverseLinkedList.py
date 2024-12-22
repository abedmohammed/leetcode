# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if not head:
            return

        prevNode, curNode = None, head

        while curNode:
            tempNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = tempNode

        return prevNode
