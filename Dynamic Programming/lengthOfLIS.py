class Solution:    
     def lengthOfLIS(self, nums: List[int]) -> int:
        # Brute Force
        # def lis(nums,n):
        #     # Base case
        #     if n == 1:
        #         return 0
        #     # Hypothesis
        #     if nums[n-1]>nums[n-2]:
        #         temp1 = 1 + lis(nums[:n-1],n-1)
        #     else:
        #         temp2 = lis(nums[:n-1],n-1)
        #     return max(temp1,temp2)
             
        # Better
        # cache = [[-1]*(len(nums)+1) for i in range(len(nums)+1)]
        # def lis(nums,n):
        #     if cache[n-1][n-2] != -1:
        #         return cache[n-1][n-2]
        #     temp1,temp2 = 0,0
        #     # 1.Base case
        #     if n == 1:
        #         cache[n-1][n-2] = 1
        #         return cache[n-1][n-2]
        #     # 2.Hypothesis
        #     if nums[n-1] > nums[n-2]:
        #         temp1 = 1 +lis(nums[:n-1],n-1)
        #     else:
        #         temp2 = lis(nums[:n-1],n-1)
        #     # 3.Induction
        #     cache[n-1][n-2] = max(temp1,temp2)
        #     return cache[n-1][n-2]
        # return lis(nums,len(nums))
        
        # optimised
        if not nums:
            return 0
        cache = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    cache[i] = max(cache[i],cache[j]+1)
        return max(cache)
        
            
            
            