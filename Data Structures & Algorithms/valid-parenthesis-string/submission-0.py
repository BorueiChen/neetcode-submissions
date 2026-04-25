class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        n = len(s)

        for idx in range(n):
            if s[idx] == "(":
                low += 1
                high += 1
            elif s[idx] == ')':
                low -= 1
                high -= 1
            else:
                low += 1
                high -= 1
        
        if low < 0:
            return False
        
        if high > 0:
            return False
        
        return True
