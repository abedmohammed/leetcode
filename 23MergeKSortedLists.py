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
    if not current: return "EMPTY"
    while(current.next):
        string += str(current.val) + " -> "
        current = current.next
    string += str(current.val)
    print(string)

class Solution(object):
    def mergeKLists(self, lists):
        if len(lists) == 0: return None

        while(len(lists) > 1):
            newLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                newLists.append(self.mergeTwoLists(l1, l2))
            lists = newLists

        return lists[0]

    def mergeTwoLists(self, l1, l2):
        head = ListNode()
        current = head

        while(l1 and l2):
            if(l1.val < l2.val):
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 or l2

        return head.next

answer = Solution()
l1 = createList([0, 4, 5])
l2 = createList([1, 3, 4])
l3 = createList([2, 6])
l4 = createList([2])
printList(answer.mergeKLists([[]]))
