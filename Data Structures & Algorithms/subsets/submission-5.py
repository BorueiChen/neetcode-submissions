class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def dfs(idx, subset):
            if idx > len(nums):
                self.ans.append(subset.copy())
                return
            
            self.ans.append(subset.copy())
            for i, num in enumerate(nums[idx:]):
                subset.append(num)
                dfs(idx + i + 1, subset)
                subset.pop()
        
        dfs(0, [])
        return self.ans