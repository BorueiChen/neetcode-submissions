class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []

        def dfs(subset, left, right):
            if left > right:
                return
            if left < 0 or right < 0:
                return
            
            if left == 0 and right == 0:
                self.ans.append(''.join(subset))
                return
            
            # take left
            subset.append("(")
            dfs(subset, left - 1, right)
            subset.pop()
            # take right
            subset.append(")")
            dfs(subset, left, right - 1)
            subset.pop()
        
        dfs([], n, n)
        return self.ans