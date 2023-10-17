# class Solution(object):
#     def findItinerary(self, tickets):
# adj = {src: [] for src, dst in tickets}

# tickets.sort()
# for src, dst in tickets:
#     adj[src].append(dst)

# res = ["JFK"]

# def dfs(src):
#     if len(res) == len(tickets) + 1:
#         return True
#     if src not in adj:
#         return False

#     temp = list(adj[src])
#     for i, v in enumerate(temp):
#         adj[src].pop(i)
#         res.append(v)

#         if dfs(v):
#             return True

#         adj[src].insert(i)
#         res.pop(v)
#     return False

# dfs("JFK")
# return res


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict

        self.flightMap = defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)

        # sort the itinerary based on the lexical order
        for origin, itinerary in self.flightMap.items():
            # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort(reverse=True)

        self.result = []
        self.DFS("JFK")

        # reconstruct the route backwards
        return self.result[::-1]

    def DFS(self, origin):
        destList = self.flightMap[origin]
        while destList:
            # while we visit the edge, we trim it off from graph.
            nextDest = destList.pop()
            self.DFS(nextDest)
        self.result.append(origin)


answer = Solution()
print(
    answer.findItinerary(
        [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    )
)
