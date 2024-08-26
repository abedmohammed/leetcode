class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        totalWater = 0

        while left < right:
            water = 0
            if maxRight < maxLeft:
                right -= 1
                water = maxRight - height[right]
                maxRight = max(height[right], maxRight)
            else:
                left += 1
                water = maxLeft - height[left]
                maxLeft = max(height[left], maxLeft)

            totalWater += water if water > 0 else 0
        
        return totalWater



answer = Solution()
print(answer.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(answer.trap([4,2,0,3,2,5]))
print(answer.trap([4,2,3]))

