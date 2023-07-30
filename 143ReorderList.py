# Definition for singly-linked list.
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
    while current.next:
        string += str(current.val) + " -> "
        current = current.next
    string += str(current.val)
    print(string)

class Solution(object):
    def reorderList(self, head):
        if not head.next: return head

        # Get length of list
        length = 0
        current = head
        while current.next:
            length += 1
            current = current.next

        # Find inflection point
        splitPoint = length // 2

        # Get head of second list 
        secondListHead = head
        count = 0
        while count < splitPoint:
            secondListHead = secondListHead.next
            count += 1

        # split lists
        prev = secondListHead
        secondListHead = secondListHead.next
        prev.next = None


        # Reverse second list
        newTail = secondListHead
        current = secondListHead.next
        newTail.next = None

        while current:
            temp = current.next
            current.next = newTail
            newTail = current
            current = temp

        # Merge both lists
        reversedHead = newTail

        currentReversed = reversedHead
        currentHead = head

        while currentReversed:
            temp = currentHead.next
            tempReversed = currentReversed.next
            currentHead.next = currentReversed
            currentReversed.next = temp

            currentHead = temp
            currentReversed = tempReversed


        return head




answer = Solution()
printList(answer.reorderList(createList([1, 2, 3])))