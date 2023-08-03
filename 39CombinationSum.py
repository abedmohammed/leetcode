class Solution(object):
    def combinationSum(self, candidates, target):
        self.ans = []
        self.current = []
        self.target = target

        for i in range(len(candidates)):
            self.recursiveAdd(0, candidates[i:])
            
        return self.ans

    def recursiveAdd(self, sum, candidates):
        if not candidates or candidates[0] + sum > self.target:
            return
        
        self.current.append(candidates[0])
        sum += candidates[0]
        print(self.current)
        print(sum)
        if sum == self.target:
            self.ans.append(self.current.copy())
            self.current.pop()
            return
        
        self.recursiveAdd(sum, candidates)
        for i in range(1, len(candidates)):
            self.recursiveAdd(sum, candidates[i:])
        self.current.pop()


answer = Solution()
print(answer.combinationSum([3,5,8], 11))