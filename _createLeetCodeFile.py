print("Question Name: ", end="")
questionName = input()

# Process the question name for the file name
fileNameParts = questionName.title().split()
fileNameParts[0] = fileNameParts[0][:-1]
fileName = "".join(fileNameParts)
fileName += ".py"

# Process the question name for the function name
functionNameParts = questionName.lower().split()[
    1:
]  # Remove the number and make lowercase
functionName = "".join(word.capitalize() for word in functionNameParts)
functionName = (
    functionName[0].lower() + functionName[1:]
)  # Make the first character lowercase

question = f"""class Solution(object):
    def {functionName}(self, nums, target):
        seen = {{}}
        for i in range(len(nums)):
            if(target - nums[i] in seen):
                return [seen[target-nums[i]], i]
            seen[nums[i]] = i

answer = Solution()
print(answer.{functionName}(PARAMS))
"""

f = open(fileName, "w")
f.write(question)
f.close()

print(f"File '{fileName}' has been created with function name '{functionName}'.")
