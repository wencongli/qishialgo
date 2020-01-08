'''
Runtime: 68 ms, faster than 38.78% of Python online submissions for Meeting Rooms II.
Memory Usage: 15.1 MB, less than 92.86% of Python online submissions for Meeting Rooms II.
'''

import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        # if overlap: need one more; if no overlap, don't need additional
        # maintain a minheap, recording the (earliest) ENDING TIME for each meeting
        # if a new meeting begins after the end of another, don't need additional
        # just update the ending time
        # else, we need a new meeting room, with the new ending time
        endtime=[]
        num=0
        
        for meet in intervals:
            if 0==len(endtime):
                num+=1
                heapq.heappush(endtime, meet[1])
                continue
            newstart, newend = meet[0], meet[1]
            earlyend=endtime[0]
            if newstart>=earlyend:
            # don't need additional
                heapq.heappushpop(endtime, newend)
            else:
                num+=1
                heapq.heappush(endtime, newend)
                
        return num
            
