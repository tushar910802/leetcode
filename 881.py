class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Returns the minimum number of boats required to rescue all people in the given list of weights,
        where each boat has a maximum weight limit of `limit`.

        Args:
            people (List[int]): A list of integers representing the weights of people to be rescued.
            limit (int): A positive integer representing the maximum weight limit of each boat.

        Returns:
            int: The minimum number of boats required to rescue all people.

        Example:
            >>> numRescueBoats([1,2], 3)
            1
            >>> numRescueBoats([3,2,2,1], 3)
            3
        """
        ans = 0
        i = 0
        j = len(people) - 1

        people.sort()

        while i <= j:
            remain = limit - people[j]
            j -= 1
            if people[i] <= remain:
                i += 1
            ans += 1

        return ans

## 881. Boats to Save People
