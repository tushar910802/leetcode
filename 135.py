class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        This function calculates the minimum number of candies required to distribute among a group of children such that
        every child gets the same number of candies and the children with the highest and lowest ratings get the maximum number of candies.

        Args:
            ratings (List[int]): A list of ratings of the children.

        Returns:
            int: The minimum number of candies required.
        """
        n = len(ratings)

        ans = 0
        l = [1] * n
        r = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                l[i] = l[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                r[i] = r[i + 1] + 1

        for a, b in zip(l, r):
            ans += max(a, b)

        return ans



## 135. Candy
