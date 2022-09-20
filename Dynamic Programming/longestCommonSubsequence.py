class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            memo = [[-1]*1001 for i in range(1001)]
            # Recursive solution
            def lcf(text1,text2,m,n):
                if memo[m][n] != -1:
                    return memo[m][n]
                # Base Case
                for i in range(m+1):
                    for j in range(n+1):
                        if i == 0 or j == 0:
                            memo[i][j] = 0
                
                for i in range(1,m+1):
                    for j in range(1,n+1):
                        if text1[i-1] == text2[j-1]:
                            memo[i][j] = 1 + memo[i-1][j-1]
                        else:
                            memo[i][j] = max(memo[i-1][j],memo[i][j-1])
                return memo[m][n]
            result = lcf(text1,text2,len(text1),len(text2))
            return result

        