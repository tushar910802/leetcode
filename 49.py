class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams together in the given list of strings.

        Parameters:
        - strs (List[str]): The list of strings to group.

        Returns:
        - List[List[str]]: A list of lists where each inner list contains anagrams.
        """
        dict = defaultdict(list)

        for str in strs:
            key = ''.join(sorted(str))
            dict[key].append(str)

        return dict.values()