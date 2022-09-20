class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = 2
        size = len(prices) 
        buy = prices[0]
        profit = 0
        i,j = 0,1
        while(j< size):
            #calculate window size
            windowSize = j-i + 1
            #reach window size if have'nt
            if (windowSize <k):
                j +=1
            #when you reach window size do required calculation
            elif(windowSize == k):
                # price is low -> buy
                if prices[j] < buy :
                    buy = prices[j]
                # price is high -> sell
                else:
                    curr_profit = prices[j] - buy
                    profit = max(curr_profit,profit)
                # slide the window
                i +=1      
        return profit