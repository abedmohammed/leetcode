class Node(object):
    def __init__(self):
        self.isWord = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]

        curr.isWord = True

    def search(self, word):
        curr = self.root

        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False

        return curr.isWord

    def startsWith(self, prefix):
        curr = self.root

        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False

        return True


trie = Trie()
trie.insert("apple")
trie.insert("apps")
trie.insert("appstore")
print(trie.startsWith("apps"))
