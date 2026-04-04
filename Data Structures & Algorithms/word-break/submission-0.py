class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        max_length = max([len(w) for w in wordDict])
        min_length = min([len(w) for w in wordDict])
        def dfs(word):
            if word in memo:
                return memo[word]
            
            if not word:
                return True
            
            if len(word) < min_length:
                return False
            
            result = False
            for idx in range(len(word)):
                if idx == max_length:
                    break
                if word[:idx+1] in wordDict:
                    result |= dfs(word[idx+1:])
            memo[word] = result
            return result
        
        return dfs(s)