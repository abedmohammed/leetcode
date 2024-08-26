class Solution(object):
    def solveNQueens(self, n):
        ans = []
        cols = set()
        posDiag = set()
        negDiag = set()
        currAns = []

        def backtrack(currRow):
            if currRow == n - 1:
                ans.append(currAns[:])

            for c in range(n):
                if c in cols or currRow + c in posDiag or currRow - c in negDiag:
                    continue

                row = "." * c + "Q" + "." * (n - c - 1)

                currAns.append(row)

                cols.add(c)
                posDiag.add(currRow + c)
                negDiag.add(currRow - c)

                backtrack(currRow + 1)

                currAns.pop()

                cols.remove(c)
                posDiag.remove(currRow + c)
                negDiag.remove(currRow - c)

        backtrack(-1)
        return ans


answer = Solution()
print(answer.solveNQueens(4))
