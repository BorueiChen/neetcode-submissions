class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dis = x**2 + y**2
            heapq.heappush(heap, (-dis, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        while len(heap) > 0:
            dis, x, y = heapq.heappop(heap)
            ans.append([x, y])
        return ans