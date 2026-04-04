class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    def helper(self, nums):
        two, one = 0, 0
        for num in nums:
            newOne = max(two + num, one)
            two = one
            one = newOne
        return one