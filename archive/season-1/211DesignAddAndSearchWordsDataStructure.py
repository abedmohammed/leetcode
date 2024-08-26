class WordDictionary(object):

    def __init__(self):
        self.head = {}

    def addWord(self, word):
        current = self.head

        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]

        current["-"] = True
        

    def search(self, word):
        current = self.head
        
        def searchRecursive(word, current):
            for i in range(len(word)):
                print("gay")
                if word[i] == ".":
                    print(current)
                    for possibility in current:
                        if possibility == "-": continue
                        if searchRecursive(word[i+1:], current[possibility]):
                            return True
                if word[i] not in current:
                    return False
                current = current[word[i]]
            return "-" in current
        
        return searchRecursive(word, current)
            

obj = WordDictionary()

for word in ["a","a"]:
    obj.addWord(word)

for word in ["a."]:
  print(obj.search(word))
    
