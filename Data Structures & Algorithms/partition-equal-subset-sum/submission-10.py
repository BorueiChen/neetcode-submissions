class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        length = len(nums)
        def dfs(idx, target):
            if (idx, target) in memo:
                return memo[(idx, target)]
            if idx == length or target < 0:
                memo[(idx, target)] = False
                return
            if target == 0:
                memo[(idx, target)] = True
                return
            
            memo[(idx, target)] = dfs(idx + 1, target) or \
            dfs(idx + 1, target - nums[idx])
            return memo[(idx, target)]
        if sum(nums) % 2 == 0:
            return dfs(0, sum(nums)/2)
        return False
        