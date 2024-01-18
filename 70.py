class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculates the number of distinct ways to climb to the top of a staircase
        with n steps, where you can climb either 1 or 2 steps at a time.

        Parameters:
        - n (int): The total number of steps in the staircase.

        Returns:
        - int: The number of distinct ways to climb to the top.

        Example:
        climbStairs(3) should return 3, as there are three ways to climb the
        staircase: 1 + 1 + 1, 1 + 2, and 2 + 1.

        Note:
        - The function uses dynamic programming to calculate the number of ways.
        - It builds an array 'f' where f[i] represents the number of ways to climb
          to step i.
        - The final result is stored in f[n-1].

        Complexity:
        - Time: O(N), where N is the number of steps in the staircase.
        - Space: O(N), as the function uses an array of size N for dynamic programming.
        """
        f = []
        
        f.append(1)
        f.append(2)
        
        for i in range(2,n):
            f.append(f[i-1] + f[i-2])
        
        print(f)
        return (f[n-1])