class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        max_index = {}
        n = len(s)
        for idx in range(n):
            max_index[s[idx]] = idx
        
        ans = []
        length = 1
        end = -1
        for idx in range(n):
            if idx == end or idx == n - 1:
                ans.append(length)
                length = 1
            elif idx > end:
                end = max_index[s[idx]]
                if idx == end:
                    ans.append(length)
                    length = 1
            else:
                length += 1
                end = max(end, max_index[s[idex]])
        return ans
            