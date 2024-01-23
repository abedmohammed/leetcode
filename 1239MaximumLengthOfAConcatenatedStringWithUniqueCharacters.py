class Solution(object):
    def maxLength(self, arr):
        def isUnique(word):
            seen = set()
            for char in word:
                if char in seen:
                    return False
                seen.add(char)

            return True

        def dfs(i, curString):
            if i == len(arr):
                if isUnique(curString):
                    return len(curString)
                else:
                    return -1

            return max(dfs(i + 1, curString + arr[i]), dfs(i + 1, curString))

        return dfs(0, "")


answer = Solution()
print(answer.maxLength(arr=["un", "iq", "ue"]))
