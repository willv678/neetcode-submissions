class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Two pointers, one at 0 and one at 1
        l, r = 0, 1
        maxP = 0 #Max profit value to return
        while r < (len(prices)): #Iterate through list
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l] #Current profit
                maxP = max(maxP, profit) #Compare to max
            else:
                l = r #Move L all the way up to R
            r += 1
        return maxP
