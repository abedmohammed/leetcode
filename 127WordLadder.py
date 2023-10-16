from collections import defaultdict, deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        neighbors = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                neighbors[pattern].append(word)

        visited = set([beginWord])
        queue = deque([beginWord])
        res = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return res

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1 :]
                    for neighWord in neighbors[pattern]:
                        if neighWord not in visited:
                            visited.add(neighWord)
                            queue.append(neighWord)
            res += 1

        return 0


answer = Solution()
print(answer.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
