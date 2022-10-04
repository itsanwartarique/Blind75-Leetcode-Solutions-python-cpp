class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Initialize frequnecy table
        table = {}
        for c in t:
            table[c] = table.get(c,0) + 1
        
        # Initialize sliding window
        left, right = 0, 0  #window bound
        counter = len(table) # track condition
        res = ['']  # return ans
        res_len = float('inf')
        
        #iterate over String
        while(right<len(s)):
            #expand the window
            right_char = s[right]
            if right_char in table:
                table[right_char] -= 1
                if table[right_char] == 0:
                    counter -= 1
            #meet the condition to stop
            while counter == 0:
                #process the current window
                curr_wind_len = right-left+1
                if curr_wind_len < res_len:
                    res[0] = s[left:right+1]
                    res_len = curr_wind_len
                #contract the window
                left_char = s[left]
                if left_char in table:
                    table[left_char] += 1
                    if table[left_char] == 1:
                        counter +=1   
                left +=1
            right +=1
        return res[0]
        
        