class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        # (1,2), (2,4), (1,4)
        cur_s, cur_e = intervals[0]
        remove = 0
        for idx in range(1, len(intervals)):
            s, e = intervals[idx]
            if (cur_s < e and e < cur_e) or (cur_s < s and s < cur_e):
                remove += 1
            else:
                cur_s, cur_e = s, e
        return remove