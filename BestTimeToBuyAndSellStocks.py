import sys
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None:
            return None
        if len(prices) <= 1:
            return prices[0]
        max_profit = 0
        max_profit_purchase = prices[0]
        for i in range(1, len(prices)):
            potential_profit = prices[i] - max_profit_purchase
            max_profit = max(max_profit, potential_profit)
            max_profit_purchase = min(max_profit_purchase, prices[i])
        return max_profit

if __name__ == '__main__':
    arr = [7,1,5,3,6,4]
    s = Solution()
    print(s.maxProfit(arr))
    arr = [7,6,4,3,1]
    print(s.maxProfit(arr))
# max_profit = -6
# max_profit_purchase = 7
#
# max_profit = -6
# max_profit_purchase = 1
#
# max_profit = 4
# max_profit_purchase = 1
#
# max_profit = 2
# max_profit_purchase = 1
#
# max_profit = 5
# max_profit_purchase = 1


