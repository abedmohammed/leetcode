class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """


answer = Solution()
print(
    answer.minInterval(intervals=[[1, 4], [2, 4], [3, 6], [4, 4]], queries=[2, 3, 4, 5])
)
