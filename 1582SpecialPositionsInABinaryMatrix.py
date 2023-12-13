class Solution(object):
    def numSpecial(self, mat):
        rows = {}
        cols = {}
        ans = 0

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    rows[i] = rows.get(i, 0) + 1
                    cols[j] = cols.get(j, 0) + 1

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    ans += 1

        return ans


answer = Solution()
print(answer.numSpecial(mat=[[1, 0, 0], [0, 0, 1], [1, 0, 0]]))
print(answer.numSpecial(mat=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(answer.numSpecial(mat=[[1, 0, 0], [1, 0, 1], [1, 0, 0]]))
