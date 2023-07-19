class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createList(array):
    head = ListNode(0)
    current = head
    
    for val in array:
        node = ListNode(val)
        current.next = node
        current = current.next
    
    return head.next

def printList(head):
    current = head
    string = ""
    while(current.next):
        string += str(current.val) + " -> "
        current = current.next
    string += str(current.val)
    print(string)

class Solution(object):
    def removeNthFromEnd(self, head, n):
        # current = head
        # count = 1

        # if not head.next: return None

        # while(current.next):
        #     current = current.next
        #     count += 1

        # current = head
        # fromStart = count - n

        # if(fromStart == 0):
        #     return head.next

        # count = 1

        # while(count <= fromStart):
        #     if(count == fromStart):
        #         current.next = current.next.next
        #     else:
        #       current = current.next
        #     count += 1
                
        # return head
        if not head.next: return None
        
        dummy = ListNode(0, head)
        current = dummy

        forward = head
        for i in range(n):
            forward = forward.next
        
        while(forward):
            forward = forward.next
            current = current.next

        current.next = current.next.next

        return dummy.next

answer = Solution()
printList(answer.removeNthFromEnd(createList([1, 2, 3, 4, 5, 6]), 6))
