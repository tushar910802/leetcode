class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        Calculates the maximum profit that can be made by buying and selling stocks,
        taking into account a transaction fee.

        Args:
            prices: A list of stock prices.
            fee: The transaction fee.

        Returns:
            The maximum profit.
        """
        sell = 0
        hold = -math.inf

        for price in prices:
            sell = max(sell, hold + price)
            hold = max(hold, sell - price - fee)

        return sell

## 714. Best Time to Buy and Sell Stock with Transaction Fee