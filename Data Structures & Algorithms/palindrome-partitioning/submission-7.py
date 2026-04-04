class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def is_palindrome(start, end):
            left = start
            right = end
            while(left < right):
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        def dfs(start, path):
            if start == len(s):
                ans.append(path.copy())
                return
            
            for idx in range(start, len(s)):
                if is_palindrome(start, idx):
                    path.append(s[start:idx+1])
                    dfs(idx+1, path)
                    path.pop()
        dfs(0, [])
        return ans
