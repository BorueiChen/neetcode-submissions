class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = 0, 0
        for idx in range(2, len(cost)+1):
            temp = one
            one = min(one + cost[idx-1], two + cost[idx - 2])
            two = temp
        return one