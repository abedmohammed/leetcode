class Solution(object):
    def pacificAtlantic(self, heights):
        pacificHash = {}
        atlanticHash = {}

        rows = len(heights)
        columns = len(heights[0])

        for i in range(columns):
            self.dfs(heights, pacificHash, 0, i, heights[0][i])
            self.dfs(heights, atlanticHash, rows - 1, i, heights[rows-1][i])

        for i in range(rows):
            self.dfs(heights, pacificHash, i, 0, heights[i][0])
            self.dfs(heights, atlanticHash, i, columns - 1, heights[i][columns-1])

        ans = []
        for pair in pacificHash:
            if pair in atlanticHash:
                ans.append(list(pair))

        return ans
    
    def dfs(self, heights, hash, i, j, prev):
        if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]) or (i,j) in hash or heights[i][j] < prev:
            return
        
        hash[(i,j)] = 1
        number = heights[i][j]

        self.dfs(heights, hash, i-1, j, number)
        self.dfs(heights, hash, i, j+1, number)
        self.dfs(heights, hash, i+1, j, number)
        self.dfs(heights, hash, i, j-1, number)

        

ans = Solution()
print(ans.pacificAtlantic([[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]))
