"""
A popular problem usually appears in the RESTFUL API.
1. follwers is a dictionary storing following relationships, e.g., 1: [1, 4, 6]
2. tweets is a list storing all tweets, new ones are appended to the right
3. a user cannot unfollow its own tweets
"""
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = []
        self.followers = {}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.followers:
            self.followers[userId] = [userId]
        users = set(self.followers[userId])
        res = []
        counter = 0
        for tweet in reversed(self.tweets):
            if tweet[0] in users:
                res.append(tweet[1])
                counter += 1
            if counter == 10:
                break
        return res
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.followers:
            self.followers[followerId] = [followerId]
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].append(followeeId)
            
            
    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.followers:
            self.followers[followerId] = [followerId]
        if followeeId != followerId and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)