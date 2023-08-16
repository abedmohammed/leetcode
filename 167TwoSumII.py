class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        
        return -1
    
answer = Solution()
print(answer.twoSum([2, 7, 11, 15], 9))
print(answer.twoSum([2, 7, 11, 15], 18))
print(answer.twoSum([2, 3, 4], 6))
print(answer.twoSum([-1, 0], -1))

