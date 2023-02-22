class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        ships = [0 for i in range(days)]
        max_w = max(weights)
        low = max_w
        high = max_w * len(weights) + 1

        while low < high:
            mid = low + (high-low)//2
            if self.solve(weights,mid,ships):
                high=mid
            else:
                low = mid + 1
        return high

    def solve(self,weights,max_w,ships):
        index = 0
        for i in range(len(ships)):
            ships[i] = 0
            while index < len(weights) and ships[i]+weights[index] <= max_w:
                ships[i] += weights[index]
                index += 1
        return index == len(weights)


## 1011. Capacity To Ship Packages Within D Days