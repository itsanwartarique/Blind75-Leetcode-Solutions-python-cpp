class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*(n+1)
        def f(nums,n):
            if dp[n] != -1:
                return dp[n]
            #base case
            if n == 1:
                dp[n] = nums[0]
                return dp[n]
            if n == 2:
                dp[n] = max(nums[0], nums[1])
                return dp[n]
            dp[n] = max(nums[0] + f(nums[2:],n-2),f(nums[1:],n-1))
            return dp[n]
        return f(nums,n)