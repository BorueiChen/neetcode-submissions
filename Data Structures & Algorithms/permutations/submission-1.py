class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def dfs(candidate, subset):
            if len(candidate) == 0:
                self.ans.append(subset.copy())
                return
            
            for i, num in enumerate(candidate):
                subset.append(num)
                dfs(candidate[:i] + candidate[i+1:], subset)
                subset.pop()
        
        dfs(nums, [])
        return self.ans