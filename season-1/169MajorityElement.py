class Solution(object):
    def majorityElement(self, nums):
        candidate = ""
        count = 0
        for num in nums:
            if(candidate == ""):
                candidate = num
                count += 1
            elif(candidate == num):
                count += 1
            else:
                count -= 1
                
            if(count == 0):
                candidate = ""
        return candidate
            

answer = Solution()
print(answer.majorityElement([2,2,1,1,1,2,2]))