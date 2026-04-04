class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {v: 1 for v in coins}
        def dfs(value):
            if value in memo:
                return memo[value]
            if value == 0:
                return 0

            if value < 0:
                return -1
            
            steps = []
            for coin in coins:
                step = dfs(value - coin)
                if step > 0:
                    steps.append(step)
            if steps:
                memo[value] = 1 + min(steps)
            else:
                memo[value] = -1
            return memo[value]
        
        return dfs(amount)