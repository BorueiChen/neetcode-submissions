class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {c:[] for c in range(numCourses)}
        indegree = {c:0 for c in range(numCourses)}
        for c, p in prerequisites:
            graph[c].append(p)
            indegree[p] += 1
        
        queue = deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                queue.append(c)
        res = []
        while queue:
            for _ in range(len(queue)):
                c = queue.popleft()
                res.append(c)
                for next_c in graph[c]:
                    indegree[next_c] -= 1
                    if indegree[next_c] == 0:
                        queue.append(next_c)
        
        return res[::-1] if len(res) == numCourses else []