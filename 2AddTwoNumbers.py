# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# LIST HELPERS
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
    def addTwoNumbers(self, l1, l2):
        # number1 = 0
        # count = 1
        # while(l1):
        #     number1 += l1.val*count
        #     count *= 10
        #     l1 = l1.next

        # number2 = 0
        # count = 1
        # while(l2):
        #     number2 += l2.val*count
        #     count *= 10
        #     l2 = l2.next

        # left = number1 + number2

        # if left == 0: return ListNode[0]

        # head = ListNode()
        # current = head
        # while(left != 0):
        #     remainder = left % 10
        #     current.next = ListNode(remainder)
        #     current = current.next
        #     left = (left - remainder)/ 10

        # return head.next

        carry = 0
        head = ListNode()
        current = head
        while(l1 or l2):
            sum = 0
            if(l1 and l2):
                sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif(l1 and not l2):
                sum = l1.val + carry
                l1 = l1.next
            elif(l2 and not l1):
                sum = l2.val + carry
                l2 = l2.next

            value = sum%10
            carry = sum//10

            current.next = ListNode(value)
            current = current.next
            printList(head.next)


        if carry != 0: current.next = ListNode(1)
        
        return head.next


l1 = createList([9,9,9,9,9,9,9])
l2 = createList([9,9,9,9])
answer = Solution()
head = answer.addTwoNumbers(l1, l2)
printList(head)
        