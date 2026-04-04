class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [stone * -1 for stone in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            if x == y:
                continue
            else:
                heapq.heappush(heap, x - y)

        return heap[0]*-1 if heap else 0