class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        """
        Groups the people into groups of the given sizes.

        Args:
            groupSizes: A list of group sizes.

        Returns:
            A list of lists, where each inner list contains the indices of the people in a group.
        """
        ans = []
        groupSizeToIndices = defaultdict(list)

        for i, groupSize in enumerate(groupSizes):
            groupSizeToIndices[groupSize].append(i)

        for groupSize, indices in groupSizeToIndices.items():
            groupIndices = []
            for index in indices:
                groupIndices.append(index)
                if len(groupIndices) == groupSize:
                    ans.append(groupIndices.copy())
                    groupIndices.clear()

        return ans


## 1282. Group the People Given the Group Size They Belong To