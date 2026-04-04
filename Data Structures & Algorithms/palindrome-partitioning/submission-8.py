class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        length = len(s)
        ans = []
        def palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -=1
            return True

        def dfs(path, start):
            if start == length:
                ans.append(path.copy())
                return
            
            for end in range(start, length):
                substring = s[start:end+1]
                if palindrome(start, end):
                    path.append(substring)
                    dfs(path, end+1)
                    path.pop()
        
        dfs([], 0)
        return ans