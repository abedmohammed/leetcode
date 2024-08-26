class Solution(object):
    def letterCombinations(self, digits):
        combinations = []
        mappings = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        def backtrack(i, current):
            if i >= len(digits):
                combinations.append(current)
                return
            
            for letter in mappings[int(digits[i])]:
                backtrack(i + 1, current + letter)

        if digits: backtrack(0, "")

        return combinations
    

answer = Solution()
print(answer.letterCombinations("23"))
