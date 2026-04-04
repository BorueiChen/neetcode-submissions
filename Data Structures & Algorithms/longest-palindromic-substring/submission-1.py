class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max_len, res = 0, ""
        for idx in range(len(s)):
            max_len, res = self.helper(idx, idx, s, max_len, res)
            max_len, res = self.helper(idx, idx+1, s, max_len, res)
        return res
    
    def helper(self, left, right, s, max_len, res):
        while 0 <= left and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                max_len = right - left + 1
                res = s[left:right+1]
            left -= 1
            right += 1
        return max_len, res

