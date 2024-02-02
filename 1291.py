class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """
        Generates a list of sequential digits within the specified range.

        Parameters:
        - low (int): The lower bound of the range.
        - high (int): The upper bound of the range.

        Returns:
        - List[int]: A list of sequential digits within the specified range.

        Example:
        sequentialDigits(100, 300) should return [123, 234], as these are the
        sequential digits between 100 and 300 (inclusive).

        Note:
        - The function iterates through the digits from 1 to 9, extending each
          digit sequence until it reaches the upper bound.
        - It appends valid digits to the result list and sorts the list before returning.
        - The result is a list of sequential digits within the specified range.

        Complexity:
        - Time: O(D), where D is the number of digits in the range (log10(high)).
        - Space: O(1), as the function uses constant space for variables.
        """
        a = []

        for i in range(1, 10):
            num = i
            next_digit = i + 1

            while num <= high and next_digit <= 9:
                num = num * 10 + next_digit
                if low <= num <= high:
                    a.append(num)
                next_digit += 1

        a.sort()
        return a