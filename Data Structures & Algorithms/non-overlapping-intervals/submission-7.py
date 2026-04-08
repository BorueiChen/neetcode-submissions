class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        # (1,2), (2,4), (1,4)
        cur_s, cur_e = intervals[0]
        remove = 0
        for idx in range(1, len(intervals)):
            s, e = intervals[idx]
            if (s <= cur_s and e <= cur_s) or (s >= cur_e and e >= cur_e):
                if (cur_s == s and cur_e == e):
                    remove += 1
                else:
                    cur_s, cur_e = s, e
            else:
                remove += 1

        return remove