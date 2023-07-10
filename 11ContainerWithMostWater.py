# class Solution(object):
#     def maxArea(self, height):
#         area = 0
#         for i in range(len(height)):
#             for j in range(i + 1, len(height)):
#                 area = max(area, (j - i)*min(height[i], height[j]))
#         return area
        
class Solution(object):
    def maxArea(self, height):
        area = 0
        i = 0
        j = len(height) - 1
        while(i < j):
            area = max(area, (j - i) * min(height[i], height[j]))
            if(height[i] < height[j]):
                i += 1
            else:
                j -= 1
        return area


answer = Solution()
print(answer.maxArea([2,3,4,5,18,17,6]))

# Time: O(n)
# Space: O(1)

