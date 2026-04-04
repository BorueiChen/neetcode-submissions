class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        length = len(s)

        for idx in range(length):
            left, right = idx, idx
            while 0 <= left and right < length and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            left, right = idx, idx+1
            while 0 <= left and right < length and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        
        return res