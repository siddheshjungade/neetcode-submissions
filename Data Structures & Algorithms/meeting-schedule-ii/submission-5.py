"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        pq = []
        intervals.sort(key=lambda x: x.start)
        heapq.heappush(pq, intervals[0].end)
        for interval in intervals[1:]:
            if pq[0] <= interval.start:
                heapq.heappop(pq)
            heapq.heappush(pq, interval.end)
        return len(pq)