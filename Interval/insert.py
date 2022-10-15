class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals += [newInterval]
        intervals.sort()
        res = [intervals[0]]
        
        #merge Intervals
        def merge(interval_A,interval_B):
            merge_front = min(interval_A[0],interval_B[0])
            merge_back = max(interval_A[1],interval_B[1])
            return [merge_front,merge_back]
        
        #check intervals are overlapping or not
        def isOverlapping(interval_A,interval_B):
            front = max(interval_A[0],interval_B[0])
            back =  min(interval_A[1],interval_B[1])
            return back - front >= 0
        
        for i in range(1,len(intervals)):
            if isOverlapping(res[-1],intervals[i]):
                res[-1] = merge(res[-1],intervals[i])
            else:
                res.append(intervals[i])
        return res
            