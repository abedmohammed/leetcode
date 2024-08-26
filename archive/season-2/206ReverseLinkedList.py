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
    if not head:
        return
    current = head
    string = ""
    while current.next:
        string += str(current.val) + " -> "
        current = current.next
    string += str(current.val)
    print(string)


class Solution(object):
    def reverseList(self, head):
        current = head
        dummy = ListNode()

        while current != None:
            temp = dummy.next
            dummy.next = current
            nextNode = current.next
            current.next = temp
            current = nextNode

        return dummy.next

    def reverseListBetter(self, head):
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def reverseListNew(self, head):
        current = head
        dummy = ListNode()

        while current != None:
            temp = dummy.next
            dummy.next = ListNode(current.val, temp)
            current = current.next

        return dummy.next

    def reverseListRecursive(self, head):
        if not head:
            return None

        def recurs(current):
            if not current.next:
                return (current, current)

            tail, head = recurs(current.next)
            tail.next = current
            current.next = None

            return (current, head)

        return recurs(head)[1]


answer = Solution()
list = createList([9, 6, 4, 2, 3, 5, 7, 0, 1])
printList(answer.reverseListBetter(list))
