class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = {}
        for word in strs:
            counter = [0 for _ in range(27)]
            for c in word:
                counter[ord(c) - ord('a')] += 1
            if tuple(counter) in output:
                output[tuple(counter)].append(word)
            else:
                output[tuple(counter)] = [word]
        
        ans = []
        for v in output.values():
            ans.append(v)
        return ans
            