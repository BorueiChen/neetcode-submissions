class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [-cnt for cnt in counter.values()]
        heapq.heapify(max_heap)
        queue = deque()
        time = 0

        while max_heap or queue:
            time += 1

            if max_heap:
                freq = heapq.heappop(max_heap)
                freq += 1
                if freq:
                    queue.append((freq, time + n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        
        return time
                