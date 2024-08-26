class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie(object):

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word):
        current = self.head
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        
        current.isWord = True
        

    def search(self, word):
        current = self.head
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.isWord
        

    def startsWith(self, prefix):
        current = self.head
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("Apple")
print(obj.search("Applee"))
