class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]

        for i in range(len(prices)):
            if prices[i] < minBuy:
                minBuy = prices[i]
            
            # At each price, we imagine selling on that day.
            # The profit would be:
            # current price – lowest price seen so far
            if prices[i] - minBuy > maxProfit:
                maxProfit = prices[i] - minBuy

        return maxProfit
