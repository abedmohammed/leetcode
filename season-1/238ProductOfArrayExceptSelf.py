class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        ans = [1] * length

        product = 1
        for i in range(length):
            ans[i] = product
            product *= nums[i]

        print(ans)

        product = 1
        for i in range(length - 1, -1, -1):
            ans[i] = product * ans[i]
            product *= nums[i]

        return ans


answer = Solution()
print(answer.productExceptSelf([1, 2, 3, 4]))