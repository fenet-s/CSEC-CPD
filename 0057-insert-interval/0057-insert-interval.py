class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        result=[intervals[0]]
        for index, inter in enumerate(intervals[1:]):
            start, end = inter
            if result[-1][1] >= start:
                result[-1][1] = max(end, result[-1][1])
            else:
                result.append([start,end])
        return result 

        