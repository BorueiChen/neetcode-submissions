class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {coin:1 for coin in coins}

        def dfs(value):
            if value in memo:
                return memo[value]

            if value <= 0:
                return 0

            ways = []
            for coin in coins:
                way = dfs(value - coin)
                if way > 0:
                    ways.append(way)
            if ways:
                memo[value] = 1 + min(ways)
            else:
                memo[value] = 0
            return memo[value]
        if amount == 0:
            return 0
        ways = dfs(amount)
        return ways if ways > 0 else -1