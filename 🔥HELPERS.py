############################### 
# LINKED LISTS
############################### 
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


answer = Solution()
l1 = createList([5, 6, 4])
l2 = createList([1, 4, 7])
printList(answer.addTwoNumbers(l1, l2))
        
############################### 
# PRINT SOLUTIONs
############################### 

answer = Solution()
print(answer.LEETCODEQUESTION())