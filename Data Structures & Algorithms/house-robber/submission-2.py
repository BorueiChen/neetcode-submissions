class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(n):
            if n in memo:
                return memo[n]
            if n >= len(nums):
                return 0
            
            memo[n] = nums[n]
            for idx in range(n+2, len(nums)):
                memo[n] = max(memo[n], nums[n] + dfs(idx))
            return memo[n]
        
        return max(dfs(0), dfs(1))