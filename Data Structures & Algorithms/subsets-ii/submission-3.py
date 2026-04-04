class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()
        def dfs(start, subset):
            if start == len(nums):
                self.ans.append(subset.copy())
                return
            
            self.ans.append(subset.copy())

            for idx in range(start, len(nums)):
                if idx > start and nums[idx] == nums[idx-1]:
                    continue

                subset.append(nums[idx])
                dfs(idx+1, subset)
                subset.pop()

        dfs(0,[])
        return self.ans