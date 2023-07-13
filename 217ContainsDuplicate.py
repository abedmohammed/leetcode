class Solution(object):
    def containsDuplicate(self, nums):
        unique = {}
        for num in nums:
            if(num in unique):
                return True
            unique[num] = 1
        return False
    
answer = Solution()
print(answer.containsDuplicate([9,6,4,2,5,7,0,1]))