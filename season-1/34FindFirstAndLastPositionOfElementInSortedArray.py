class Solution(object):
    def searchRange(self, nums, target):
        # find leftest most 
        res = -1
        left = 0
        right = len(nums) - 1

        if(target < nums[left] or target > nums[right] or right <= 0):
            return [-1, -1]

        while(left <= right):
            # calculate middle
            middle = (right + left) // 2

            if(nums[middle] < target):
                # if middle is lower than target, move left to middle + 1
                left = middle + 1
            elif(nums[middle] == target):
                res = middle
                right = middle - 1
            else:
                # if middle is higher than target, move right to middle
                # if middle is target, move right to middle
                right = middle - 1

        most_left = res

        # find rightest most 
        res = -1
        left = 0
        right = len(nums) - 1
        while(left <= right):
            # calculate middle
            middle = (right + left) // 2

            if(nums[middle] > target):
                # if middle is higher than target, move right to middle - 1
                right = middle - 1
            elif(nums[middle] == target):
                res = middle
                left = middle + 1
            else:
                # if middle is lower than target, move left to middle
                left = middle + 1

        most_right = res

        return [most_left, most_right]


answer = Solution()
print(answer.searchRange([5,7,7,7,9,10], 8))

# Time: O(logN)
# Space: O(1)
