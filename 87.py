class Solution:
    def __init__(self):
        self.map = {} # key: (s1, s2), value: bool
    def isScramble(self, s1: str, s2: str) -> bool:
        """
        Given two strings s1 and s2 of the same length, determines if s2 is a scrambled string of s1.
        A scrambled string of s1 is one that can be constructed by swapping some characters of s1.

        Args:
        - s1 (str): A string
        - s2 (str): A string

        Returns:
        - bool: True if s2 can be formed by scrambling the characters of s1, False otherwise
        """
        if (s1, s2) in self.map:
            return self.map[(s1, s2)]

        if len(s1) != len(s2):
            # Memorization
            self.map[(s1, s2)] = False
            return False

        if s1 == s2:
            # Memorization
            self.map[(s1, s2)] = True
            return True

        # Prunning
        if sorted(s1) != sorted(s2):
            # Memorization
            self.map[(s1, s2)] = False
            return False

        # i starts from 1, otherwise s[0:0] causes RecursionError
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True

            if self.isScramble(s1[:i], s2[len(s2)-i:]) and self.isScramble(s1[i:], s2[:len(s2)-i]):
                return True

        # Memorization
        self.map[(s1, s2)] = False
        return False

## 87. Scramble String