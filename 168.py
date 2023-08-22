class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        return self.convertToTitle((columnNumber - 1) // 26) + chr(ord('A') + (columnNumber - 1) % 26) if columnNumber else ''