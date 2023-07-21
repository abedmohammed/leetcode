class Solution(object):
    def exist(self, board, word):
        rows = len(board)
        columns = len(board[0])

        for row in board:
            print(row)

        def search(i, j, k):
            if k >= len(word): return True

            if(i < 0 or i >= rows or j < 0 or j >= columns or board[i][j] == "." or board[i][j] != word[k]):
                return False
            


            letter = board[i][j]
            board[i][j] = "."
                
            if (search(i-1, j, k+1) or search(i+1, j, k+1) or search(i, j-1, k+1) or search(i, j+1, k+1)):
                return True
            
            board[i][j] = letter
            return False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                letter = board[i][j]
                if letter == word[0]:
                    if search(i, j, 0): 
                        return True

        return False



answer = Solution()
print(answer.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCEEESED"))