class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        left, right = 0, 0
        while right < len(nums):
            max_right = 0
            for idx in range(left, right + 1):
                max_right = max(max_right, idx + nums[idx])
            left = right + 1
            right = max_right
            result += 1
        return result