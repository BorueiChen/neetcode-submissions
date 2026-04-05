class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = set([0])
        length = len(nums)
        if sum(nums) % 2 == 0:
            target = sum(nums) / 2
            for idx in range(length - 1, -1, -1):
                next_dp = set()
                for num in dp:
                    next_dp.add(num)
                    next_dp.add(num + nums[idx])
                    if target in next_dp:
                        return True
                dp = next_dp
        return False