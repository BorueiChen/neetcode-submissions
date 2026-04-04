class Twitter:

    def __init__(self):
        self.user_to_heap = {} # user: heap(time, id)
        self.count = 0
        self.follow_table = {} # user: set

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_to_heap:
            self.user_to_heap[userId] = [(self.count, tweetId)]
            self.count += 1
        else:
            self.user_to_heap[userId].append((self.count, tweetId))
            self.count += 1

        if userId not in self.follow_table:
            self.follow_table[userId] = set([userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        output = []
        for user in self.follow_table.get(userId, []):
            for pair in self.user_to_heap.get(user, []):
                heapq.heappush(output, pair)
                if len(output) > 10:
                    heapq.heappop(output)
        
        ans = []
        while output:
            _, tweetId = heapq.heappop(output)
            ans.append(tweetId)
        return ans[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_table:
            self.follow_table[followerId] = set([followerId, followeeId])
        else:
            self.follow_table[followerId].add(followeeId)       

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId in self.follow_table[followerId]:
            self.follow_table[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)