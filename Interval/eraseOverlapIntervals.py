class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count,left,right = 0,0,1
        while right<len(intervals):
            #case 1: left and right intervals are non-overlaping
            if intervals[left][1] <= intervals[right][0]:
                left = right
                right +=1
            #case 2 : left and right intervals are partially overlaping : remove right interval
            elif intervals[left][1] <= intervals[right][1]:
                count +=1
                right +=1
            #case 3 : left and right intervals are fully overlapping : remove big interval
            else:
                count +=1
                left = right
                right += 1
        return count
                