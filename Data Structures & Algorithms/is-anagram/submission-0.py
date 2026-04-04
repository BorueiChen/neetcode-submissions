class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = [char for char in s]
        list_t = [char for char in t]

        if [e for e in sorted(list_s)] == [e for e in sorted(list_t)]:
            return True
        return False