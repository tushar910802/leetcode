class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        """
        Computes the maximum number of consecutive correct answers in the answer key,
        such that at most `k` incorrect answers are allowed in between.

        Args:
            answerKey: A string of T's and F's, where T represents a correct answer and F represents an incorrect answer.
            k: The maximum number of incorrect answers allowed between consecutive correct answers.

        Returns:
            The maximum number of consecutive correct answers in the answer key.
        """
        ans = 0
        maxCount = 0
        count = collections.Counter()

        l = 0
        for r, c in enumerate(answerKey):
            count[c == 'T'] += 1
            maxCount = max(maxCount, count[c == 'T'])
            while maxCount + k < r - l + 1:
                count[answerKey[l] == 'T'] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans

## 2024. Maximize the Confusion of an Exam