class Solution:
    def numDecodings(self, s: str) -> int:
        
        length = len(s)
        memo = {}
        digit1 = [str(v) for v in range(1,10)]
        digit2 = [str(v) for v in range(10,26+1)]
        def dfs(string):
            if string in memo:
                return memo[string]

            if not string:
                return 1
            
            ways = 0
            if string[:1] in digit1:
                ways += dfs(string[1:])
            if string[:2] in digit2:
                ways += dfs(string[2:])
            
            memo[string] = ways
            return memo[string]
        
        return dfs(s)
            

            