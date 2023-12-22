questionName = "1422. Maximum Score after Splitting a String"

questionName = questionName.title().split()
questionName[0] = questionName[0][:-1]
questionName = "".join(questionName)
questionName += ".py"

question = """class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            if(target - nums[i] in seen):
                return [seen[target-nums[i]], i]
            seen[nums[i]] = i

answer = Solution()
print(answer.QUESTION(PARAMS))
"""

f = open(questionName, "w")
f.write(question)
f.close()
