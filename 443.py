class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Compresses a list of characters by replacing consecutive groups of the same character
        with the character followed by the number of occurrences of that character.
        
        Args:
        - chars: A list of strings representing the characters to be compressed.
        
        Returns:
        - The length of the compressed list of characters. The compressed list is stored in-place
        in the original list passed as argument.
        """
        ans = 0
        i = 0

        while i < len(chars):
            letter = chars[i]
            count = 0
            while i < len(chars) and chars[i] == letter:
                count += 1
                i += 1
            chars[ans] = letter
            ans += 1
            if count > 1:
                for c in str(count):
                    chars[ans] = c
                    ans += 1

        return ans

## 443. String Compression