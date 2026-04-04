class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        length = len(nums)
        def dfs(idx):
            if idx in dp:
                return dp[idx]
            
            step = 1
            for j in range(idx+1, length):
                if nums[idx] < nums[j]:
                    step = max(step, 1 + dfs(j))
            dp[idx] = step
            return step
        
        ans = 0
        for idx in range(length):
            ans = max(ans, dfs(idx))
        
        print(dp)
        return ans