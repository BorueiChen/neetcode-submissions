class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for idx, e in enumerate(nums):
            table[target - e] = idx
        for idx, e in enumerate(nums):
            if e in table:
                if idx != table[e]:
                    return [idx, table[e]]