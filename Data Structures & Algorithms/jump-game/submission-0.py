class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        cur = len(nums) - 1
        expect = 0
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] >= expect:
                cur = idx
                expect = 0
            expect += 1
        
        return True if cur == 0 else False