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
        intervals.sort(key = lambda x: x.start)
        for i in intervals:
            if pq and pq[0] <= i.start:
                heapq.heappop(pq)
            heapq.heappush(pq,i.end)

        return len(pq)

        