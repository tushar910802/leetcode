class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        """
        Finds the winners of a game based on the given list of matches, where each match
        is represented as a list [winner, loser].

        Parameters:
        - matches (List[List[int]]): A list of matches where each match is represented by
        a list [winner, loser].

        Returns:
        - List[List[int]]: A list containing two sublists - the first sublist consists of
        players with 0 losses, and the second sublist consists of players with 1 loss.

        Example:
        findWinners([[1, 2], [3, 1], [2, 4], [5, 3]]) should return [[5], [4]],
        representing players who have 0 losses and 1 loss, respectively.

        Note:
        - Each match is represented as [winner, loser].
        - The function calculates the number of losses for each player and categorizes
        them into two groups: players with 0 losses and players with 1 loss.
        - The result is a list with two sublists, each containing the players in their
        respective categories.

        Complexity:
        - Time: O(N), where N is the number of matches.
        - Space: O(P), where P is the number of players (unique winners and losers).
        """
        ans = [[] for _ in range(2)]
        lossesCount = collections.Counter()

        for winner, loser in matches:
            if winner not in lossesCount:
                lossesCount[winner] = 0
            lossesCount[loser] += 1

        for player, nLosses in lossesCount.items():
            if nLosses < 2:
                ans[nLosses].append(player)

        return [sorted(ans[0]), sorted(ans[1])]