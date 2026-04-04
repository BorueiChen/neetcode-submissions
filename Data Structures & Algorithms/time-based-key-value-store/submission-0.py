class TimeMap:
    def __init__(self):
        self.table = {} # key: list[(time, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.table:
            self.table[key] = [(timestamp, value)]
        else:
            self.table[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table:
            return ""
        # binary search
        left, right = 0, len(self.table[key]) - 1
        ans = ""
        while left <= right:
            mid = (left + right) // 2
            if self.table[key][mid][0] <= timestamp:
                ans = self.table[key][mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return ans