class Solution:
    def removeStars(self, s: str) -> str:
        """
            Removes all occurrences of '*' character from a given string, along with the character immediately
            preceding it.

            Args:
            - s (str): The input string to be processed.

            Returns:
            - str: A new string that is obtained by removing all occurrences of '*' character and the character
                immediately preceding it, from the input string. If the input string contains no '*', the function
                returns the input string itself.

            The function iterates through each character in the input string. If the current character is '*', 
            the function removes the previous character from the output list. Otherwise, the function appends the
            current character to the output list. Finally, the function returns a string obtained by joining the
            output list of characters together.
        
        """
        ans = []
        for c in s:
            if c == '*':
                ans.pop()
            else:
                ans.append(c)
        return ''.join(ans)

## 2390. Removing Stars From a String