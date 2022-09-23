class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Brute force : copy first row of the matrix to last column of temp matrix
        # row,col= len(matrix),len(matrix[0])
        # res = [[0]*col for i in range(row)]
        # res[1][1] = 8
        # for i in range(row):
        #     for j in range(col):
        #         res[j][col-1-i] = matrix[i][j]
        # return res
        
        # Optimised : first find transepose of the matrix and then reverse each rows
        def reverse(nums):
            l,r = 0,len(nums)-1
            while(l<r):
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1
            return nums
        row,col = len(matrix),len(matrix[0])
        for i in range(row):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for row in matrix:
            reverse(row)
            
        
            