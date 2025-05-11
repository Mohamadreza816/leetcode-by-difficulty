class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_price = 0
        best_res = 0
        for i in prices:
            if min_price > i:
                min_price = i
                max_price = i
            elif i > max_price:
                max_price = i
                best_res = max(best_res, max_price - min_price)

        return best_res
