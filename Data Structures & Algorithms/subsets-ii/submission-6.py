class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def dfs(start, path):
            if start == len(nums):
                ans.append(path.copy())
                return
            
            ans.append(path.copy())
            for idx in range(start, len(nums)):
                if idx > start and nums[idx] == nums[idx-1]:
                    continue
                path.append(nums[idx])
                dfs(idx+1, path)
                path.pop()
        
        dfs(0, [])
        return ans