###############################
# TREES
###############################
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = TreeNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = TreeNode(val)


tree = TreeNode(6)
tree.insert(2)
tree.insert(8)
tree.insert(0)
tree.insert(4)
tree.insert(7)
tree.insert(9)
tree.insert(3)
tree.insert(5)

answer = Solution()
answer.inOrder(tree)


###############################
# LINKED LISTS
###############################
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


answer = Solution()
l1 = createList([5, 6, 4])
l2 = createList([1, 4, 7])
printList(answer.addTwoNumbers(l1, l2))

###############################
# PRINT SOLUTIONs
###############################

answer = Solution()
print(answer.LEETCODEQUESTION())
