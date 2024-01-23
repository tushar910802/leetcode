class Solution:   
    def maxLength(self, arr: List[str]) -> int:
        """
        Finds the maximum length of a concatenated string, choosing non-overlapping
        strings from the given list.

        Parameters:
        - arr (List[str]): A list of strings.

        Returns:
        - int: The maximum length of a concatenated string.

        Example:
        maxLength(["un","iq","ue"]) should return 4, as the maximum length can be
        achieved by concatenating "un" and "iq" to form "uniq".

        Note:
        - The function checks for duplicate characters within each word and ignores
          words with duplicates.
        - It uses a set to store concatenated strings and ensures non-overlapping
          combinations.
        - The result is the maximum length of a concatenated string.

        Complexity:
        - Time: O(N*M), where N is the length of the input list and M is the average
          length of the words in the list.
        - Space: O(N*M), as the function uses a set to store concatenated strings.
        """
        concated = [set()]
        for word in arr:
            # ignore words with dup chars in itself
            if len(set(word)) != len(word):
                continue
            # trick: use a copy of concated to do the iteration while appending to it
            for concat in (_ for _ in concated): 
                if concat & set(word):
                    continue
                concated.append(concat | set(word))
        return max(map(len, concated))