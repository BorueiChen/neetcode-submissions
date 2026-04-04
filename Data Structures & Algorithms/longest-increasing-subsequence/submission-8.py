class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        LIS = [1] * length

        for idx in range(length - 1, -1, -1):
            for j in range(idx+1, length):
                if nums[idx] < nums[j]:
                    LIS[idx] = max(LIS[idx], 1+LIS[j])
        
        return max(LIS)