class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        """
        Counts the number of flowers in full bloom at the time of each person's arrival.

        Args:
            flowers: A list of lists, where each inner list contains the start and end time
            of a flower's bloom period.
            people: A list of integers, where each integer represents the time of a person's arrival.

        Returns:
            A list of integers, where each integer represents the number of flowers in full
            bloom at the time of the corresponding person's arrival.
        """
        starts = sorted(s for s, _ in flowers)
        ends = sorted(e for _, e in flowers)
        return [bisect.bisect_right(starts, person) -
                bisect.bisect_left(ends, person)
                for person in people]

## 2251. Number of Flowers in Full Bloom
