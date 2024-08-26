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
    def oddEvenList(self, head):
        oddDummy, evenDummy = ListNode(), ListNode()
        oddDummyHead, evenDummyHead, current = oddDummy, evenDummy, head

        count = 1

        while(current):
            if(count % 2 != 0):
                oddDummy.next = current
                oddDummy = oddDummy.next
            else:
                evenDummy.next = current
                evenDummy = evenDummy.next

            count += 1
            current = current.next

        evenDummy.next = None
        oddDummy.next = evenDummyHead.next 

        return oddDummyHead.next

answer = Solution()
printList(answer.oddEvenList(createList([1, 2, 3, 4, 5, 6, 7, 8])))
