class Solution:
    def numDecodings(self, s: str) -> int:
        
        length = len(s)
        dp = {}
        def dfs(idx):
            if idx in dp:
                return dp[idx]
            if idx == length:
                return 1            
            if s[idx] == "0":
                return 0
            

            
            res = dfs(idx+1)
            if (idx + 1 < len(s)) and (s[idx] == "1" or 
            s[idx] == '2' and s[idx+1] in "0123456"):
                res += dfs(idx+2)
            
            dp[idx] = res
            return res

        return dfs(0)