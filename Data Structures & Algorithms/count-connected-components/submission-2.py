class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {n_:[] for n_ in range(n)}

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(cur, prev, visited):
            if cur in visited:
                return
            
            visited.add(cur)
            for neighbor in graph[cur]:
                if neighbor == prev:
                    continue
                dfs(neighbor, cur, visited)
        count = 0
        visited = set()
        for node in range(n):
            res = set()
            dfs(node, -1, res)
            if len(visited & res) == 0:
                count += 1
                visited |= res
        
        return count
            