class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = 0
        for i in nums:
            currentSum = max(currentSum + i, i)
            maxSum = max(maxSum,currentSum)
        return maxSum
            
        
        