class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        current = self
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        
        current.isWord = True

class Solution(object):
    def findWords(self, board, words):
        trie = TrieNode()

        for word in words:
            trie.addWord(word)

        rows, columns = len(board), len(board[0])

        ans = set()

        def dfs(i, j, current, word):
            if (i < 0 or j < 0 or i >= rows or j >= columns) or (board[i][j] == ".") or (board[i][j] not in current.children):
                return False
            
            letter = board[i][j]
            word += letter
            current = current.children[letter]
            board[i][j] = "."

            if current.isWord:
                ans.add(word)

            dfs(i - 1, j, current, word)
            dfs(i + 1, j, current, word)
            dfs(i, j - 1, current, word)
            dfs(i, j + 1, current, word)

            board[i][j] = letter

        for i in range(rows):
            for j in range(columns):
                dfs(i, j, trie, "")

        return list(ans)

            
                
                

answer = Solution()
print(answer.findWords([["a", "a"], ["a", "a"]], ["aaaaa"]))
print(answer.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
print(answer.findWords([["a","b","c"],["a","e","d"],["a","f","g"]], ["abcdefg"]))