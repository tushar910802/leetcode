class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        """
        Determines if it is possible to transform the given list `nums` into 
        a strictly increasing sequence by repeatedly subtracting prime numbers 
        from each element. The prime number chosen to subtract from `nums[i]` 
        must be smaller than `nums[i]` - `nums[i+1]` to ensure each element 
        remains less than the following one.

        Parameters:
        nums (List[int]): The list of integers to be modified.

        Returns:
        bool: True if it's possible to make `nums` strictly increasing, 
              False otherwise.
        """
        
        # Step 1: Generate a list of prime numbers up to the largest number in `nums`
        primes = []
        for i in range(2, max(nums)):
            # Check if `i` is prime by attempting division with known primes
            for j in primes:
                if i % j == 0:
                    break
            else:
                # `i` is prime if it is not divisible by any earlier prime
                primes.append(i)

        # Step 2: Attempt to transform `nums` into a strictly increasing sequence
        n = len(nums)
        for i in range(n - 2, -1, -1):  # Start from the second-to-last element and move left
            # If the current number is already smaller than the next, no need to change it
            if nums[i] < nums[i + 1]:
                continue

            # Find the largest prime that can be subtracted from `nums[i]`
            # while ensuring `nums[i]` < `nums[i + 1]` after the operation
            j = bisect_right(primes, nums[i] - nums[i + 1])

            # Check if the result after subtraction would violate the conditions
            # or if there's no suitable prime to perform the subtraction
            if j == len(primes) or primes[j] >= nums[i]:
                return False  # Not possible to create a strictly increasing sequence

            # Subtract the selected prime to make `nums[i]` smaller than `nums[i + 1]`
            nums[i] -= primes[j]

        return True  # Transformation is successful