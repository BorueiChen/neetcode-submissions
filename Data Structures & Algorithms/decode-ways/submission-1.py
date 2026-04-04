class Solution:
    def numDecodings(self, s: str) -> int:
        
        digit1 = [str(value) for value in range(1, 10)]
        digit2 = [str(value) for value in range(10,26+1)]
        def dfs(word, start):
            if start == len(s):
                return 1
            if start > len(s):
                return 0
            
            ways1 = 0
            next_word = word[start:start+1]
            if next_word in digit1:
                ways1 = dfs(word, start+1)
            ways2 = 0
            next_word = word[start:start+2]
            if len(next_word) == 2 and next_word in digit2:
                ways2 = dfs(word, start+2)
            
            return ways1 + ways2

        return dfs(s, 0)