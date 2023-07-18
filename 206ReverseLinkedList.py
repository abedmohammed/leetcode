# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        # tail = head
        
        # if not head or not head.next: return head

        # head = head.next
        # tail.next = None

        # while(head):
        #     next = head.next
        #     head.next = tail
        #     tail = head
        #     head = next

        # return tail

        if not head: return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return newHead

        

answer = Solution()
print(answer.reverseList([9,6,4,2,3,5,7,0,1]))