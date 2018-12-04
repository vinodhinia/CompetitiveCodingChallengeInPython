class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        #Sort the intervals by start Date
        intervals.sort(key=lambda interval: interval.start)
        # Start comparing in pairs
        i = 0
        j = 1
        # i=0, j=1 if 2nd intervals start time is less than the 1st intervals start time then Intervals i=overlap

        while i < len(intervals)-1 and j < len(intervals):
            interval1 = intervals[i]
            interval2 = intervals[j]

            if interval2.start < interval1.end:
                return False
            else:
                i +=1
                j +=1
        return True




i1 = Interval(7, 10)
i2 = Interval(2, 4)
intervals = [i1, i2]

#[[0,30],[5,10],[15,20]]
s = Solution()
print(s.canAttendMeetings(intervals))

i1 = Interval(0, 30)
i2 = Interval(5, 10)
i3 = Interval(15, 20)

intervals = [i1, i2, i3]

print(s.canAttendMeetings(intervals))

#[[2,4], [4, 5], [4,6]]

i1 = Interval(2, 4)
i2 = Interval(4, 5)
i3 = Interval(4, 4)

intervals = [i1, i2, i3]
print(s.canAttendMeetings(intervals))

