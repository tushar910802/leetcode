class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Get the lengths of both input strings
        len_str1, len_str2 = len(str1), len(str2)
      
        # Dynamic programming table f, where f[i][j] will store the length of the 
        # longest common subsequence of str1[:i] and str2[:j]
        dp_table = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]
      
        # Build the table in bottom-up manner
        for i in range(1, len_str1 + 1):
            for j in range(1, len_str2 + 1):
                # If characters match, add 1 to the diagonal value
                if str1[i - 1] == str2[j - 1]:
                    dp_table[i][j] = dp_table[i - 1][j - 1] + 1
                # Otherwise, take the maximum value from above or left cell
                else:
                    dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])
      
        # This will hold the shortest common supersequence characters
        sscs = []
      
        # Initialize pointers for both strings
        i, j = len_str1, len_str2
      
        # Trace back from the bottom-right corner of the table
        while i > 0 or j > 0:
            if i == 0:
                # If we've finished str1, add remaining str2 characters
                j -= 1
                sscs.append(str2[j])
            elif j == 0:
                # If we've finished str2, add remaining str1 characters
                i -= 1
                sscs.append(str1[i])
            else:
                # Follow the path of the longest common subsequence
                if dp_table[i][j] == dp_table[i - 1][j]:
                    i -= 1
                    sscs.append(str1[i])
                elif dp_table[i][j] == dp_table[i][j - 1]:
                    j -= 1
                    sscs.append(str2[j])
                else:
                    # If characters match, go diagonally up-left and add the character
                    i -= 1
                    j -= 1
                    sscs.append(str1[i])
      
        # The sscs list contains the shortest common supersequence in reverse order;
        # reverse it to get the correct sequence
        return ''.join(sscs[::-1])