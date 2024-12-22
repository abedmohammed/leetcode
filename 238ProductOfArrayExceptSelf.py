class Solution(object):
    def productExceptSelf(self, nums):
        # # O(n) space
        # n = len(nums)

        # leftProduct = [nums[0]] * n
        # rightProduct = [nums[-1]] * n

        # for i in range(1, n):
        #     leftProduct[i] = leftProduct[i-1] * nums[i]

        # for i in range(n - 2, -1, -1):
        #     rightProduct[i] = rightProduct[i+1] * nums[i]

        # res = [1] * n

        # for i in range(n):
        #     left = leftProduct[i-1] if i > 0 else 1
        #     right = rightProduct[i+1] if i < n - 1 else 1

        #     res[i] = left * right

        # return res

        # O(1) space
        n = len(nums)

        res = [nums[-1]] * n

        for i in range(n - 2, -1, -1):
            res[i] = res[i + 1] * nums[i]

        cur = 1

        res[0] = res[1]

        for i in range(1, n - 1):
            cur *= nums[i - 1]
            res[i] = cur * res[i + 1]

        res[-1] = cur * nums[i]

        return res
