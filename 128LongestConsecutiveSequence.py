# class Node(object):
#     def __init__(self):
#         self.prev = None
#         self.next = None


class Solution(object):
    def longestConsecutive(self, nums):
        # Smashing brain on keyboard answer
        # linkedHash = {}

        # for num in nums:
        #     if num in linkedHash:
        #         continue

        #     # add new element, find next and previous
        #     newNode = Node()

        #     if num - 1 in linkedHash:
        #         newNode.prev = num - 1
        #         linkedHash[num-1].next = num

        #     if num + 1 in linkedHash:
        #         newNode.next = num + 1
        #         linkedHash[num+1].prev = num

        #     linkedHash[num] = newNode

        # maxLength = 0

        # for num, node in linkedHash.items():
        #     if(node.prev != None):
        #         continue

        #     curLength = 1
        #     curNode = node
        #     while curNode.next != None:
        #         curNode = linkedHash[curNode.next]
        #         curLength += 1

        #     maxLength = max(curLength, maxLength)

        # return maxLength

        numSet = set(nums)
        maxLength = 0

        for number in numSet:
            if number - 1 in numSet:
                continue

            curLength = 1
            curNum = number
            while curNum + 1 in numSet:
                curLength += 1
                curNum += 1

            maxLength = max(curLength, maxLength)

        return maxLength
