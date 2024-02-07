class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Sorts characters in the input string based on their frequency.

        Parameters:
        - s (str): The input string.

        Returns:
        - str: The sorted string based on character frequency.
        """
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1
            
        priority_queue = []
        
        for key, value in counter.items():        
            heapq.heappush(priority_queue, (-value, key))
        
        results = ""
        for k in range(len(priority_queue)):      
            pair = heapq.heappop(priority_queue)

            for i in range(-pair[0]):
                results += pair[1]

        
        return results