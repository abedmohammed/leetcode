# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        # O(N) space
        # current = head
        # seen = {}

        # while(current):
        #     if(current in seen):
        #         return True
        #     else:
        #         seen[current] = 1
        #     current = current.next

        # return False

        #O(1) 
        # current = head
        # trash = ListNode("aint no way")

        # while(current):
        #     if(current.next == trash):
        #         return True
        #     else:
        #         dummy = current
        #         current = current.next
        #         dummy.next = trash
        #     current = current.next
        # return False
    
        #tortoise O(N)
        tortoise = head
        hare = head
        trash = ListNode("aint no way")


        while(tortoise.next):
            if(tortoise.next == trash):
                return True
            elif(tortoise.next is None):
                return False
            else:
                tortoise = tortoise.next.next
                temp = hare
                hare = hare.next
                temp.next = trash

        return False

answer = Solution()
print(answer.hasCycle([3,2,0,-4]))