class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates.sort()

        def dfs(idx, subset, total):
            if total == target:
                self.ans.append(subset.copy())
                return
            
            if total > target or idx == len(candidates):
                return
                            
            # take candidate
            subset.append(candidates[idx])
            dfs(idx+1, subset, total + candidates[idx])
            subset.pop()
            # skip candidate
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            dfs(idx+1, subset, total)
        
        dfs(0,[],0)
        return self.ans
