class Solution(object):
    def findRedundantConnection(self, edges):
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(node):
            curPar = parent[node]

            while curPar != parent[curPar]:
                parent[curPar] = parent[parent[curPar]]
                curPar = parent[curPar]

            return curPar

        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 == parent2:
                return False

            if rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]


answer = Solution()
print(
    answer.findRedundantConnection(
        [
            [7, 8],
            [2, 6],
            [2, 8],
            [1, 4],
            [9, 10],
            [1, 7],
            [3, 9],
            [6, 9],
            [3, 5],
            [3, 10],
        ]
    )
)
