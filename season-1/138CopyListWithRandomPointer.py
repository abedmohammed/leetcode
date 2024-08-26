# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


def createList(array, randoms):
    head = Node(0)
    current = head

    for i, val in enumerate(array):
        node = Node(val)
        current.next = node
        current.random = randoms[i]
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
    def copyRandomList(self, head):
        mapping = {None: None}
        cur = head

        while cur:
            node = Node(cur.val)
            mapping[cur] = node
            cur = cur.next

        cur = head

        while cur:
            nodeCopy = mapping[cur]
            nodeCopy.next = mapping[cur.next]
            nodeCopy.random = mapping[cur.random]
            cur = cur.next

        return mapping[head]


answer = Solution()
l1 = createList([1, 2, 4, 6], [2, None, None, 2])
printList(answer.copyRandomList(l1))
