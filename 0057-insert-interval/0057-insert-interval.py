class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        res = []
        i = 0

        while i < len(intervals):
            interval =  intervals[i]
            cur_interval = []
            if newInterval and newInterval[0] < interval[0]:
                cur_interval = newInterval
                newInterval = []
            else:
                cur_interval = interval
                i += 1

            if res and  res[-1][1] >= cur_interval[0]:
                res[-1][1] = max(res[-1][1], cur_interval[1])
            else:
                res.append(cur_interval)


        if newInterval and  res[-1][1] >= newInterval[0]:
            res[-1][1] = max(res[-1][1], newInterval[1])
        elif newInterval:
            res.append(newInterval)


        return res