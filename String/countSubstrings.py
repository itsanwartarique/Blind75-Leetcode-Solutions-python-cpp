class Solution:
    def countSubstrings(self, s: str) -> int:
        #brute force 
        # def isPlaindrome(s):
        #     l,r = 0, len(s) -1
        #     while(l<r):
        #         if s[l] != s[r]:
        #             return False
        #         else:
        #             l +=1
        #             r -=1
        #     return True
        # count = 0
        # for i in range(len(s)):
        #     for j in range(1,len(s)):
        #         temp = s[i:j+1]
        #         if isPlaindrome(temp):
        #             count +=1
        # return count
        
        #optimised
        def countPalindrome(s,l,r):
            count = 0
            while(l>=0 and r<len(s) and s[l] == s[r]):
                count += 1
                l -= 1
                r += 1
            return count  
        res = 0
        for i in range(len(s)):
            res += countPalindrome(s,i,i)
            res += countPalindrome(s,i,i+1)
        return res
            