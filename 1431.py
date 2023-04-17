class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)
        return [x + extraCandies >= max_num for x in candies]


## 1431. Kids With the Greatest Number of Candies
