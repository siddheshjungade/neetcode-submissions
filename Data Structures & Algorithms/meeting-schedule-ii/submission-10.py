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
        intervals.sort(key = lambda x: x.start)
        mx = 0
        q = []
        for i in intervals:
            while q and q[0] <= i.start:
                heapq.heappop(q)
            heapq.heappush(q,i.end)
            mx = max(mx, len(q))

        return mx

        