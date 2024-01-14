class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        Checks if two words are "close" under the following conditions:
        1. They have the same length.
        2. They have the same set of characters.

        Two words are considered "close" if and only if the frequencies of all characters
        in both words can be rearranged to form an anagram.

        Parameters:
        - word1 (str): The first input word.
        - word2 (str): The second input word.

        Returns:
        - bool: True if the words are "close," False otherwise.

        Example:
        closeStrings("abc", "bca") should return True, as "abc" and "bca" are close words.

        Note:
        - The two words must have the same length to be considered close.
        - Close words have the same set of characters, and the frequencies of these
        characters can be rearranged to form an anagram.

        Complexity:
        - Time: O(N log N), where N is the length of the input words.
        - Space: O(C), where C is the number of unique characters in the input words.
        """
        if len(word1) != len(word2):
            return False
        
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        if count1.keys() != count2.keys():
            return False
        
        return sorted(count1.values()) == sorted(count2.values())