# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n
        bad_version = 0
        while (left <= right):
            mid = (left + right) // 2
            is_bad = self.isBadVersion(mid)

            if(is_bad):
                bad_version = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return bad_version
    
    def isBadVersion(self, n):
        if(n == 4):
            return True
        return False

answer = Solution()
print(answer.firstBadVersion(5))