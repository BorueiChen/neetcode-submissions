class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        self.count = 0

    def addNum(self, num: int) -> None:
        self.count += 1
        heapq.heappush(self.left, -1 * num)

        if len(self.left) - len(self.right) == 2:
            heapq.heappush(self.right, heapq.heappop(self.left) * -1)
        
        if self.right and self.left and self.left[0] * -1 > self.right[0]:
            heapq.heappush(self.right, heapq.heappop(self.left) * -1)
            heapq.heappush(self.left, heapq.heappop(self.right) * -1)
            

    def findMedian(self) -> float:
        if self.count % 2:
            return self.left[0]*-1
        else:
            return ((self.left[0]*-1) + self.right[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()