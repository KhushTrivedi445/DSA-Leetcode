class Solution(object):
    def maxProfit(self, prices):
        buy = 0
        sell = 1
        max_profit = 0

        while sell < len(prices):

            # Found a cheaper buying price
            if prices[sell] < prices[buy]:
                buy = sell

            # Calculate profit if we sell today
            else:
                current_profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, current_profit)

            # Move to the next day
            sell += 1

        return max_profit
        
        