class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        """
        This function checks if a list of coordinates represents a straight line.

        Args:
            coordinates: A list of lists of integers, where each inner list represents a coordinate.

        Returns:
            True if the coordinates represent a straight line, False otherwise.
        """
        x0, y0, x1, y1 = *coordinates[0], *coordinates[1]
        dx = x1 - x0
        dy = y1 - y0

        return all((x - x0) * dy == (y - y0) * dx for x, y in coordinates)

## 1232. Check If It Is a Straight Line
