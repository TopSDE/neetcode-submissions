class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0
        buyedStock = prices[0]

        for i in range(n):
            res = max(res, prices[i] - buyedStock)
            buyedStock = min(buyedStock, prices[i])

        return res