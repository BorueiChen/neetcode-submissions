class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ans = False
        length = len(nums)
        def dfs(idx, target):
            if ans == True:
                return
            if target == 0:
                ans = True
                return
            if target < 0 or idx == length:
                return
            
            dfs(idx+1, target - nums[idx])
            dfs(idx+1, target)
            return
        
        if sum(nums) % 2 == 0:
            dfs(0, sum(nums)/2)
        return ans