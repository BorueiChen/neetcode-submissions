class Solution:
    def rob(self, nums: List[int]) -> int:
        two, one = 0, 0
        for num in nums:
            newOne = max(two + num, one)
            two = one
            one = newOne
        return one