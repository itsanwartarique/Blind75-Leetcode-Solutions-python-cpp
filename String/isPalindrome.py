class Solution:
    # Method 1
    # def isPalindrome(self, s: str) -> bool:
    #     newStr = ""
    #     for char in s:
    #         if char.isalnum():
    #             newStr += char.lower()      
    #     return newStr == newStr[::-1]
    
    # Method 2
      def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        
        while(left < right):
            while left<right and not self.isAlNum(s[left]):
                left +=1
            while right>left and not self.isAlNum(s[right]):
                right -=1
            if(s[left].lower() != s[right].lower()):
                return False
            left, right = left+1,right-1
        return True;  
             
    
      def isAlNum(self, c:str):
        return (ord("A") <= ord(c) <= ord("Z") or
         ord("a") <= ord(c) <= ord("z") or
         ord("0") <= ord(c) <= ord("9")) 
      
      