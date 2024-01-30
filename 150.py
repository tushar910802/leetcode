class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluates the value of a given arithmetic expression in Reverse Polish Notation (RPN).

        Parameters:
        - tokens (List[str]): A list of strings representing the RPN expression.

        Returns:
        - int: The result of the evaluation.

        Example:
        evalRPN(["2", "1", "+", "3", "*"]) should return 9, as the RPN expression
        corresponds to (2 + 1) * 3.

        Note:
        - The function uses a stack to keep track of operands and applies operators
          when encountered.
        - It supports addition, subtraction, multiplication, and integer division.
        - The result is the final value after processing all tokens in the RPN expression.

        Complexity:
        - Time: O(N), where N is the number of tokens in the input list.
        - Space: O(N), as the function uses a stack to store intermediate results.
        """
        stack = []
        operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b),
        }

        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(operators[token](a, b))
            else:
                stack.append(int(token))

        return stack[0]