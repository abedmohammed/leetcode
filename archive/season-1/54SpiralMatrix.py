class Solution(object):
    def spiralOrder(self, matrix):
        t, b = 0, len(matrix)
        l, r = 0, len(matrix[0]) 
        ans = []

        while l < r and t < b:
            
            # Get top row
            for i in range(l, r):
                ans.append(matrix[t][i])
            t += 1

            # Get right column
            for i in range(t, b):
                ans.append(matrix[i][r - 1])
            r -= 1

            if not (l < r and t < b):
                break

            # Get bottom row
            for i in range(r - 1, l - 1, -1):
                ans.append(matrix[b - 1][i])
            b -= 1

            # Get left column
            for i in range(b - 1, t - 1, -1):
                ans.append(matrix[i][l])
            l += 1
    

        return ans
            
            

answer = Solution()
print(answer.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(answer.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(answer.spiralOrder([[1]]))
print(answer.spiralOrder([[6,9,7]]))
print(answer.spiralOrder([[6],[9],[7]]))