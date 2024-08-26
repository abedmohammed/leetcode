class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        combos_12 = {}
        length = len(nums1)
        for i in range(length):
            for j in range(length):
                add = nums1[i] + nums2[j]
                if(add in combos_12):
                    combos_12[add].append([i, j])
                else:
                    combos_12[add] = [[i,j]]

        combos_34 = {}
        for i in range(length):
            for j in range(length):
                add = nums3[i] + nums4[j]
                if(add in combos_34):
                    combos_34[add].append([i, j])
                else:
                    combos_34[add] = [[i,j]]

        count = 0
        for value in combos_12:
            target = -value
            if(target in combos_34):
                pairs_1 = len(combos_12[value])
                pairs_2 = len(combos_34[target])
                count += pairs_1*pairs_2

        return count      
          
answer = Solution()
print(answer.fourSumCount([1],[-1],[-1],[1]))