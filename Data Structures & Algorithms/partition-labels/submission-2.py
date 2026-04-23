class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        max_index = {}
        n = len(s)
        for idx in range(n):
            max_index[s[idx]] = idx
        
        ans = []
        length = 0
        end = -1
        for idx in range(n):
            end = max(end, max_index[s[idx]])
            length += 1

            if idx == end:
                ans.append(length)
                length = 0

        return ans
            