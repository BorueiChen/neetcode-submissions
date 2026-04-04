class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min = 0, 0
        ans = 0
        for idx, num in enumerate(nums):
            if idx == 0:
                cur_max, cur_min = num, num
                ans = num
                continue
            temp = cur_max
            cur_max = max(cur_max * num, cur_min * num, num)
            cur_min = min(temp * num, cur_min * num, num)
            ans = max(ans, cur_max)
        return ans