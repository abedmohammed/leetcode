import heapq


class Twitter(object):
    def __init__(self):
        self.users = {}
        self.tweets = {}
        self.count = 0

    def postTweet(self, userId, tweetId):
        self.count -= 1
        self.tweets[userId] = self.tweets.get(userId, []) + [(self.count, tweetId)]

    def getNewsFeed(self, userId):
        res = []
        latestTweetHeap = []

        self.follow(userId, userId)
        for follower in self.users[userId]:
            if follower in self.tweets:
                index = len(self.tweets[follower]) - 1
                count, tweetId = self.tweets[follower][index]
                latestTweetHeap.append([count, tweetId, follower, index])
        heapq.heapify(latestTweetHeap)
        while latestTweetHeap and len(res) < 10:
            count, tweetId, follower, index = heapq.heappop(latestTweetHeap)
            res.append(tweetId)

            if index > 0:
                index -= 1
                count, tweetId = self.tweets[follower][index]
                heapq.heappush(latestTweetHeap, [count, tweetId, follower, index])

        return res

    def follow(self, followerId, followeeId):
        if followerId not in self.users:
            self.users[followerId] = set()
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId not in self.users:
            self.users[followerId] = set()
        self.users[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
# obj.follow(1, 2)
# obj.follow(1, 3)
# obj.unfollow(1, 2)
obj.postTweet(1, 111)
# obj.postTweet(2, 112)
print(obj.getNewsFeed(1))
