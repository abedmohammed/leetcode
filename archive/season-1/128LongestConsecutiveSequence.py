class Solution(object):
    def longestConsecutive(self, nums):
        # if not nums: return 0

        # nums = sorted(nums)

        # longest, current = 1, 1
        # last = nums[0]
        # for num in nums:
        #     if num == last + 1:
        #         current += 1
        #     elif num == last:
        #         continue
        #     else:
        #         longest = max(longest, current)
        #         current = 1
        #     last = num
 
        # return max(longest, current)

        if not nums: return []

        longest, numSet = 1, set(nums)
        for num in numSet:
            if num - 1 not in numSet:
              next = num + 1
              newLongest = 1
              while(next in numSet):
                  newLongest += 1
                  next += 1
              longest = max(longest, newLongest)
        return longest
            

answer = Solution()
print(answer.longestConsecutive([1, 2, 3]))

