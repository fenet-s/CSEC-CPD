class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        left= 0
        result = [intervals[0]]
        for index,interval in enumerate(intervals[1:]):
            start, end = interval

            if result[-1][1] >= start:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start,end])
        return result
                
        