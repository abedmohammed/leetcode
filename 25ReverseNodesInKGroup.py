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
    def reverseKGroup(self, head, k):
        nodesCheck = head
        store = ListNode()

        first, newHead = True, None

        while nodesCheck:
            start = nodesCheck

            for i in range(k - 1):
                if not nodesCheck.next:
                    store.next = start
                    return newHead
                nodesCheck = nodesCheck.next

            store.next = nodesCheck
            nodesCheck = nodesCheck.next
            store = start

            # reverse list starting at start ending before nodesCheck
            previous = None
            current = start
            while current and current != nodesCheck:
                temp = current.next
                current.next = previous
                previous = current
                current = temp

            if first:
                first = False
                newHead = previous

        return newHead


answer = Solution()
printList(answer.reverseKGroup(createList([1, 2, 3, 4, 5]), 2))
printList(answer.reverseKGroup(createList([1, 2, 3, 4, 5]), 3))
