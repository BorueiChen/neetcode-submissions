class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []

        def dfs(start, path):
            if start == len(s):
                self.ans.append(path.copy())
                return
            
            for idx in range(start, len(s)):
                if self.is_palin(s, start, idx):
                    path.append(s[start:idx + 1])
                    dfs(idx+1, path)
                    path.pop()
        
        dfs(0, [])
        return self.ans
        
    def is_palin(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right-= 1
        return True