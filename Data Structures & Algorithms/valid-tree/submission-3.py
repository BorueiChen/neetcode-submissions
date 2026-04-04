class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {node:[] for node in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node, prev, visited):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node, visited):
                    return False
            return True
        
        res = set()
        return dfs(0, -1, res) and len(res) == n