class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Finds the length of the longest common subsequence of two given strings.

        Parameters:
        - text1 (str): The first input string.
        - text2 (str): The second input string.

        Returns:
        - int: The length of the longest common subsequence.

        Example:
        longestCommonSubsequence("abcde", "ace") should return 3, as "ace" is the
        longest common subsequence.

        Note:
        - The function uses dynamic programming to build a 2D array 'f' where f[i][j]
          represents the length of the longest common subsequence of text1[:i] and
          text2[:j].
        - It iterates through the characters of both strings and updates 'f' based on
          whether the characters match or not.
        - The result is the value stored in f[m][n], where m and n are the lengths of
          text1 and text2, respectively.

        Complexity:
        - Time: O(m*n), where m and n are the lengths of text1 and text2.
        - Space: O(m*n), as the function uses a 2D array of size m+1 x n+1 for
          dynamic programming.
        """
        m = len(text1)
        n = len(text2)
        
        f = []
        
        for i in range(m + 1):
            f.append([])
            for j in range(n + 1):
                f[i].append(0)
                
        for i in range(m):
            for j in range(n):                
                if text1[i] == text2[j]:
                    f[i + 1][j + 1] = f[i][j] + 1
                else:
                    f[i + 1][j + 1] = max(f[i][j + 1], f[i + 1][j])
                    
                                    
        return f[m][n]