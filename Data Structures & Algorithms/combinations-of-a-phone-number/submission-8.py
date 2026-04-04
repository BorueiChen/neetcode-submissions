class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {
            '0': ['+'],
            '1': [],
            '2': ["A", "B", "C"],
            '3': ['D', 'E', "F"],
            '4': ['G', 'H', "I"],
            '5': ['J', "K", "L"],
            '6': ["M", "N", "O"],
            '7': ['P', 'Q', "R", 'S'],
            '8': ["T", 'U', 'V'],
            '9': ['W', 'X', 'Y', 'Z']
        }

        self.ans = []
        def dfs(path, start):
            if start == len(digits):
                self.ans.append(path)
                return
            
            if digits[start] not in table:
                return

            for char in table[digits[start]]:
                dfs(path+char.lower(), start + 1)

        if digits:
            dfs("",0)
        return self.ans