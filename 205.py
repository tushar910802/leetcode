class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Determines if two strings are isomorphic, i.e., if characters in one string can be
        replaced to get the other string.

        Parameters:
        - s (str): The first input string.
        - t (str): The second input string.

        Returns:
        - bool: True if the strings are isomorphic, False otherwise.

        Example:
        isIsomorphic("egg", "add") should return True, as the characters 'e' and 'a' are
        mapped to 'a', and 'g' and 'd' are mapped to 'd', resulting in isomorphic strings.

        Note:
        - The function uses two dictionaries to map characters from 's' to 't' and vice versa.
        - It iterates through the strings and checks if the mappings are consistent.
        - If the mappings are not consistent, the function returns False.
        - The result is True if the strings are isomorphic, False otherwise.
        """
        letter_map = {}
        reverse_map = {}

        for i in range(len(s)):
            letter_s = s[i]
            letter_t = t[i]

            if letter_s in letter_map and letter_map[letter_s] != letter_t:
                return False
            if letter_t in reverse_map and reverse_map[letter_t] != letter_s:
                return False

            letter_map[letter_s] = letter_t
            reverse_map[letter_t] = letter_s

        return True