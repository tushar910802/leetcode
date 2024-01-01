class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        Finds the maximum number of content children that can be satisfied based on their greed factor and available cookies.

        Args:
        - g (List[int]): List of integers representing the greed factor of each child.
        - s (List[int]): List of integers representing the sizes of available cookies.

        Returns:
        - int: The maximum number of content children that can be satisfied.

        Algorithm:
        1. Sort the lists 'g' (greed factors) and 's' (cookie sizes).
        2. Initialize a cookie index to track available cookies.
        3. Iterate through each child's greed factor.
        4. For each child, find the smallest cookie that can satisfy their greed factor.
        5. If a suitable cookie is found, increment the content children count.
        6. Return the total count of content children.

        Example:
        Solution().findContentChildren([1, 2, 3], [1, 1]) returns 1
        - Explanation: Sorting 'g' as [1, 2, 3] and 's' as [1, 1].
                       The first child (greed 1) can be satisfied with a cookie of size 1.
                       The second child (greed 2) has no available cookies.
                       The third child (greed 3) has no available cookies.
                       Only one child can be content, so the function returns 1.
        """
        g.sort()
        s.sort()
      
        # Initialize the cookie index
        cookie_index = 0
      
        # Iterate through each greed factor
        for child_index, greed in enumerate(g):
            # Move through the cookie sizes until we find a cookie that satisfies the current greed factor
            while cookie_index < len(s) and s[cookie_index] < greed:
                cookie_index += 1
          
            # If there are no more cookies left, return the number of content children so far
            if cookie_index >= len(s):
                return child_index
          
            # Move to the next cookie index assuming the current cookie has been used
            cookie_index += 1
      
        # All children have been content, return the total number of children
        return len(g)