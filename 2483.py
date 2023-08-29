class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
        Finds the best time to close the shop to minimize the penalty.

        Args:
            customers: A string representing the customers that come to the shop. Each character is either 'Y' (yes) or 'N' (no).

        Returns:
            The best time to close the shop, represented by the index of the customer in `customers`.
        """
        # Initialize the best profit and the best closing time.
        maxProfit = 0
        ans = 0
        profit = 0

        # Iterate over the customers.
        for i, customer in enumerate(customers):
            # Update the profit.
            profit += 1 if customer == 'Y' else -1

            # Update the best profit and the best closing time if necessary.
            if profit > maxProfit:
                maxProfit = profit
                ans = i + 1

        return ans
## 2483. Minimum Penalty for a Shop
