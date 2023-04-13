class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        Validate if the given pushed and popped sequences correspond to a valid stack operation.
        
        Args:
        pushed (List[int]): A list of integers representing the order in which elements are pushed onto the stack.
        popped (List[int]): A list of integers representing the order in which elements are popped from the stack.

        Returns:
        bool: True if the given sequences correspond to valid stack operations, False otherwise.
        """
        stack = []
        i = 0  # popped's index

        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return not stack

## 946. Validate Stack Sequences
