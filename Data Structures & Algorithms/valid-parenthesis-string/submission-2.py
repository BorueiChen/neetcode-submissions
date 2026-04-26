class Solution:
    def checkValidString(self, s: str) -> bool:
        left, right = 0, 0
        star_left, star_right = 0, 0

        n = len(s)
        for idx in range(n):
            s_left = s[idx]
            s_right = s[n - idx]

            # left
            if s_left == ')':
                if left:
                    left -= 1
                elif star_left:
                    star_left -= 1
                else:
                    return False
            elif s_left == '(':
                left += 1
            else:
                star_left += 1

            # right
            if s_right == '(':
                if right:
                    right -= 1
                elif star_right:
                    star_right -= 1
                else:
                    return False
            elif s_right == ')':
                right += 1
            else:
                star_right += 1    
        return True        
