class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        """
        Sorts a list of integers into two separate lists, one containing even numbers
        and the other containing odd numbers, and then concatenates them in the
        original order.

        Args:
            A (List[int]): A list of integers to be sorted.

        Returns:
            List[int]: A new list containing the elements of the input list `A`,
            sorted in such a way that even numbers appear first, followed by odd numbers.
        """
        B = []  # List to store even numbers
        C = []  # List to store odd numbers

        # Iterate through the input list and categorize numbers as even or odd
        for x in A:
            if x % 2 == 0:
                B.append(x)  # Append even numbers to B
            else:
                C.append(x)  # Append odd numbers to C

        # Concatenate the lists B and C to maintain the original order
        C = B + C

        return C

## 905. Sort Array By Parity
