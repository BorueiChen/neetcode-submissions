class Solution:
    def numDecodings(self, s: str) -> int:
        
        digit1 = [str(value) for value in range(1, 10)]
        digit2 = [str(value) for value in range(10,26+1)]
        memo = {}
        def dfs(word):
            if word in memo:
                return memo[word]
            
            if not word:
                return 1
            
            one = word[:1]
            two = word[:2]
            ways = 0
            if one in digit1:
                ways += dfs(word[1:])
            if two in digit2:
                ways += dfs(word[2:])
            
            memo[word] = ways
            return memo[word]

        return dfs(s)