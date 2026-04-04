class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        length = len(nums)
        if total % 2:
            return False
        
        avg = total / 2
        visited = []
        def dfs(value):
            if value == 0:
                return True
            if value < 0:
                return False
            
            result = False
            for idx in range(length):
                if result:
                    break
                if idx not in visited:
                    visited.append(idx)
                    result |= dfs(value - nums[idx])
                    visited.pop()
            return result
        
        return dfs(avg)