class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        Sorts a string according to a custom order defined by the 'order' string.

        Parameters:
        - order (str): A string defining the custom order of characters.
        - s (str): The input string to be sorted.

        Returns:
        - str: The sorted string according to the custom order.

        Example:
        customSortString("cba", "abcd") should return "cbad", as 'c', 'b', and 'a' are
        placed before 'd' in the custom order.

        Note:
        - The function first counts the occurrences of each character in the input string.
        - It then iterates through the custom order and appends characters from the
          input string according to the custom order.
        - Finally, it appends any remaining characters from the input string in their
          original order.
        - The result is a string sorted according to the custom order.

        Complexity:
        - Time: O(N), where N is the length of the input string.
        - Space: O(1), as the function uses a fixed-size array to store character counts.
        """
        ans = ""
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        for c in order:
            while count[ord(c) - ord('a')] > 0:
                ans += c
                count[ord(c) - ord('a')] -= 1

        for c in string.ascii_lowercase:
            for _ in range(count[ord(c) - ord('a')]):
                ans += c

        return ans