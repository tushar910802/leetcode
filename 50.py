class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        This function calculates x raised to the power n (i.e., x^n).

        Args:
            x: The base number.
            n: The exponent.

        Returns:
            The value of x^n.
        """
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n & 1:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n // 2)


## 50. Pow(x, n)
