class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        sa = [[a,s] for a,s in zip(ages,scores)]

        sa.sort()
        scores = [s for a,s in sa]

        maxScore = 0
        n = len(scores)
        dp = [0] * n

        for i in range(n):
            score = scores[i]
            dp[i] = score

            for j in range(i):
                if scores[j] <= score:
                    dp[i] = max(dp[i],dp[j] + score)
            maxScore = max(maxScore, dp[i])

        return maxScore