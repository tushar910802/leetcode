class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        """Calculates the minimum time required to collect all garbage items using a specified travel sequence.

        Args:
            garbage: A list of strings representing the garbage items. Each string represents a pile of garbage,
                    with each character representing a type of garbage.

            travel: A list of integers representing the travel sequence. Each integer represents the index of the
                    next garbage pile to visit.

        Returns:
            An integer representing the minimum time required to collect all garbage items.
        """

        prefix = list(itertools.accumulate(travel))

        def getTime(c: str) -> int:
            """Calculates the time required to collect all garbage items of a specific type (c).

            Args:
                c: The character representing the garbage type.

            Returns:
                An integer representing the time required to collect all garbage items of type c.
            """
            characterCount = 0
            lastIndex = -1
            for i, s in enumerate(garbage):
                if any(g == c for g in s):
                    lastIndex = i
                    characterCount += s.count(c)
            return characterCount + (0 if lastIndex <= 0 else prefix[lastIndex - 1])

        return getTime('M') + getTime('P') + getTime('G')