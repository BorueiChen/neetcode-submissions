class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        res = []
        indegree = {course:0 for course in range(numCourses)}
        graph = {course:[] for course in range(numCourses)}
        for course, pre in  prerequisites:
            indegree[pre] += 1
            graph[course].append(pre)
        
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        while queue:
            for _ in range(len(queue)):
                course = queue.popleft()
                res.append(course)
                for next_task in graph[course]:
                    indegree[next_task] -= 1
                    if indegree[next_task] == 0:
                        queue.append(next_task)
        
        return True if len(res) == numCourses else False
