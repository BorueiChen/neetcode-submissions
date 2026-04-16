class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        minHeap = {}
        for h in hand:
            minHeap[h] = 1 + minHeap.get(h, 0)
        
        heapq.heapify(list(minHeap.keys()))

        while minHeap:
            top = minHeap[0]

            for idx in range(groupSize):
                if minHeap.get(top + idx, 0) == 0:
                    return False
                minHeap[top+idx] -= 1
                if minHeap[top+idx] == 0:
                    heapq.heappop(minHeap)

        return True