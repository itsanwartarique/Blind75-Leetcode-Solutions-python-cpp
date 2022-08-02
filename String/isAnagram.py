class Solution:
#     Method 1
    # def isAnagram(self, s: str, t: str) -> bool:
    #     a = ''.join(sorted(s))
    #     b = ''.join(sorted(t))
    #     if(a!=b):
    #         return False
    #     return True
    
#     Method 2
    def isAnagram(self, s: str, t: str) -> bool:
        n1,n2 = len(s),len(t)
        if(n1 != n2):
            return False
        countS,countT = {},{}
        
        for i in range(n1):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True
            