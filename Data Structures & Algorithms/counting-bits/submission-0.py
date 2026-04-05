class Solution:
    def countBits(self, n: int) -> List[int]:
        return [self.count(idx) for idx in range(n+1)]
    def count(self, n):
        res = 0
        while n:
            if n & 1:
                res += 1
            n >>= 1
        return res