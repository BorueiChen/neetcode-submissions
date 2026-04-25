class Solution:
    def checkValidString(self, s: str) -> bool:
        
        n = len(s)
        open = 0
        star = 0
        for idx in range(n):
            if s[idx] == ')':
                if open:
                    open -= 1
                elif star:
                    star -= 1
                else:
                    return False
            elif s[idx] == '(':
                open += 1
            else:
                star += 1

        close = 0
        star = 0
        for idx in range(n - 1, -1, -1):
            if s[idx] == '(':
                if close:
                    close -= 1
                elif star:
                    star -= 1
                else:
                    return False
            elif s[idx] == ')':
                close += 1
            else:
                star += 1        

        return True