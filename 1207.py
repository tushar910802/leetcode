class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        Checks if the number of occurrences of each unique element in the given list
        is unique.

        Parameters:
        - arr (List[int]): The input list of integers.

        Returns:
        - bool: True if the number of occurrences of each unique element is unique,
                False otherwise.

        Example:
        uniqueOccurrences([1, 2, 2, 3, 3, 3]) should return True, as the occurrences
        are [1, 2, 3] with counts [1, 2, 3], which are all unique.

        Note:
        - The function uses a Counter to count the occurrences of each unique element.
        - It then checks if the counts themselves are unique.
        
        Complexity:
        - Time: O(N), where N is the length of the input list.
        - Space: O(U), where U is the number of unique elements in the input list.
        """
        count = collections.Counter(arr)
        occurrences = set()

        for value in count.values():
            if value in occurrences:
                return False
            occurrences.add(value)

        return True