class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = {}
        for h in hand:
            count[h] = 1 + count.get(h, 0)
        
        minHeap = heapq.heapify(list(count.keys()))
        print(minHeap)
        while minHeap:
            top = minHeap[0]
            print(f"start")
            for idx in range(top, top + groupSize):
                print(f"{idx}: {count.get(idx, 0)}")
                if count.get(idx, 0) == 0:
                    return False
                count[idx] -= 1
                if count[idx] == 0:
                    if idx == minHeap[0]:
                        heapq.heappop(minHeap)

        return True