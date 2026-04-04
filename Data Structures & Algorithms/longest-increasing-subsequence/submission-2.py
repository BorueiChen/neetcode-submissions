class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        length = len(nums)
        memo = {}
        def dfs(idx):
            if idx in memo:
                return memo[idx]
            
            step = 1
            for start in range(idx+1, length):
                if nums[idx] < nums[start]:
                    step = max(step, 1+dfs(start))
            memo[idx] = step
            return step
        
        ans = 0
        for idx in range(length):
            ans = max(ans, dfs(idx))
        return ans