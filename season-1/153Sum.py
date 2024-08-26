class Solution(object):
    def threeSum(self, nums):
        # hashNums = {}
        # sortedNums = sorted(nums)

        # ans = []
        # for i in range(len(nums)):
        #     hashNums[sortedNums[i]] = i

        # lastI = -1
        # lastJ = -1
        # for i in range(len(sortedNums)):
        #     if lastI != -1 and sortedNums[i] == sortedNums[lastI]: continue
        #     for j in range(i+1, len(sortedNums)):
        #         if lastJ != -1 and sortedNums[j] == sortedNums[lastJ]: continue
        #         target = -(sortedNums[i] + sortedNums[j])
        #         if target in hashNums and j < hashNums[target]:
        #             ans.append([sortedNums[i], sortedNums[j], target])
        #         lastJ = j
        #     lastI = i

        # print(hashNums)
        # return ans

        nums.sort()
        ans = []

        print(nums)
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            while l < r:
                target = n + nums[l] + nums[r]
                if target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    ans.append([n, nums[l], nums[r]])
                    l += 1
                
                    while l < r and nums[l] == nums[l-1]:
                        l+=1

        return ans

answer = Solution()
print(answer.threeSum([-3, 3, 4, -3, 1, 2]))