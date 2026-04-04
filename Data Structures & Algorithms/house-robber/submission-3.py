class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_2, rob_1 = 0, 0
        for num in nums:
            temp = max(num + rob_2, rob_1)
            rob_2 = rob_1
            rob_1 = temp
        return rob_1