from collections import defaultdict, deque
import heapq

class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.followsMap = defaultdict(set)
        self.tweetsMap = defaultdict(deque)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweetsMap[userId].appendleft((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list:
        """
        Retrieve the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
        """
        min_heap = []
        self.followsMap[userId].add(userId)
        
        for uid in self.followsMap[userId]:
            if uid in self.tweetsMap:
                tweets = self.tweetsMap[uid]
                for tweet in tweets:
                    heapq.heappush(min_heap, (tweet[1], tweet[0]))
                    if len(min_heap) > 10:
                        heapq.heappop(min_heap)

        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])

        return result[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followsMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.followsMap[followerId]:
            self.followsMap[followerId].remove(followeeId)

# Example usage:
# twitter = Twitter()
# twitter.postTweet(1, 5)  # User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1)  # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
# twitter.follow(1, 2)  # User 1 follows user 2.
# twitter.postTweet(2, 6)  # User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1)  # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.unfollow(1, 2)  # User 1 unfollows user 2.
# twitter.getNewsFeed(1)  # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
