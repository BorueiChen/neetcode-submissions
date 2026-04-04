class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        for a,b in edges:
            if a not in graph:
                graph[a] = [b]
            else:
                graph[a].append(b)
            if b not in graph:
                graph[b] = [a]
            else:
                graph[b].append(a)

        def dfs(cur, prev, remove, visited):
            if cur in visited:
                return False
            
            visited.add(cur)
            for next_n in graph[cur]:
                if (cur == remove[0] and next_n == remove[1]) or\
                (cur == remove[1] and next_n == remove[0]):
                    continue
                if next_n == prev:
                    continue
                if not dfs(next_n, cur, remove, visited):
                    return False
            return True
        
        for edge in edges[::-1]:
            visited = set()
            if len(graph[edge[0]]) > 1 and dfs(edge[0], -1, edge, visited) and len(visited) == len(graph):
                return edge
