class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        #check if intervals overlap
        def isOverlapping(interval_A,interval_B):
            front = max(interval_A[0],interval_B[0])
            back =  min(interval_A[1],interval_B[1])
            return back - front >= 0
        #merge Overlapping intervals
        def merge(interval_A,interval_B):
            merged_front = min(interval_A[0],interval_B[0])
            merged_back =  max(interval_A[1],interval_B[1])
            return [merged_front,merged_back]
        #iterate over intervals
        for i in range(1,len(intervals)):
            if isOverlapping(res[-1],intervals[i]):
                res[-1] = merge(res[-1],intervals[i])
            else:
                res.append(intervals[i])
        return res