class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Calculates the number of days until a warmer day for each day's temperature.

        Parameters:
        - temperatures (List[int]): A list of integers representing daily temperatures.

        Returns:
        - List[int]: A list where each element represents the number of days until a
          warmer day.

        Example:
        dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) should return
        [1, 1, 4, 2, 1, 1, 0, 0], as for each day, it calculates the number of days until
        the next warmer day.

        Note:
        - The function uses a stack to keep track of indices of temperatures.
        - It iterates through the temperatures, updating the answer for each day by
          popping indices from the stack when a warmer day is found.
        - The result is a list representing the number of days until a warmer day for
          each day's temperature.

        Complexity:
        - Time: O(N), where N is the number of temperatures.
        - Space: O(N), as the function uses a stack to store indices.
        """
        ans = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)

        return ans