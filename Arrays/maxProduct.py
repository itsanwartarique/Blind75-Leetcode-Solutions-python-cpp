class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currentMax = 1
        currentMin = 1
        for i in nums:
            if i==0:
                currentMax,currentMin = 1,1
                continue
            temp1 = currentMax*i
            temp2 = currentMin*i
            currentMax = max(temp1,temp2,i)
            currentMin = min(temp1,temp2,i)
            res = max(res,temp1,temp2)
        return res