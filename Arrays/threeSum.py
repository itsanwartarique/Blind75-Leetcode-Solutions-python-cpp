class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for index,item in enumerate(nums):
            if index > 0 and item == nums[index-1]:
                continue
            l,r = index+1,len(nums) -1
            while(l<r):
                total = item + nums[l] + nums[r]
                if total == 0:
                    res.append([item, nums[l], nums[r]])
                    l +=1
                    while nums[l] == nums[l-1] and l<r:
                        l +=1 
                elif total > 0:
                    r -=1
                else:
                    l +=1
        return res