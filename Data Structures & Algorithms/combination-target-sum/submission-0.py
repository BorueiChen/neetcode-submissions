class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        def dfs(start, path, total):
            if total == target:
                self.ans.append(path.copy())
                return
            
            if start >= len(candidates) or total > target:
                return
            
            path.append(candidates[start])
            dfs(start, path, total + candidates[start])
            path.pop()
            dfs(start + 1, path, total)

        dfs(0, [], 0)
        return self.ans